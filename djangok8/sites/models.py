import datetime
import uuid

from django.contrib.auth.models import User
from django.db import models

class Site(models.Model):

    class Meta:
        verbose_name = 'Site'
        verbose_name_plural = 'Sites'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    site_url = models.CharField(max_length=1200)
    last_check_at = models.DateTimeField(default=datetime.datetime.utcnow())
    status = models.CharField(max_length=200, default='created')

    def __str__(self):
        return self.site_url

