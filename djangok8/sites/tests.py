import datetime

from django.test import TestCase
from django.utils import timezone

from .models import Site


class QuestionModelTests(TestCase):
    site_url = 'https://google.com/'

    def test_url_is_valid(self):
        site = Site(site_url=self.site_url)
        self.assertIs(site.site_url, self.site_url)

    def test_status_is_created_by_default(self):
        site = Site(site_url=self.site_url)
        self.assertIs(site.status, 'created')

    def test_status_ping(self):
        site = Site(site_url=self.site_url)
        status = site.check_availability()
        self.assertIs(status.code, 200)

    def test_status_govnosite(self):
        site = Site(site_url='http://govnosait.govno')
        status = site.check_availability()
        self.assertEqual(status.code, 'down')
        self.assertTrue('Max retr' in status.message)

    def test_update_availability(self):
        site = Site(site_url=self.site_url)
        site.update_availability()
        self.assertIs(site.status, 200)

    def test_iter(self):
        a = [6, 3, 1, 2]
        for x in range(100, 1000, 4):
            print(f'{x}')
