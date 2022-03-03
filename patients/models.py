from datetime import datetime
from django.db import models

GENDER = (("Male", "Male"),
    ("Female",  "Female"),
    ("Other", "Other"))
EDUCATION = ()
RELATION = ()

class Patient(models.Model):
    department = models.CharField(max_length=100)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField()
    email = models.CharField(max_length=100)
    phone_number = models.IntegerField(max_length=10)
    emergency_phone_number = models.IntegerField(max_length=10)
    gender = models.CharField(max_length=100, choices=GENDER)
    # ward = 
    # facility = 


class Family(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField()
    email = models.CharField(max_length=100)
    phone_number = models.IntegerField(max_length=10)
    address = models.CharField(max_length=200)
    gender = models.CharField(max_length=100, choices=GENDER)
    relation = models.CharField(max_length=100, choices=RELATION)
    education = models.CharField(max_length=100, choices=EDUCATION)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)

class DiseaseHistory(models.Model):
    name = models.CharField(max_length=50)
    # treatment = 
    remark = models.CharField(max_length=100)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)

class Treatment(models.Model):
    # given_by =  
    last_updated = models.DateField(default=datetime.now())
    discription = models.CharField(max_length=1000)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)

