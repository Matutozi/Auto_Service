# services/forms.py
from django import forms
from .models import ServiceRequest
from mechanics.models import Mechanic

class ServiceRequestForm(forms.ModelForm):
    mechanic = forms.ModelChoiceField(queryset=Mechanic.objects.all(), required=False)
    description = forms.CharField(widget=forms.Textarea, required=True)

    class Meta:
        model = ServiceRequest
        fields = ['mechanic', 'description', 'status']

   