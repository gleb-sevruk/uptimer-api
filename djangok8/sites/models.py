import datetime
import uuid

import django
import requests
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class SiteAvailabilityStatus:
    code: int
    message: str

    def __init__(self, code, message):
        self.code = code
        self.message = message


class Site(models.Model):
    class Meta:
        verbose_name = 'Site'
        verbose_name_plural = 'Sites'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    site_url = models.CharField(max_length=1200)
    last_check_at = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=200, default='created')
    status_code = models.IntegerField(default=-1)

    def __str__(self):
        return self.site_url

    def check_availability(self):
        try:
            req = requests.get(self.site_url)
            status = SiteAvailabilityStatus(code=req.status_code, message='ok')
        except requests.exceptions.RequestException as e:
            status = SiteAvailabilityStatus(code='down', message=str(e))

        return status


    def update_availability(self):
        status = self.check_availability()
        self.status = status.code
        self.last_check_at = datetime.datetime.utcnow()
        self.save()

