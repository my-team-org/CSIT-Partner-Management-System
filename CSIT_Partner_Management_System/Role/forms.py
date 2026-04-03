import os
from django import forms
from Core.models import Job, JobPosition, Company

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['company', 'job_name', 'job_description', 'job_skill', 
                 'job_department', 'job_welfare_benefit', 'job_file', 
                 'job_status', 'job_quantity']
        
        widgets = {
            'job_name': forms.Select(attrs={
                'class': 'form-control select2',
                'data-placeholder': 'เลือกตำแหน่งงาน'
            }),
            'job_description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'กรุณาระบุรายละเอียดงานและหน้าที่รับผิดชอบ'
            }),
            'job_skill': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'ระบุทักษะที่ต้องการ เช่น Python, Django, การสื่อสารดี'
            }),
            'job_department': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'วิทยาการคอมพิวเตอร์, เทคโนโลยีสารสนเทศ'
            }),
            'job_welfare_benefit': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'ระบุสวัสดิการต่างๆ เช่น ประกันสุขภาพ, โบนัส, วันหยุดพักร้อน'
            }),
            'job_file': forms.FileInput(attrs={
                'class': 'form-control-file',
                'accept': '.pdf,.doc,.docx,.jpg,.png'
            }),
            'job_status': forms.Select(attrs={
                'class': 'form-control'
            }),
            'job_quantity': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': 1,
                'value': 1
            }),
        }
        
        labels = {
            'job_name': 'ตำแหน่งงาน',
            'job_description': 'รายละเอียดงาน',
            'job_skill': 'ทักษะที่ต้องการ',
            'job_department': 'สาขา',
            'job_welfare_benefit': 'สวัสดิการ',
            'job_file': 'เอกสารประกอบ (ถ้ามี)',
            'job_status': 'สถานะประกาศ',
            'job_quantity': 'จำนวนที่รับสมัคร'
        }
    
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        self.company = kwargs.pop('company', None)
        super().__init__(*args, **kwargs)
        
        self._configure_job_name_field()
        self._configure_company_field()
        self._enhance_field_attributes()
    
    def _configure_job_name_field(self):
        """ปรับแต่งฟิลด์ตำแหน่งงาน"""
        self.fields['job_name'].queryset = JobPosition.objects.all()
        self.fields['job_name'].empty_label = "--- กรุณาเลือกตำแหน่งงาน ---"
        self.fields['job_name'].required = True
    
    def _configure_company_field(self):
        """ปรับแต่งฟิลด์บริษัทตามบทบาทผู้ใช้"""
        if 'company' not in self.fields:
            return
            
        is_admin = self.user and self.user.is_superuser
        is_csit = self.user and self.user.groups.filter(name='CSIT').exists()
        
        if is_admin or is_csit:
            # สำหรับ Admin/CSIT - เลือกบริษัทได้
            self.fields['company'].queryset = Company.objects.filter(is_active=True)
            self.fields['company'].empty_label = "--- กรุณาเลือกบริษัท ---"
            self.fields['company'].widget = forms.Select(attrs={
                'class': 'form-control select2',
                'data-placeholder': 'เลือกบริษัท'
            })
        elif self.company:
            # สำหรับ HR - ใช้บริษัทที่กำหนดและซ่อนฟิลด์
            self.fields['company'].initial = self.company
            self.fields['company'].widget = forms.HiddenInput()
        else:
            # กรณีอื่นๆ ซ่อนฟิลด์
            self.fields['company'].widget = forms.HiddenInput()
    
    def _enhance_field_attributes(self):
        """ปรับแต่งคุณสมบัติเพิ่มเติมของฟิลด์"""
        # เพิ่มคำอธิบายช่วยเหลือ
        self.fields['job_quantity'].help_text = "จำนวนพนักงานที่ต้องการรับสมัคร (ขั้นต่ำ 1 ตำแหน่ง)"
        self.fields['job_file'].help_text = "รองรับไฟล์ PDF, Word, และรูปภาพ (ขนาดไม่เกิน 5MB)"
        
        # กำหนดให้บางฟิลด์เป็น required
        required_fields = ['job_name', 'job_description', 'job_quantity', 'job_status']
        for field in required_fields:
            self.fields[field].required = True
            self.fields[field].widget.attrs['required'] = 'required'
    
    def clean_job_quantity(self):
        """ตรวจสอบจำนวนที่รับสมัคร"""
        quantity = self.cleaned_data.get('job_quantity')
        if quantity < 1:
            raise forms.ValidationError("จำนวนที่รับสมัครต้องไม่น้อยกว่า 1 ตำแหน่ง")
        return quantity
    
    def clean_job_file(self):
        """ตรวจสอบไฟล์ที่อัปโหลด"""
        file = self.cleaned_data.get('job_file')
        if file:
            valid_extensions = ['.pdf', '.doc', '.docx', '.jpg', '.png']
            ext = os.path.splitext(file.name)[1].lower()
            if ext not in valid_extensions:
                raise forms.ValidationError("รองรับเฉพาะไฟล์ PDF, Word, และรูปภาพเท่านั้น")
            
            # ตรวจสอบขนาดไฟล์ (ตัวอย่าง: ไม่เกิน 5MB)
            max_size = 5 * 1024 * 1024
            if file.size > max_size:
                raise forms.ValidationError("ขนาดไฟล์ต้องไม่เกิน 5MB")
        return file