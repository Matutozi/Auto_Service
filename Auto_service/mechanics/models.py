from django.db import models
from django.contrib.auth.models import User

class Mechanic(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE),
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    specialization = models.CharField(max_length=100)
    experience_years = models.PositiveIntegerField()
    #rating = models.DecimalField(max_digits=3, decimal_places=2, default=0.00)
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.user.username
