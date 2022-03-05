from asyncio.windows_events import NULL
from datetime import datetime
from django.db import models

from facility.models import Facility, Ward

GENDER = (("Male", "Male"),
    ("Female",  "Female"),
    ("Other", "Other"))
EDUCATION = (("BELOW HIGH SCHOOL", "BELOW HIGH SCHOOL"),
            ("HIGH SCHOOL", "HIGH SCHOOL"),
            ("SECONDARY HIGH SCHOOL", "SECONDARY HIGH SCHOOL"),
            ("BACHELOR", "BACHELOR"),
            ("MASTERS", "MASTERS"),
            ("PHD", "PHD"))

RELATION = (("BROTHER","BROTHER"),("SISTER","SISTER"),("SON","SON"),("DAUGHTER","DAUGHTER"),("FATHER","FATHER"),("MOTHER","MOTHER"), ("HUSBAND","HUSBAND"), ("WIFE","WIFE"))

CARE_TYPE = (('General care', 'General care'),
             ('Genito urinary care', 'Genito urinary care'), 
             ('Gastro-intestinal care', 'Gastro-intestinal care'))
CARE_SUB_TYPE = (('Mouth care','Mouth care'),
                ('Bath', 'Bath'),
                ('Nail cutting', 'Nail cutting'),
                ('Shaving', 'Shaving'))
ICDS_CODE = (("DM", "D-32"),
    ("Hypertension", "HT-58"),
    ("IHD", "IDH-21"),
    ("COPD", "DPOC-144"),
    ("Dementia", "DM-62"),
    ("CVA", "CAV-89"),
    ("Cancer", "C-98"),
    ("CKD", "DC-25"))
class Patient(models.Model):
    address = models.CharField(max_length=100)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField(null=True)
    email = models.CharField(max_length=100)
    landmark = models.CharField(max_length=100)
    phone_number = models.IntegerField(max_length=10)
    emergency_phone_number = models.IntegerField(max_length=10)
    gender = models.CharField(max_length=100, choices=GENDER)
    ward = models.ForeignKey(Ward, on_delete=NULL)
    facility = models.ForeignKey(Facility, on_delete=models.CASCADE)



class Family(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField(null=True)
    email = models.CharField(max_length=100)
    phone_number = models.IntegerField(max_length=10)
    address = models.CharField(max_length=200)
    remarks = models.CharField(max_length=200, null=True)
    gender = models.CharField(max_length=100, choices=GENDER)
    relation = models.CharField(max_length=100, choices=RELATION)
    education = models.CharField(max_length=100, choices=EDUCATION)
    occupation = models.CharField(max_length=50, null=True)
    is_primary = models.BooleanField(default=False)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)

class Disease(models.Model):
    name = models.CharField(max_length=100)
    icds_code: models.CharField(max_length=100, choices=ICDS_CODE)
class DiseaseHistory(models.Model):
    name = models.CharField(max_length=50)
    # treatment = 
    remark = models.CharField(max_length=100)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)

class Treatment(models.Model):
    # given_by =  
    last_updated = models.DateField(default=datetime.now())
    discription = models.CharField(max_length=1000)
    # care_type = models.CharField(max_length=100, choices=CARE_TYPE)
    # care_sub_type = models.CharField(max_length=100, choices=CARE_SUB_TYPE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)

