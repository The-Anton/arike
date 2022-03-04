from django.contrib import admin

from schedule.models import Visit, HealthInfo, Note

admin.sites.site.register(Visit)
admin.sites.site.register(HealthInfo)
admin.sites.site.register(Note)
