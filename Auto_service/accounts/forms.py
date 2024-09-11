from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import CustomUser, Address

class CustomUserCreationForm(UserCreationForm):
    other_name = forms.CharField(max_length=30, required=False)
    date_of_birth = forms.DateField()

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.save()
        if commit:
            custom_user = CustomUser(
                user=user,
                other_name=self.cleaned_data.get('other_name'),
                date_of_birth=self.cleaned_data.get('date_of_birth')
            )
            custom_user.save()
        return user

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['street_address', 'city', 'state', 'country']

class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']

