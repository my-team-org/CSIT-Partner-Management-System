from django import forms
from Core.models import application_forms

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = application_forms
        fields = '__all__'  # Or specify the fields explicitly