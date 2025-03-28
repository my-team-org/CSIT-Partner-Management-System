from django import forms
from .models import Job


class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['job_name', 'job_description', 'job_skill', 'job_department', 'job_welfare_benefit', 'job_file', 'job_status', 'job_quantity']
        widgets = {
             'job_name': forms.Select(attrs={'class': 'form-control'}),   # ใช้ Select widget พร้อมตัวเลือก
            'job_description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'job_skill': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'job_department': forms.TextInput(attrs={'class': 'form-control'}),
            'job_welfare_benefit': forms.TextInput(attrs={'class': 'form-control'}),  # ใช้ Select widget พร้อมตัวเลือก
            'job_file': forms.FileInput(attrs={'class': 'form-control'}),
            'job_status': forms.Select(attrs={'class': 'form-control'}),
            'job_quantity': forms.NumberInput(attrs={'class': 'form-control'}),
        }

