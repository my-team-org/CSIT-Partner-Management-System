from django.db import models
from django.contrib.auth.models import User

# Job-related Models
class JobPosition(models.Model):
    
    NAM_CHOICES = [
    ('ai_engineer', 'AI Engineer'),
    ('automation_engineer', 'Automation Engineer'),
    ('backend_developer', 'Backend Developer'),
    ('blockchain_developer', 'Blockchain Developer'),
    ('cloud_engineer', 'Cloud Engineer'),
    ('computer_vision_engineer', 'Computer Vision Engineer'),
    ('cybersecurity_analyst', 'Cybersecurity Analyst'),
    ('data_analyst', 'Data Analyst'),
    ('data_engineer', 'Data Engineer'),
    ('data_scientist', 'Data Scientist'),
    ('database_administrator', 'Database Administrator'),
    ('devops_engineer', 'DevOps Engineer'),
    ('embedded_software_engineer', 'Embedded Software Engineer'),
    ('frontend_developer', 'Frontend Developer'),
    ('fullstack_developer', 'Full Stack Developer'),
    ('game_developer', 'Game Developer'),
    ('game_engine_programmer', 'Game Engine Programmer'),
    ('hardware_engineer', 'Hardware Engineer'),
    ('iot_developer', 'IoT Developer'),
    ('machine_learning_engineer', 'Machine Learning Engineer'),
    ('mobile_developer', 'Mobile Developer'),
    ('network_administrator', 'Network Administrator'),
    ('network_engineer', 'Network Engineer'),
    ('qa_engineer', 'QA Engineer'),
    ('robotics_engineer', 'Robotics Engineer'),
    ('security_engineer', 'Security Engineer'),
    ('site_reliability_engineer', 'Site Reliability Engineer (SRE)'),
    ('software_architect', 'Software Architect'),
    ('software_engineer', 'Software Engineer'),
    ('software_test_engineer', 'Software Test Engineer'),
    ('solutions_architect', 'Solutions Architect'),
    ('systems_administrator', 'Systems Administrator'),
    ('systems_architect', 'Systems Architect'),
    ('ui_ux_designer', 'UI/UX Designer'),
    ('web_developer', 'Web Developer'),
]
    
    job_type = models.CharField(choices= NAM_CHOICES,max_length=50, verbose_name= "ตำแหน่งงาน")  # ชื่อของตำแหน่งงาน
    
    def __str__(self):
        return (self.job_type)

class Job(models.Model):

        
    TYPE_CHOICES_STATUS = [
        ('open', 'เปิดรับสมัคร'),
        ('closed', 'ปิดรับสมัคร'),
    ]
    
    company = models.ForeignKey('Company', on_delete=models.CASCADE, verbose_name="บริษัท",null=True)  # บริษัทที่เปิดรับสมัคร
    
    job_id = models.AutoField(primary_key=True, blank=True)  # ใช้ AutoField เพื่อให้สร้าง ID อัตโนมัติ
    
    job_name = models.ForeignKey(JobPosition, on_delete=models.CASCADE, verbose_name="ชื่อตำแหน่งงาน" ,null=True, blank=True, default="-")  # ชื่อตำแหน่งงาน
    
    job_posted = models.DateTimeField(auto_now_add=True, verbose_name="วันที่ประกาศงาน",null=True, blank=True)  # วันที่ประกาศงาน
              
    job_updated = models.DateTimeField(auto_now=True, verbose_name="วันที่ปรับปรุงข้อมูล", null= True, blank=True)  # วันที่ปรับปรุงข้อมูล
    
    job_quantity = models.IntegerField(verbose_name="จำนวนที่เปิดรับสมัคร",null=True, blank=True)  # จำนวนที่เปิดรับสมัคร
    
    job_description = models.TextField(verbose_name="รายละเอียดงาน" ,null=True, blank=True, default="-")  # รายละเอียดงาน
    
    job_skill = models.TextField(verbose_name="ทักษะที่ต้องการ" ,null=True, blank=True, default="-")  # ทักษะที่ต้องการ
    
    job_department = models.CharField(max_length=255, verbose_name="สาขาวิชา" ,null=True, blank=True)  # แผนกที่เกี่ยวข้อง
    
    job_welfare_benefit = models.TextField(max_length=255, verbose_name="สวัสดิการ" ,null=True, blank=True, default="-")  # สวัสดิการ
    
    job_file = models.FileField(upload_to='uploads/', verbose_name="ไฟล์แนบ" ,null=True, blank=True, default="-")  # ไฟล์แนบ
    
    job_status = models.CharField(max_length=50, choices=TYPE_CHOICES_STATUS, verbose_name= "สถานะ" ,null=True, blank=True)  # สถานะการเปิดรับสมัคร
    
    def __str__(self):
        return f"{self.job_name}"


