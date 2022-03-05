from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

from facility.models import District, Facility
ROLES = (("PRIMARY NURSE", "PRIMARY NURSE"), 
        ("SECONDARY NURSE", "SECONDARY NURSE"), 
        ("ADMIN", "ADMIN"))

class CustomAccountManager(BaseUserManager):
        def create_superuser(self, email, password, **other_fields):
                other_fields.setdefault('is_staff', True)
                other_fields.setdefault('is_superuser', True)
                other_fields.setdefault('is_active', True)

                if other_fields.get('is_staff') is not True:
                        raise ValueError(
                        'Superuser must be assigned to is_staff=True.')
                if other_fields.get('is_superuser') is not True:
                        raise ValueError(
                        'Superuser must be assigned to is_superuser=True.')

                return self.create_user(email, password, **other_fields)

        def create_user(self, email, password, **other_fields):
                if not email:
                        raise ValueError("You must provide an email address")
                
                email = self.normalize_email(email)
                user = self.model(email=email, **other_fields)
                user.set_password(password)
                user.save()
                return user


class ArikeUser(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=100, unique=True)
    birth_date = models.DateField(null=True)
    department = models.CharField(max_length=100)
    role = models.CharField(max_length=100, choices=ROLES)
    is_verified = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    district = models.ForeignKey(District, on_delete= models.CASCADE)
    facility = models.ForeignKey(Facility, on_delete= models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELD = ['first_name', 'email', 'role']

    objects = CustomAccountManager()
    
    def __str__(self):
        return self.email
