from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from .models import Mechanic

class MechanicRegister(forms.ModelForm):
    class Meta:
        model = Mechanic
        fields = ['first_name', 'last_name', 'specialization', 'experience_years', 'location']


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']