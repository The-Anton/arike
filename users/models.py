from django.db import models
from django.contrib.auth.models import User

ROLES = (("PRIMARY NURSE", "PRIMARY NURSE"), 
        ("SECONDARY NURSE", "SECONDARY NURSE"), 
        ("ADMIN", "ADMIN"))

class ArikeUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.CharField(max_length=100)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    role = models.CharField(max_length=100, choices=ROLES)

