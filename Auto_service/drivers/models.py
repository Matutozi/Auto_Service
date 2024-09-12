from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Driver(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)

    vehicle_make = models.CharField(max_length=100)
    vehicle_model = models.CharField(max_length=100)
    vehicle_year = models.PositiveIntegerField()
    rating = models.DecimalField(max_digits=3, decimal_places=2, default=5)

    def __str__(self):
        return self.user.username