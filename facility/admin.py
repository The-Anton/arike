from django.contrib import admin
from facility.models import Facility

admin.sites.site.register(Facility)