from django.db import models

KIND = (("PHC","PHC"),
        ("CHC", "CHC"))

LOCAL_BODY_CHOICES = (
    # Panchayath levels
    (1, "Grama Panchayath"),
    (2, "Block Panchayath"),
    (3, "District Panchayath"),
    (4, "Nagar Panchayath"),
    # Municipality levels
    (10, "Municipality"),
    # Corporation levels
    (20, "Corporation"),
    # Unknown
    (50, "Others"),
)

class State(models.Model):
        name = models.CharField(max_length=100)

class District(models.Model):
        name = models.CharField(max_length=100)
        state = models.ForeignKey(State, on_delete=models.CASCADE)

class LSG(models.Model):
        name = models.CharField(max_length=100)
        kind = models.CharField(max_length=100, choices=LOCAL_BODY_CHOICES)
        lsg_body_code = models.CharField(max_length=100, choices=LOCAL_BODY_CHOICES)
        discrict = models.ForeignKey(District, on_delete=models.CASCADE)

class Ward(models.Model):
        name = models.CharField(max_length=100)
        number = models.IntegerField()
        lsg_body = models.ForeignKey(LSG, on_delete=models.CASCADE)
        
class Facility(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    pin_code = models.IntegerField(max_length=6)
    phone_number = models.IntegerField(max_length=10)
    kind = models.CharField(max_length=100, default="PHC", choices=KIND)
    ward = models.ForeignKey(Ward, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

