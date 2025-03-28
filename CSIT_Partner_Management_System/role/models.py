from django.db import models
from django.contrib.auth.models import User

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
    
    job_id = models.AutoField(primary_key=True)  # ใช้ AutoField เพื่อให้สร้าง ID อัตโนมัติ
    
    job_name = models.ForeignKey(JobPosition, on_delete=models.CASCADE, verbose_name="ชื่อตำแหน่งงาน" ,null=True)  # ชื่อตำแหน่งงาน
    
    job_posted = models.DateTimeField(auto_now_add=True, verbose_name="วันที่ประกาศงาน",null=True)  # วันที่ประกาศงาน
              
    job_updated = models.DateTimeField(auto_now=True, verbose_name="วันที่ปรับปรุงข้อมูล", null= True)  # วันที่ปรับปรุงข้อมูล
    
    job_quantity = models.IntegerField(verbose_name="จำนวนที่เปิดรับสมัคร",null=True)  # จำนวนที่เปิดรับสมัคร
    
    job_description = models.TextField(verbose_name="รายละเอียดงาน" ,null=True)  # รายละเอียดงาน
    
    job_skill = models.TextField(verbose_name="ทักษะที่ต้องการ" ,null=True)  # ทักษะที่ต้องการ
    
    job_department = models.CharField(max_length=255, verbose_name="สาขาวิชา" ,null=True)  # แผนกที่เกี่ยวข้อง
    
    job_welfare_benefit = models.TextField(max_length=255, verbose_name="สวัสดิการ" ,null=True)  # สวัสดิการ
    
    job_file = models.FileField(upload_to='uploads/', verbose_name="ไฟล์แนบ" ,null=True)  # ไฟล์แนบ
    
    job_status = models.CharField(max_length=50, choices=TYPE_CHOICES_STATUS, verbose_name= "สถานะ" ,null=True)
    
    def __str__(self):
        return f"{self.job_name}"


# Company Model
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
    
    name_th = models.CharField(max_length=255, verbose_name="ชื่อหน่วยงาน (ไทย)")
    name_en = models.CharField(max_length=255, verbose_name="ชื่อหน่วยงาน (อังกฤษ)")
    email = models.EmailField(verbose_name="E-mail หน่วยงาน")
    website = models.URLField(blank=True, verbose_name="Website หน่วยงาน")
    company_types = models.CharField(max_length=50, choices=TYPE_CHOICES, verbose_name="ประเภทหน่วยงาน")
    description = models.TextField(verbose_name="เกี่ยวกับการประกอบการ")

    head_name = models.CharField(max_length=255, verbose_name="ชื่อหัวหน้าหน่วยงาน")
    head_position = models.CharField(max_length=100, verbose_name="ตำแหน่ง")

    address_no = models.CharField(max_length=100, verbose_name="ที่ตั้ง เลขที่")
    address_moo = models.CharField(max_length=100, verbose_name="หมู่ที่", blank=True)
    address_building = models.CharField(max_length=100, verbose_name="ชื่ออาคาร", blank=True)
    address_soi = models.CharField(max_length=100, verbose_name="ซอย", blank=True)
    address_road = models.CharField(max_length=100, verbose_name="ถนน", blank=True)
    province = models.CharField(max_length=100, verbose_name="จังหวัด")
    district = models.CharField(max_length=100, verbose_name="อำเภอ")
    subdistrict = models.CharField(max_length=100, verbose_name="ตำบล")
    postal_code = models.CharField(max_length=10, verbose_name="รหัสไปรษณีย์")
    phone = models.CharField(max_length=20, verbose_name="โทรศัพท์")
    
    company_type = models.CharField(max_length=50, choices=TYPE_CHOICES_COMPANY, verbose_name="ประเภทบริษัท")
    
    company_file = models.FileField(upload_to='uploads/', verbose_name="ไฟล์แนบ")
    
    company_date_add = models.DateTimeField(auto_now_add=True, verbose_name="วันที่เพิ่มข้อมูลบริษัท")

    def __str__(self):
        return self.name_th
    
class Company_image(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name="ชื่อหน่วยงาน")
    image = models.ImageField(upload_to='static/images/', null=True, blank=True) 
    
    def __str__(self):
        return self.company.name_en
    
class HumanResouce(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="ผู้ใช้งาน")
    
    company = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name="หน่วยงาน")
    contact_name = models.CharField(max_length=255, verbose_name="ชื่อผู้ประสานงาน")
    contact_position = models.CharField(max_length=100, verbose_name="ตำแหน่ง")
    contact_department = models.CharField(max_length=100, verbose_name="แผนก/หน่วย/ฝ่าย")
    contact_email = models.EmailField(verbose_name="E-mail ผู้ประสานงาน")
    contact_phone = models.CharField(max_length=20, verbose_name="โทรศัพท์ผู้ประสานงาน")
    
    def __str__(self):
        return self.contact_name

