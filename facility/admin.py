from django.contrib import admin
from facility.models import LSG, State, District, Facility, Ward

admin.sites.site.register(Facility)
admin.sites.site.register(Ward)
admin.sites.site.register(State)
admin.sites.site.register(District)
admin.sites.site.register(LSG)