from datetime import datetime

from celery.task import Task


class TestTask(Task):

    def run(self, *args, **kwargs):
        print('running test task...')
        return True