# Company-related Models
class Company(models.Model):
    TYPE_CHOICES = [
        ('public', 'รัฐวิสาหกิจ'),
        ('private', 'เอกชน'),
        ('government', 'ราชการ'),
    ]

    TYPE_CHOICES_COMPANY = [
        ('partner', 'พาร์ทเนอร์'),
        ('no-partner', 'ไม่ใช่พาร์ทเนอร์'),
    ]

    company_own = models.ForeignKey(User, on_delete=models.CASCADE, related_name="owned_companies")
    
    name_th = models.CharField(max_length=255, verbose_name="ชื่อหน่วยงาน (ไทย)", null=True, blank=True, default="-")
    name_en = models.CharField(max_length=255, verbose_name="ชื่อหน่วยงาน (อังกฤษ)", null=True, blank=True, default="-")
    email = models.EmailField(verbose_name="E-mail หน่วยงาน", null=True, blank=True, default="-")
    website = models.URLField(blank=True, verbose_name="Website หน่วยงาน", null=True, default="-")
    company_type = models.CharField(max_length=50, choices=TYPE_CHOICES_COMPANY, verbose_name="ประเภทบริษัท", null=True, blank=True)
    description = models.TextField(verbose_name="เกี่ยวกับการประกอบการ", null=True, blank=True, default="-")
    head_name = models.CharField(max_length=255, verbose_name="ชื่อหัวหน้าหน่วยงาน", null=True, blank=True, default="-")
    head_position = models.CharField(max_length=100, verbose_name="ตำแหน่ง", null=True, blank=True, default="-")
    address_no = models.CharField(max_length=100, verbose_name="ที่ตั้ง เลขที่", null=True, blank=True, default="-")
    address_moo = models.CharField(max_length=100, verbose_name="หมู่ที่", blank=True, null=True, default="-")
    address_building = models.CharField(max_length=100, verbose_name="ชื่ออาคาร", blank=True, null=True, default="-")
    address_soi = models.CharField(max_length=100, verbose_name="ซอย", blank=True, null=True, default="-")
    address_road = models.CharField(max_length=100, verbose_name="ถนน", blank=True, null=True, default="-")
    province = models.CharField(max_length=100, verbose_name="จังหวัด", null=True, blank=True, default="-")
    district = models.CharField(max_length=100, verbose_name="อำเภอ", null=True, blank=True, default="-")
    subdistrict = models.CharField(max_length=100, verbose_name="ตำบล", null=True, blank=True, default="-")
    postal_code = models.CharField(max_length=10, verbose_name="รหัสไปรษณีย์", null=True, blank=True, default="-")
    phone = models.CharField(max_length=20, verbose_name="โทรศัพท์", null=True, blank=True, default="-")
    company_file = models.FileField(upload_to='uploads/companyfile/', verbose_name="ไฟล์แนบ", null=True, blank=True, default="-")
    company_date_add = models.DateTimeField(auto_now_add=True, verbose_name="วันที่เพิ่มข้อมูลบริษัท", null=True, blank=True)
    logo = models.ImageField(upload_to='uploads/company-logo', verbose_name="โลโก้หน่วยงาน", null=True, blank=True, default="-")

    def __str__(self):
        return self.name_th if self.name_th else self.name_en if self.name_en else "Unnamed Company"


