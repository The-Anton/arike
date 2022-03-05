from datetime import datetime
from django.db import models
from django.contrib.auth.models import User
from patients.models import Patient
from users.models import ArikeUser

SYMPTOMS = ()
class Visit(models.Model):
    date = models.DateField()
    duration = models.IntegerField()
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    nurse = models.ForeignKey(ArikeUser, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
class HealthInfo(models.Model):
    palliative_phase = models.CharField(max_length=100)
    blood_pressure = models.IntegerField()
    pulse = models.IntegerField()
    blood_sugar = models.IntegerField()
    personal_hygiene = models.CharField(max_length=100)
    mouth_hygiene = models.CharField(max_length=100)
    public_hygiene = models.CharField(max_length=100)
    systemic_examination = models.CharField(max_length=100)
    systemic_examination_details = models.CharField(max_length=100)
    patient_at_peace = models.BooleanField(default=True)
    pain = models.BooleanField(default=False)
    symptoms = models.CharField(max_length=100, choices=SYMPTOMS)
    notes = models.CharField(max_length=100)
    visit = models.ForeignKey(Visit, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

class Note(models.Model):
    last_updated = models.DateTimeField(default=datetime.now())
    created_at= models.DateTimeField(default=datetime.now())
    note = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    given_by = models.ForeignKey(ArikeUser, on_delete=models.SET_NULL, null=True)
    visit = models.ForeignKey(Visit, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)