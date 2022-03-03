from django.db import models

KIND = (("PHC","PHC"),
        ("CHC", "CHC"))

class Facility(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    pin_code = models.IntegerField(max_length=6)
    phone_number = models.IntegerField(max_length=10)
    kind = models.CharField(max_length=100, default="PHC", choices=KIND)
