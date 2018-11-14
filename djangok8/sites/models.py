import datetime
import uuid
from datetime import timedelta

import django
import requests
from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from pyfcm import FCMNotification

from djangok8.sites.tasks import UpdateAvailabilityTask


class SiteAvailabilityStatus:
    code: int
    message: str

    def __init__(self, code, message):
        self.code = code
        self.message = message


class FcmDevice(models.Model):
    class Meta:
        verbose_name = 'Fcm Token'

    fcm_token = models.CharField(max_length=1200, unique=True)
    brand = models.CharField(max_length=200)
    build_number = models.CharField(max_length=200)
    device_id = models.CharField(max_length=100)
    unique_id = models.CharField(max_length=100)
    device_name = models.CharField(max_length=400)
    last_access_date = models.DateTimeField(default=timezone.now)

    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)



class Site(models.Model):
    class Meta:
        verbose_name = 'Site'
        verbose_name_plural = 'Sites'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    site_url = models.CharField(max_length=1200)
    last_check_at = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=200, default='created')
    status_code = models.IntegerField(default=-1)
    update_pending = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)


    def __str__(self):
        return self.site_url

    def check_availability(self):
        try:
            req = requests.head(self.site_url)
            code = req.status_code
            if code == 200:
                code = 'online'
            else:
                code = 'down'
            status = SiteAvailabilityStatus(code=code, message='ok')
        except requests.exceptions.RequestException as e:
            status = SiteAvailabilityStatus(code='down', message=str(e))

        return status

    def update_availability_async(self):
        self.update_pending = True
        self.save()
        UpdateAvailabilityTask.delay(1, site_id=self.id)

    def update_availability(self):
        status = self.check_availability()
        prev_status = self.status
        self.status = status.code
        self.update_pending = False
        self.last_check_at = datetime.datetime.utcnow()
        self.save()
        if prev_status != self.status:
            self.notify_user_about_status_change(prev_status, self.status)

    def notify_user_about_status_change(self, old_status, new_status):
        all_devices = FcmDevice.objects.filter(user=self.user).values_list('fcm_token', flat=True)

        push_service = FCMNotification(api_key=settings.FCM_KEY)
        if new_status == 'down':
            # todo emoji
            title = f'Site went offline'
            msg = f'{self.site_url} - {new_status}'
        else:
            title = f'Back online!'
            msg = f'{self.site_url} - {new_status}'
        print(push_service.notify_multiple_devices(registration_ids=all_devices, message_title=title, message_body=msg, ))
