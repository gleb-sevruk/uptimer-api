from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# set the default Django settings module for the 'celery' program.
from django.conf import settings

from djangok8.sites.tasks import UpdateAllSitesAvailabilityTask
from djangok8.tasks import TestTask

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangok8.settings.local')

app = Celery('djangok8')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()


@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    # Calls test('world') every 30 seconds
    sender.add_periodic_task(30.0, UpdateAllSitesAvailabilityTask(), expires=10)
    sender.add_periodic_task(1.0, TestTask(), expires=10)

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))