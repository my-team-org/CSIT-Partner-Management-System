from django import forms
from .models import Student
import re
from django.core.validators import RegexValidator

class StudentProfileForm(forms.ModelForm):
    # เพิ่มฟิลด์เพิ่มเติมที่จำเป็น
    GENDER_CHOICES = [
        ('male', 'ชาย'),
        ('female', 'หญิง'),
        ('other', 'อื่นๆ'),
    ]
    
    SOLDIER_STATUS_CHOICES = [
        ('ผ่านการเกณฑ์ทหาร', 'ผ่านการเกณฑ์ทหาร'),
        ('ยังไม่ผ่านการเกณฑ์ทหาร', 'ยังไม่ผ่านการเกณฑ์ทหาร'),
        ('ได้รับการยกเว้น', 'ได้รับการยกเว้น'),
    ]

    gender = forms.ChoiceField(
        choices=GENDER_CHOICES,
        label='เพศ',
        widget=forms.RadioSelect,
        required=True
    )
    
    soldier_status = forms.ChoiceField(
        choices=SOLDIER_STATUS_CHOICES,
        label='สถานะการเกณฑ์ทหาร',
        required=True
    )
    
    id_card = forms.CharField(
        label='เลขบัตรประชาชน',
        max_length=13,
        validators=[
            RegexValidator(
                regex='^[0-9]{13}$',
                message='กรุณากรอกเลขบัตรประชาชน 13 หลัก'
            )
        ],
        required=True
    )
    
    emergency_contact = forms.CharField(
        label='บุคคลที่ติดต่อได้ในกรณีฉุกเฉิน',
        max_length=255,
        required=True
    )
    
    emergency_phone = forms.CharField(
        label='โทรศัพท์ติดต่อฉุกเฉิน',
        max_length=20,
        required=True
    )

    class Meta:
        model = Student
        fields = [
            'student_id', 'name', 'field_of_study', 'year',
            'mobile_phone', 'email', 'address', 'photo',
            'resume', 'transcript', 'gender', 'id_card',
            'emergency_contact', 'emergency_phone', 'soldier_status',
            'height', 'weight', 'disease', 'advisor',
            'gpa_term', 'gpa_total', 'internship_start_date',
            'internship_end_date', 'national', 'citizenship',
            'religion'
        ]
        widgets = {
            'student_id': forms.TextInput(attrs={
                'pattern': '[0-9]{10}',
                'title': 'กรุณากรอกรหัสนิสิต 10 ตัวเลข'
            }),
            'address': forms.Textarea(attrs={'rows': 3}),
            'year': forms.NumberInput(attrs={'min': 1, 'max': 4}),
            'gpa_term': forms.NumberInput(attrs={'step': 0.01, 'min': 0, 'max': 4}),
            'gpa_total': forms.NumberInput(attrs={'step': 0.01, 'min': 0, 'max': 4}),
            'height': forms.NumberInput(attrs={'min': 100, 'max': 250}),
            'weight': forms.NumberInput(attrs={'min': 30, 'max': 200}),
            'internship_start_date': forms.DateInput(attrs={'type': 'date'}),
            'internship_end_date': forms.DateInput(attrs={'type': 'date'}),
            'disease': forms.Textarea(attrs={'rows': 2, 'placeholder': 'ถ้าไม่มีให้เว้นว่างไว้'}),
        }
        labels = {
            'student_id': 'รหัสนิสิต*',
            'name': 'ชื่อ-นามสกุล*',
            'field_of_study': 'สาขาวิชา*',
            'year': 'ชั้นปี*',
            'mobile_phone': 'โทรศัพท์มือถือ*',
            'email': 'อีเมล*',
            'address': 'ที่อยู่ปัจจุบัน*',
            'photo': 'รูปถ่าย (ขนาด 1-2 นิ้ว)',
            'resume': 'ไฟล์ Resume (PDF)',
            'transcript': 'ไฟล์ Transcript (PDF)',
            'height': 'ส่วนสูง (ซม.)',
            'weight': 'น้ำหนัก (กก.)',
            'disease': 'โรคประจำตัว (ถ้ามี)',
            'gpa_term': 'เกรดเฉลี่ยภาคเรียนล่าสุด',
            'gpa_total': 'เกรดเฉลี่ยรวม',
            'internship_start_date': 'วันที่เริ่มฝึกงาน',
            'internship_end_date': 'วันที่สิ้นสุดฝึกงาน',
            'national': 'เชื้อชาติ',
            'citizenship': 'สัญชาติ',
            'religion': 'ศาสนา',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # กำหนดฟิลด์ที่จำเป็น
        required_fields = [
            'student_id', 'name', 'field_of_study', 'year',
            'mobile_phone', 'email', 'address', 'gender',
            'id_card', 'emergency_contact', 'emergency_phone',
            'soldier_status'
        ]
        
        for field in required_fields:
            self.fields[field].required = True
        
        # กำหนด placeholder
        self.fields['mobile_phone'].widget.attrs.update({'placeholder': 'เช่น 0812345678'})
        self.fields['email'].widget.attrs.update({'placeholder': 'example@email.com'})
        
        # ตั้งค่าฟิลด์ไฟล์
        self.fields['photo'].widget.attrs.update({'accept': 'image/*'})
        self.fields['resume'].widget.attrs.update({'accept': '.pdf'})
        self.fields['transcript'].widget.attrs.update({'accept': '.pdf'})

    def clean_student_id(self):
        student_id = self.cleaned_data.get('student_id')
        if not re.match(r'^\d{10}$', student_id):
            raise forms.ValidationError("รหัสนิสิตต้องเป็นตัวเลข 10 หลัก")
        
        # ตรวจสอบว่าไม่ซ้ำ (ยกเว้นของตัวเอง)
        if self.instance.pk:
            if Student.objects.exclude(pk=self.instance.pk).filter(student_id=student_id).exists():
                raise forms.ValidationError("รหัสนิสิตนี้ถูกใช้งานแล้ว")
        else:
            if Student.objects.filter(student_id=student_id).exists():
                raise forms.ValidationError("รหัสนิสิตนี้ถูกใช้งานแล้ว")
                
        return student_id

    def clean_year(self):
        year = self.cleaned_data.get('year')
        if year < 1 or year > 4:
            raise forms.ValidationError("ชั้นปีต้องอยู่ระหว่าง 1-4")
        return year

    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get('internship_start_date')
        end_date = cleaned_data.get('internship_end_date')
        
        # ตรวจสอบวันที่ฝึกงาน
        if start_date and end_date:
            if start_date > end_date:
                self.add_error('internship_end_date', "วันที่สิ้นสุดต้องไม่น้อยกว่าวันที่เริ่มต้น")
        
        # ตรวจสอบ GPA
        gpa_term = cleaned_data.get('gpa_term')
        gpa_total = cleaned_data.get('gpa_total')
        
        if gpa_term is not None and (gpa_term < 0 or gpa_term > 4):
            self.add_error('gpa_term', "เกรดเฉลี่ยต้องอยู่ระหว่าง 0-4")
            
        if gpa_total is not None and (gpa_total < 0 or gpa_total > 4):
            self.add_error('gpa_total', "เกรดเฉลี่ยต้องอยู่ระหว่าง 0-4")
        
        return cleaned_data