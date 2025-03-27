# filepath: c:\xampp2\htdocs\Made_chuu\CSIT-Partner-Management-System\CSIT_Partner_Management_System\admin_check\forms.py
from django import forms
from .models import application_forms

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = application_forms
        fields = '__all__'  # Or specify the fields explicitly