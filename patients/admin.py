from django.contrib import admin
from patients.models import Patient, Family, DiseaseHistory, Treatment

admin.sites.site.register(Patient)
admin.sites.site.register(Family)
admin.sites.site.register(DiseaseHistory)
admin.sites.site.register(Treatment)