class CompanyImage(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name="ชื่อหน่วยงาน")
    image = models.ImageField(upload_to='static/images/', null=True, blank=True)

    def __str__(self):
        return str(self.company)


# Human Resource Models
class HumanResource(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="ผู้ใช้งาน")
    company = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name="หน่วยงาน")
    contact_name = models.CharField(max_length=255, verbose_name="ชื่อผู้ประสานงาน")
    contact_position = models.CharField(max_length=100, verbose_name="ตำแหน่ง")
    contact_department = models.CharField(max_length=100, verbose_name="แผนก/หน่วย/ฝ่าย")
    contact_email = models.EmailField(verbose_name="E-mail ผู้ประสานงาน",null=True, blank=True, default="-")
    contact_phone = models.CharField(max_length=20, verbose_name="โทรศัพท์ผู้ประสานงาน")

    def __str__(self):
        return self.contact_name


class HumanResourceJob(models.Model):
    human_resource = models.ForeignKey(HumanResource, on_delete=models.CASCADE, verbose_name="ผู้ประสานงาน")
    job = models.ForeignKey(Job, on_delete=models.CASCADE, verbose_name="ตำแหน่งงาน")

    def __str__(self):
        return str(self.human_resource)


# Student-related Models
class Student(models.Model):
    GENDER_CHOICES = [
        ('male', 'ชาย'),
        ('female', 'หญิง'),
        ('other', 'อื่นๆ'),
    ]

    ACADEMIC_YEAR_CHOICES = [
        ('1', '1'),
        ('2', '2'),
    ]

    SOLDIER_CHOICES = [
        ('ผ่านการเกณฑ์ทหาร', 'ผ่านการเกณฑ์ทหาร'),
        ('ยังไม่ผ่านการเกณฑ์ทหาร', 'ยังไม่ผ่านการเกณฑ์ทหาร'),
        ('ได้รับการยกเว้น', 'ได้รับการยกเว้น'),
    ]

    user = models.OneToOneField(
        User, 
        on_delete=models.CASCADE,
        related_name='student'  # เพิ่มบรรทัดนี้
    )
    name = models.CharField(max_length=255, verbose_name="ชื่อนิสิต")
    student_id = models.CharField(max_length=20, verbose_name="รหัสนิสิต")
    field_of_study = models.CharField(max_length=255, verbose_name="สาขาวิชา", blank=True, null=True)
    year = models.IntegerField(verbose_name="ชั้นปี", blank=True, null=True)
    advisor = models.CharField(max_length=255, verbose_name="อาจารย์ที่ปรึกษา", blank=True, null=True)
    academic_year = models.CharField(max_length=9, verbose_name="ปีการศึกษา", blank=True, null=True)
    semester = models.CharField(max_length=10, choices=ACADEMIC_YEAR_CHOICES, verbose_name="ภาคเรียน", blank=True, null=True)
    gpa_term = models.FloatField(verbose_name="เกรดเฉลี่ยภาคเรียนที่ผ่านมา", blank=True, null=True)
    gpa_total = models.FloatField(verbose_name="เกรดเฉลี่ยรวม", blank=True, null=True)
    internship_start_date = models.DateField(verbose_name="วันที่เริ่มปฏิบัติงาน", blank=True, null=True)
    internship_end_date = models.DateField(verbose_name="วันที่สิ้นสุดปฏิบัติงาน", blank=True, null=True)
    id_card = models.CharField(max_length=13, verbose_name="บัตรประจำตัวประชาชนเลขที่", blank=True, null=True)
    id_card_issue_date = models.DateField(verbose_name="วันที่ออกบัตร", blank=True, null=True)
    id_card_expiry_date = models.DateField(verbose_name="วันที่บัตรหมดอายุ", blank=True, null=True)
    national = models.CharField(max_length=50, verbose_name="เชื้อชาติ", blank=True, null=True)
    citizenship = models.CharField(max_length=50, verbose_name="สัญชาติ", blank=True, null=True)
    religion = models.CharField(max_length=50, verbose_name="ศาสนา", blank=True, null=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, verbose_name="เพศ", blank=True, null=True)
    height = models.IntegerField(verbose_name="ส่วนสูง (cm.)", blank=True, null=True)
    weight = models.IntegerField(verbose_name="น้ำหนัก (kg.)", blank=True, null=True)
    disease = models.CharField(max_length=255, blank=True, verbose_name="โรคประจำตัว (ถ้ามี)")
    address = models.TextField(verbose_name="ที่อยู่ปัจจุบัน", blank=True, null=True)
    mobile_phone = models.CharField(max_length=20, verbose_name="โทรศัพท์มือถือ", blank=True, null=True)
    email = models.EmailField(verbose_name="E-mail", blank=True, null=True)
    emergency_contact = models.CharField(max_length=255, verbose_name="บุคคลที่ติดต่อได้ในกรณีฉุกเฉิน", blank=True, null=True)
    relationship = models.CharField(max_length=50, verbose_name="ความเกี่ยวข้องเป็น", blank=True, null=True)
    emergency_phone = models.CharField(max_length=20, verbose_name="โทรศัพท์", blank=True, null=True)
    photo = models.ImageField(upload_to='uploads/student-image/', verbose_name="รูปถ่าย", blank=True, null=True)
    resume = models.FileField(upload_to='uploads/student-resume/', verbose_name="Resume", blank=True, null=True)
    transcript = models.FileField(upload_to='uploads/student-transcript/', verbose_name="Transcript", blank=True, null=True)
    activity_transcript = models.FileField(upload_to='uploads/student-activity-transcript/', verbose_name="Activity Transcript", blank=True, null=True)
    soldier = models.CharField(max_length=50, choices=SOLDIER_CHOICES, verbose_name="สถานะทหาร", blank=True, null=True)

    def __str__(self):
        return self.name


