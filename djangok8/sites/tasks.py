from __future__ import absolute_import, unicode_literals

from datetime import datetime, timedelta

from celery.task import Task


class UpdateAllSitesAvailabilityTask(Task):
    def run(self, *args, **kwargs):
        from djangok8.sites.models import Site
        since = datetime.utcnow() - timedelta(seconds=120)
        print(f'--- start ---- update ALL since: {since}')
        sites = Site.objects.filter(last_check_at__lte=since)
        for site in sites:
            print(f'--- start ---- async task... site_url: {site.site_url}')
            UpdateAvailabilityTask.delay(1, site_id=site.id)
            print(f'---  end  --    -- async task... site_url: {site.site_url}')


        return True


class UpdateAvailabilityTask(Task):

    def run(self, *args, **kwargs):
        from djangok8.sites.models import Site
        site_id = kwargs["site_id"]
        site = Site.objects.get(pk=site_id)
        if not site:
            print(f'Site with id {id} not found')
            return


        print(f'--- start ---- running task... site_url: {site.site_url}')
        site.update_availability()

        print(f'---  end  --    -- running task... site_url: {site.site_url}')
        return True
