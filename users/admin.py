from django.contrib import admin

from users.models import ArikeUser

admin.sites.site.register(ArikeUser)
