from django import forms
from main.models import Company

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = '__all__'
        
        widgets = {
            'name_th': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),
            'name_en': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'example@email.com'}),
            'website': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'https://www.example.com'}),
            'company_type': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'รายละเอียดบริษัท'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'xxx-xxxxxxx'}),
            'company_file': forms.ClearableFileInput(attrs={'class': 'form-control-file', 'accept': 'image/*'}),
            'logo': forms.ClearableFileInput(attrs={'class': 'form-control-file', 'accept': 'image/*'}),
        }

    def clean_company_file(self):
        company_file = self.cleaned_data.get('company_file', None)
        return company_file  # ไม่ตรวจสอบประเภทไฟล์
    
    def save(self, commit=True, user=None):
        company = super().save(commit=False)
        if user:
            company.owner = user  # บันทึก owner ตาม User ที่ล็อกอิน
        if commit:
            company.save()
        return company