class StudentJob(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name="นิสิต")
    job = models.ForeignKey(Job, on_delete=models.CASCADE, verbose_name="ตำแหน่งงาน")

    def __str__(self):
        return str(self.student)


class application_forms(models.Model):
    id = models.AutoField(primary_key=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    pdf_date = models.DateField()
    pdf_file = models.FileField(upload_to='pdfs/application_forms/%Y/%m/%d/')
    status = models.CharField(max_length=20, choices=[('pending', 'รอการตรวจสอบ'), ('approved', 'อนุมัติ'), ('rejected', 'ปฏิเสธ')], default='pending')
    comment = models.CharField(max_length=255, blank=True , null=True)
    
    def __str__(self):
        return self.student.name


class Review(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE,verbose_name="บริษัท")
    recommend = models.BooleanField(verbose_name="ระดับการแนะนำ")
    overall_rating = models.IntegerField(verbose_name="ภาพรวม")
    benefits_rating = models.IntegerField(verbose_name="สวัสดิการ")
    environment_rating = models.IntegerField(verbose_name="สภาพแวดล้อม")
    management_rating = models.IntegerField(verbose_name="การบริหาร")

    job_type = models.CharField(max_length=255,verbose_name="ตำแหน่งงาน")

    job_description = models.TextField(verbose_name="รายละเอียดงาน")
    experience = models.TextField(verbose_name="ประสบการณ์ที่ได้รับ")
    advice = models.TextField(verbose_name="คำแนะนำ")
    created_at = models.DateTimeField(auto_now_add=True,verbose_name="วันที่สร้าง")

    def str(self):
        if self.company.name_en:
            return f'{self.company.name_th} ({self.company.name_en})'
        return self.company.name_th