from django import forms
from .models import Company, Student

# Company Form
class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = '__all__'
        widgets = {
            # ข้อมูลทั่วไป
            'name_th': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'กรอกชื่อหน่วยงาน (ภาษาไทย)'
            }),
            'name_en': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'กรอกชื่อหน่วยงาน (ภาษาอังกฤษ)'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control', 
                'placeholder': 'กรอกอีเมลหน่วยงาน'
            }),
            'website': forms.URLInput(attrs={
                'class': 'form-control', 
                'placeholder': 'กรอกเว็บไซต์หน่วยงาน'
            }),
            'company_type': forms.Select(attrs={
                'class': 'form-select'
            }),
            'description': forms.Textarea(attrs={
                'rows': 3, 
                'class': 'form-control', 
                'placeholder': 'กรอกคำอธิบายเกี่ยวกับบริษัท'
            }),
            # ข้อมูลหัวหน้าหน่วยงาน/ผู้จัดการสถานประกอบการ
            'head_name': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'กรอกชื่อหัวหน้าหน่วยงาน'
            }),
            'head_position': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'กรอกตำแหน่งหัวหน้าหน่วยงาน'
            }),
            # ที่ตั้งหน่วยงาน
            'address_no': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'กรอกเลขที่'
            }),
            'address_moo': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'กรอกหมู่ที่'
            }),
            'address_building': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'กรอกชื่ออาคาร'
            }),
            'address_soi': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'กรอกซอย'
            }),
            'address_road': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'กรอกถนน'
            }),
            'province': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'กรอกจังหวัด'
            }),
            'district': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'กรอกอำเภอ'
            }),
            'subdistrict': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'กรอกตำบล'
            }),
            'postal_code': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'กรอกรหัสไปรษณีย์'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'กรอกโทรศัพท์หน่วยงาน'
            }),
            # ข้อมูลผู้ประสานงาน
            'contact_name': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'กรอกชื่อผู้ประสานงาน'
            }),
            'contact_position': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'กรอกตำแหน่งผู้ประสานงาน'
            }),
            'contact_department': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'กรอกแผนก/หน่วย/ฝ่าย'
            }),
            'contact_email': forms.EmailInput(attrs={
                'class': 'form-control', 
                'placeholder': 'กรอกอีเมลผู้ประสานงาน'
            }),
            'contact_phone': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'กรอกโทรศัพท์ผู้ประสานงาน'
            }),
            # ข้อมูลตำแหน่งงาน
            'job_title': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'กรอกตำแหน่งงาน'
            }),
            'related_field': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'กรอกสาขาวิชาที่เกี่ยวข้อง'
            }),
            'job_description': forms.Textarea(attrs={
                'rows': 3, 
                'class': 'form-control', 
                'placeholder': 'กรอกรายละเอียดตำแหน่งงาน'
            }),
            'required_skills': forms.Textarea(attrs={
                'rows': 3, 
                'class': 'form-control', 
                'placeholder': 'กรอกทักษะพิเศษที่ต้องการ'
            }),
            'benefits': forms.Textarea(attrs={
                'rows': 3, 
                'class': 'form-control', 
                'placeholder': 'กรอกสวัสดิการ'
            }),
        }

# Student Form
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        widgets = {
            # ข้อมูลส่วนตัวนิสิต
            'name': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'กรอกชื่อนิสิต'
            }),
            'student_id': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'กรอกรหัสนิสิต'
            }),
            'field_of_study': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'กรอกสาขาวิชา'
            }),
            'year': forms.NumberInput(attrs={
                'class': 'form-control', 
                'placeholder': 'กรอกชั้นปี'
            }),
            'advisor': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'กรอกชื่ออาจารย์ที่ปรึกษา'
            }),
            'academic_year': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'กรอกปีการศึกษา'
            }),
            'semester': forms.Select(attrs={
                'class': 'form-select'
            }),
            'gpa_term': forms.NumberInput(attrs={
                'class': 'form-control', 
                'placeholder': 'กรอกเกรดเฉลี่ยภาคเรียนที่ผ่านมา'
            }),
            'gpa_total': forms.NumberInput(attrs={
                'class': 'form-control', 
                'placeholder': 'กรอกเกรดเฉลี่ยรวม'
            }),
            'internship_start_date': forms.DateInput(attrs={
                'class': 'form-control', 
                'placeholder': 'กรอกวันที่เริ่มปฏิบัติงาน',
                'type': 'date'
            }),
            'internship_end_date': forms.DateInput(attrs={
                'class': 'form-control', 
                'placeholder': 'กรอกวันที่สิ้นสุดปฏิบัติงาน',
                'type': 'date'
            }),
            'id_card': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'กรอกเลขที่บัตรประจำตัวประชาชน'
            }),
            'id_card_issue_date': forms.DateInput(attrs={
                'class': 'form-control', 
                'placeholder': 'กรอกวันที่ออกบัตร',
                'type': 'date'
            }),
            'id_card_expiry_date': forms.DateInput(attrs={
                'class': 'form-control', 
                'placeholder': 'กรอกวันที่บัตรหมดอายุ',
                'type': 'date'
            }),
            'national': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'กรอกเชื้อชาติ'
            }),
            'citizenship': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'กรอกสัญชาติ'
            }),
            'religion': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'กรอกศาสนา'
            }),
            'gender': forms.Select(attrs={
                'class': 'form-select'
            }),
            'height': forms.NumberInput(attrs={
                'class': 'form-control', 
                'placeholder': 'กรอกส่วนสูง (ซม.)'
            }),
            'weight': forms.NumberInput(attrs={
                'class': 'form-control', 
                'placeholder': 'กรอกน้ำหนัก (กก.)'
            }),
            'disease': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'กรอกโรคประจำตัว (ถ้ามี)'
            }),
            'address': forms.Textarea(attrs={
                'rows': 3, 
                'class': 'form-control', 
                'placeholder': 'กรอกที่อยู่ปัจจุบัน'
            }),
            'mobile_phone': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'กรอกโทรศัพท์มือถือ'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control', 
                'placeholder': 'กรอกอีเมล'
            }),
            'emergency_contact': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'กรอกชื่อบุคคลที่ติดต่อได้ในกรณีฉุกเฉิน'
            }),
            'relationship': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'กรอกความเกี่ยวข้อง'
            }),
            'emergency_phone': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'กรอกโทรศัพท์บุคคลที่ติดต่อได้ในกรณีฉุกเฉิน'
            }),
            'photo': forms.ClearableFileInput(attrs={
                'class': 'form-control', 
                'title': 'อัพโหลดรูปถ่าย'
            }),
            'resume': forms.ClearableFileInput(attrs={
                'class': 'form-control', 
                'accept': '.pdf,.doc,.docx', 
                'title': 'อัพโหลดประวัติส่วนตัว (Resume)'
            }),
            'transcript': forms.ClearableFileInput(attrs={
                'class': 'form-control', 
                'accept': '.pdf,.jpg,.jpeg,.png', 
                'title': 'อัพโหลดใบแสดงผลการศึกษา (Transcript)'
            }),
            'activity_transcript': forms.ClearableFileInput(attrs={
                'class': 'form-control', 
                'accept': '.pdf,.jpg,.jpeg,.png', 
                'title': 'อัพโหลดใบแสดงผลการเข้าร่วมกิจกรรม (Activity Transcript)'
            }),
        }