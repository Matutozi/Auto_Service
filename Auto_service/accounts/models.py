from django.db import models
from django.contrib.auth.models import User

# Create your models here.
    

class CustomUser(models.Model):
    """Class that stores all the user information"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #zip_code = models.CharField(max_length=6)
    other_name = models.CharField(max_length=30, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    date_of_birth = models.DateField()
    #profile_picture = models.ImageField(default="defalut_profile_pics.jpg", upload_to="profile_pictures")

    def __str__(self):
        return self.user.username
    
class Address(models.Model):
    """Class that handles all information relating to address"""
    
    custom_user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)  # Link to CustomUser
    street_address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=25)

    def __str__(self):
        return f"{self.street_address}, {self.city}, {self.state}, {self.country}"