class HumnanResource_Job(models.Model):
    HumanResouce = models.ForeignKey(HumanResouce, on_delete=models.CASCADE, verbose_name="ผู้ประสานงาน")
    Job = models.ForeignKey(Job, on_delete=models.CASCADE, verbose_name="ตำแหน่งงาน")
    
    def __str__(self):
        return f"{self.HumanResouce}, {self.Job}"

# Student Model
class Student(models.Model):
    GENDER_CHOICES = [
        ('male', 'ชาย'),
        ('female', 'หญิง'),
        ('other', 'อื่นๆ'),
    ]

    Academic_Year_CHOICES = [
        ('1', '1'),
        ('2', '2'),
    ]
    
    SOLDIER_CHOICES =[
        ('ผ่านการเกณฑ์ทหาร', 'ผ่านการเกณฑ์ทหาร'),
        ('ยังไม่ผ่านการเกณฑ์ทหาร', 'ยังไม่ผ่านการเกณฑ์ทหาร'),
        ('ได้รับการยกเว้น', 'ได้รับการยกเว้น'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="ผู้ใช้งาน")

    name = models.CharField(max_length=255, verbose_name="ชื่อนิสิต")
    student_id = models.CharField(max_length=20, verbose_name="รหัสนิสิต")
    field_of_study = models.CharField(max_length=255, verbose_name="สาขาวิชา")
    year = models.IntegerField(verbose_name="ชั้นปี")
    advisor = models.CharField(max_length=255, verbose_name="อาจารย์ที่ปรึกษา")
    academic_year = models.CharField(max_length=9, verbose_name="ปีการศึกษา")
    semester = models.CharField(max_length=10,choices=Academic_Year_CHOICES, verbose_name="ภาคเรียน")
    gpa_term = models.FloatField(verbose_name="เกรดเฉลี่ยภาคเรียนที่ผ่านมา")
    gpa_total = models.FloatField(verbose_name="เกรดเฉลี่ยรวม")
    internship_start_date = models.DateField(verbose_name="วันที่เริ่มปฏิบัติงาน")
    internship_end_date = models.DateField(verbose_name="วันที่สิ้นสุดปฏิบัติงาน")
    id_card = models.CharField(max_length=13, verbose_name="บัตรประจำตัวประชาชนเลขที่")
    id_card_issue_date = models.DateField(verbose_name="วันที่ออกบัตร")
    id_card_expiry_date = models.DateField(verbose_name="วันที่บัตรหมดอายุ")
    national = models.CharField(max_length=50, verbose_name="เชื้อชาติ")
    citizenship = models.CharField(max_length=50, verbose_name="สัญชาติ")
    religion = models.CharField(max_length=50, verbose_name="ศาสนา")
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, verbose_name="เพศ")
    height = models.IntegerField(verbose_name="ส่วนสูง (cm.)")
    weight = models.IntegerField(verbose_name="น้ำหนัก (kg.)")
    disease = models.CharField(max_length=255, blank=True, verbose_name="โรคประจำตัว (ถ้ามี)")
    address = models.TextField(verbose_name="ที่อยู่ปัจจุบัน")
    mobile_phone = models.CharField(max_length=20, verbose_name="โทรศัพท์มือถือ")
    email = models.EmailField(verbose_name="E-mail")
    emergency_contact = models.CharField(max_length=255, verbose_name="บุคคลที่ติดต่อได้ในกรณีฉุกเฉิน")
    relationship = models.CharField(max_length=50, verbose_name="ความเกี่ยวข้องเป็น")
    emergency_phone = models.CharField(max_length=20, verbose_name="โทรศัพท์")
    photo = models.ImageField(upload_to='uploads/', verbose_name="รูปถ่าย")
    resume = models.FileField(upload_to='uploads/', verbose_name="Resume")
    transcript = models.FileField(upload_to='uploads/', verbose_name="Transcript")
    activity_transcript = models.FileField(upload_to='uploads/', verbose_name="Activity Transcript")

    soldier = models.CharField(max_length=50, choices= SOLDIER_CHOICES,verbose_name="สถานะทหาร")
        
    def __str__(self):
        return self.name
    
class Student_job(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name="นิสิต")
    job = models.ForeignKey(Job, on_delete=models.CASCADE, verbose_name="ตำแหน่งงาน")
    
    
    def __str__(self):
        return self.student
    
class application_forms(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    pdf_date = models.DateField()
    file = models.FileField(upload_to='media/pdfs/')
    
class Review(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    recommend = models.BooleanField()
    overall_rating = models.IntegerField()
    benefits_rating = models.IntegerField()
    environment_rating = models.IntegerField()
    management_rating = models.IntegerField()
    
    job_type = models.CharField(max_length=255)
    
    job_description = models.TextField()
    experience = models.TextField()
    advice = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Review for {self.company.name_en}'