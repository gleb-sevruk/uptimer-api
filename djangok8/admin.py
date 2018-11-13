from django.contrib import admin

from djangok8.sites.models import FcmDevice


class FcmDeviceAdmin(admin.ModelAdmin):
    list_display = ('fcm_token',  'device_name')


admin.site.register(FcmDevice, FcmDeviceAdmin)