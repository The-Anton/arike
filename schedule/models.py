from django.db import models
from django.contrib.auth.models import User
from patients.models import Patient

class Visit(models.Model):
    date = models.DateField()
    duration = models.IntegerField()
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)


class Health_info(models.Model):
    palliative_phase = models.CharField(max_length=100)
    blood_pressure = models.IntegerField()
    pulse = models.IntegerField()
    blood_sugar = models.IntegerField()
    personal_hygiene = models.CharField(max_length=100)
    mouth_hygiene = models.CharField(max_length=100)
    systemic_examination = models.CharField(max_length=100)
    systemic_examination_details = models.CharField(max_length=100)
    notes = models.CharField(max_length=100)
    visit = models.ForeignKey(Visit, on_delete=models.CASCADE)


class Note(models.Model):
    last_updated = models.DateTimeField()
    created_updated = models.DateTimeField()
    content = models.CharField(max_length=100)
    given_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    visit = models.ForeignKey(Visit, on_delete=models.CASCADE)
