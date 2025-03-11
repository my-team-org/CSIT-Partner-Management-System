from django.db import models

# Company Model
class Company(models.Model):
    TYPE_CHOICES = [
        ('public', 'รัฐวิสาหกิจ'),
        ('private', 'เอกชน'),
        ('government', 'ราชการ'),
    ]

    name_th = models.CharField(max_length=255, verbose_name="ชื่อหน่วยงาน (ไทย)")
    name_en = models.CharField(max_length=255, verbose_name="ชื่อหน่วยงาน (อังกฤษ)")
    email = models.EmailField(verbose_name="E-mail หน่วยงาน")
    website = models.URLField(blank=True, verbose_name="Website หน่วยงาน")
    company_type = models.CharField(max_length=50, choices=TYPE_CHOICES, verbose_name="ประเภทหน่วยงาน")
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

    contact_name = models.CharField(max_length=255, verbose_name="ชื่อผู้ประสานงาน")
    contact_position = models.CharField(max_length=100, verbose_name="ตำแหน่ง")
    contact_department = models.CharField(max_length=100, verbose_name="แผนก/หน่วย/ฝ่าย")
    contact_email = models.EmailField(verbose_name="E-mail ผู้ประสานงาน")
    contact_phone = models.CharField(max_length=20, verbose_name="โทรศัพท์ผู้ประสานงาน")

    job_title = models.CharField(max_length=100, verbose_name="ตำแหน่งงาน")
    related_field = models.CharField(max_length=255, verbose_name="สาขาวิชาที่เกี่ยวข้อง")
    job_description = models.TextField(verbose_name="รายละเอียดตำแหน่งงาน")
    required_skills = models.TextField(verbose_name="ทักษะพิเศษ")
    benefits = models.TextField(verbose_name="สวัสดิการ")

    def __str__(self):
        return self.name_th

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

    def __str__(self):
        return self.name