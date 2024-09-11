from django import forms
from .models import Driver
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class DriverRegisterForm(forms.ModelForm):
    class Meta:
        model = Driver
        fields = ['first_name', 'last_name', 'vehicle_make', 'vehicle_model', 'vehicle_year']

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']