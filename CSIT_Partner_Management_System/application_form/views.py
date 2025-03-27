from django.shortcuts import render, redirect, get_object_or_404
from django.http import FileResponse
import fitz  # PyMuPDF
import os
from .models import *
from .forms import *

# กำหนด BASE_DIR และพาธฟอนต์
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def application_form(request, company_id=None):
    if company_id:
        company = get_object_or_404(Company, id=company_id)
    else:
        company = None

    if request.method == "POST":
        student_form = StudentForm(request.POST, request.FILES)
        company_form = CompanyForm(request.POST, instance=company)
        human_resource_form = HumanResouceForm(request.POST)
        job_form = JobForm(request.POST)

        if student_form.is_valid():  # ตรวจสอบเฉพาะ student_form
            # บันทึกข้อมูล student
            student = student_form.save(commit=False)
            student.company = company  # เชื่อม Student กับ Company
            student.user = request.user  # กำหนด user จาก request
            student.save()  # บันทึกลงฐานข้อมูล
            
            return redirect('success_page')  # เปลี่ยนไปยังหน้าสำเร็จ
        else:
            print(student_form.errors)  # เพิ่มการดีบัก
    else:
        student_form = StudentForm()
        company_form = CompanyForm(instance=company)
        human_resource_form = HumanResouceForm()
        job_form = JobForm()

    context = {
        'student_form': student_form,
        'company_form': company_form,
        'human_resource_form': human_resource_form,
        'job_form': job_form
    }
    return render(request, 'application_form.html', context)

def success_page(request):
    return render(request, 'success.html')

def fill_and_show_pdf(request):
    input_pdf = os.path.join(BASE_DIR, "static/pdf/SC_Co-op_01.pdf")  # ไฟล์ต้นฉบับ
    output_pdf = os.path.join(BASE_DIR, "static/pdf/filled.pdf")  # ไฟล์ที่แก้ไขแล้ว

    # ดึงข้อมูลนิสิต
    student = get_object_or_404(Student, user=request.user)

    # ตรวจสอบว่ามีนิสิตสมัครงานหรือไม่
    student_jobs = Student_job.objects.filter(student=student)
    if not student_jobs.exists():
        return render(request, 'error.html', {'message': 'นิสิตยังไม่ได้สมัครงาน'})

    # ดึงข้อมูลงานที่นิสิตสมัคร (เลือกงานแรก)
    student_job = student_jobs.first()
    job = student_job.job  # งานที่นิสิตสมัคร

    # ดึงข้อมูล HumanResource ที่เกี่ยวข้องกับ Job
    human_resource_job = get_object_or_404(HumnanResource_Job, Job=job)
    human_resource = human_resource_job.HumanResouce

    # ดึงข้อมูล Company ที่เกี่ยวข้องกับ HumanResource
    company = human_resource.company

    # เปิด PDF และเติมข้อมูล
    doc = fitz.open(input_pdf)
    page = doc[0]  # หน้าแรก

    # สร้างฟอนต์โดยใช้ PyMuPDF font code
    font = fitz.Font("figo")  # ใช้ฟอนต์ Helvetica

    # แทรกฟอนต์ลงในหน้า PDF
    page.insert_font(fontname="F0", fontbuffer=font.buffer)

    # ชื่อสถานประกอบการ/หน่วยงาน ที่ต้องการสมัคร (Name of employer)
    page.insert_text(
        (100, 135),  # ตำแหน่งเริ่มต้น
        company.name_th,
        fontname="F0",  # ฟอนต์ที่ใช้
        fontsize=10,
        color=(0, 0, 0)  # สีฟ้า
    )

    # สมัครงานในตำแหน่ง (Position sought)
    page.insert_text(
        (250, 153),  # ตำแหน่งเริ่มต้น
        str(student_job.job.job_name),
        fontname="F0",  # ฟอนต์ที่ใช้
        fontsize=10,
        color=(0, 0, 0)  # สีฟ้า
    )

     # ระยะเวลาปฏิบัติงานสหกิจศึกษา (4 เดือน) (Period of work) จาก(From)
    page.insert_text(
        (360, 172),  # ตำแหน่งเริ่มต้น
        str(student.internship_start_date.strftime('%d/%m/%Y')),
        fontname="F0",  # ฟอนต์ที่ใช้
        fontsize=10,
        color=(0, 0, 0)  # สีฟ้า
    )

    # ระยะเวลาปฏิบัติงานสหกิจศึกษา (4 เดือน) (Period of work) ถึง(Until)
    page.insert_text(
        (475, 172),  # ตำแหน่งเริ่มต้น
        str(student.internship_end_date.strftime('%d/%m/%Y')),
        fontname="F0",  # ฟอนต์ที่ใช้
        fontsize=10,
        color=(0, 0, 0)  # สีฟ้า
    )

    # ต าแหน่ง ของหัวหน้าหน่วยงานที่ท าหนังสือถึง
    page.insert_text(
        (270, 190),  # ตำแหน่งเริ่มต้น
        str(company.head_position),
        fontname="F0",  # ฟอนต์ที่ใช้
        fontsize=10,
        color=(0, 0, 0)  # สีฟ้า
    )

    # ชื่อ-นามสกุล ของหัวหน้าหน่วยงานที่ท าหนังสือถึง
    page.insert_text(
        (270, 209),  # ตำแหน่งเริ่มต้น
        company.head_name,
        fontname="F0",  # ฟอนต์ที่ใช้
        fontsize=10,
        color=(0, 0, 0)  # สีฟ้า
    )

    # ที่อยู่สถานประกอบการ
    page.insert_text(
        (180, 227),  # ตำแหน่งเริ่มต้น
        company.address_no,
        fontname="F0",  # ฟอนต์ที่ใช้
        fontsize=10,
        color=(0, 0, 0)  # สีฟ้า
    )

        # ที่อยู่สถานประกอบการ
    page.insert_text(
        (265, 227),  # ตำแหน่งเริ่มต้น
        company.address_building,
        fontname="F0",  # ฟอนต์ที่ใช้
        fontsize=10,
        color=(0, 0, 0)  # สีฟ้า
    )

            # ที่อยู่สถานประกอบการ
    page.insert_text(
        (420, 227),  # ตำแหน่งเริ่มต้น
        company.address_soi,
        fontname="F0",  # ฟอนต์ที่ใช้
        fontsize=10,
        color=(0, 0, 0)  # สีฟ้า
    )

                # ที่อยู่สถานประกอบการ
    page.insert_text(
        (533, 227),  # ตำแหน่งเริ่มต้น
        company.address_moo,
        fontname="F0",  # ฟอนต์ที่ใช้
        fontsize=10,
        color=(0, 0, 0)  # สีฟ้า
    )

                    # ที่อยู่สถานประกอบการ
    page.insert_text(
        (100, 245),  # ตำแหน่งเริ่มต้น
        company.address_road,
        fontname="F0",  # ฟอนต์ที่ใช้
        fontsize=10,
        color=(0, 0, 0)  # สีฟ้า
    )

    # ที่อยู่สถานประกอบการ
    page.insert_text(
        (230, 245),  # ตำแหน่งเริ่มต้น
        company.subdistrict,
        fontname="F0",  # ฟอนต์ที่ใช้
        fontsize=10,
        color=(0, 0, 0)  # สีฟ้า
    )

    # ที่อยู่สถานประกอบการ
    page.insert_text(
        (400, 245),  # ตำแหน่งเริ่มต้น
        company.district,
        fontname="F0",  # ฟอนต์ที่ใช้
        fontsize=10,
        color=(0, 0, 0)  # สีฟ้า
    )

    # ที่อยู่สถานประกอบการ
    page.insert_text(
        (110, 263),  # ตำแหน่งเริ่มต้น
        company.province,
        fontname="F0",  # ฟอนต์ที่ใช้
        fontsize=10,
        color=(0, 0, 0)  # สีฟ้า
    )

    # ที่อยู่สถานประกอบการ
    page.insert_text(
        (290, 263),  # ตำแหน่งเริ่มต้น
        company.postal_code,
        fontname="F0",  # ฟอนต์ที่ใช้
        fontsize=10,
        color=(0, 0, 0)  # สีฟ้า
    )

    # ที่อยู่สถานประกอบการ
    page.insert_text(
        (430, 263),  # ตำแหน่งเริ่มต้น
        company.phone,
        fontname="F0",  # ฟอนต์ที่ใช้
        fontsize=10,
        color=(0, 0, 0)  # สีฟ้า
    )

    # ที่อยู่สถานประกอบการ
    page.insert_text(
        (280, 282),  # ตำแหน่งเริ่มต้น
        company.website,
        fontname="F0",  # ฟอนต์ที่ใช้
        fontsize=10,
        color=(0, 0, 0)  # สีฟ้า
    )

    # ที่อยู่สถานประกอบการ
    page.insert_text(
        (472, 282),  # ตำแหน่งเริ่มต้น
        company.email,
        fontname="F0",  # ฟอนต์ที่ใช้
        fontsize=10,
        color=(0, 0, 0)  # สีฟ้า
    )

        # ลักษณะงานที่หน่วยงานต้องการให้นิสิตปฏิบัติงาน
    page.insert_text(
        (90, 318),  # ตำแหน่งเริ่มต้น
        job.job_description,
        fontname="F0",  # ฟอนต์ที่ใช้
        fontsize=10,
        color=(0, 0, 0)  # สีฟ้า
    )

    # ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    # ข้าพเจ้าชื่อ-สกุล (Name – Surname) (นาย/นางสาว)
    page.insert_text(
        (270, 380),  # ตำแหน่งเริ่มต้น
        student.name,
        fontname="F0",  # ฟอนต์ที่ใช้
        fontsize=10,
        color=(0, 0, 0)  # สีฟ้า
    )
    
    # รหัสนิสิต (Student ID. No.)
    page.insert_text(
        (177, 398),  # ตำแหน่งเริ่มต้น
        student.student_id,
        fontname="F0",  # ฟอนต์ที่ใช้
        fontsize=10,
        color=(0, 0, 0)  # สีฟ้า
    )

    # สาขาวิชา (Field of Study)
    page.insert_text(
        (393, 398),  # ตำแหน่งเริ่มต้น
        student.field_of_study,
        fontname="F0",  # ฟอนต์ที่ใช้
        fontsize=10,
        color=(0, 0, 0)  # สีฟ้า
    )

     # นิสิตชั้นปีที่ (Year of study)
    page.insert_text(
        (185, 415),  # ตำแหน่งเริ่มต้น
        str(student.year),
        fontname="F0",  # ฟอนต์ที่ใช้
        fontsize=10,
        color=(0, 0, 0)  # สีฟ้า
    )

    # ชื่ออาจารย์ที่ปรึกษา (Name of academic advisor)
    page.insert_text(
        (265, 435),  # ตำแหน่งเริ่มต้น
        student.advisor,
        fontname="F0",  # ฟอนต์ที่ใช้
        fontsize=10,
        color=(0, 0, 0)  # สีฟ้า
    )

     # เกรดเฉลี่ยภาคการศึกษาที่ผ่านมา (recently received GPA)
    page.insert_text(
        (300, 453),  # ตำแหน่งเริ่มต้น
        str(student.gpa_term),
        fontname="F0",  # ฟอนต์ที่ใช้
        fontsize=10,
        color=(0, 0, 0)  # สีฟ้า
    )

     # เกรดเฉลี่ยรวม (Cumulative GPA)
    page.insert_text(
        (500, 453),  # ตำแหน่งเริ่มต้น
        str(student.gpa_total),
        fontname="F0",  # ฟอนต์ที่ใช้
        fontsize=10,
        color=(0, 0, 0)  # สีฟ้า
    )

    # เชื้อชาติ(Race)
    page.insert_text(
        (140, 522),  # ตำแหน่งเริ่มต้น
        student.national,
        fontname="F0",  # ฟอนต์ที่ใช้
        fontsize=10,
        color=(0, 0, 0)  # สีฟ้า
    )

     # เชื้อชาติ(Race)
    page.insert_text(
        (310, 522),  # ตำแหน่งเริ่มต้น
        student.citizenship,
        fontname="F0",  # ฟอนต์ที่ใช้
        fontsize=10,
        color=(0, 0, 0)  # สีฟ้า
    )
    
    # เชื้อชาติ(Race)
    page.insert_text(
        (460, 522),  # ตำแหน่งเริ่มต้น
        student.religion,
        fontname="F0",  # ฟอนต์ที่ใช้
        fontsize=10,
        color=(0, 0, 0)  # สีฟ้า
    )

    # เพศ (Sex)
    page.insert_text(
        (130, 540),  # ตำแหน่งเริ่มต้น
        student.gender,
        fontname="F0",  # ฟอนต์ที่ใช้
        fontsize=10,
        color=(0, 0, 0)  # สีฟ้า
    )

    # ส่วนสูง (Height)
    page.insert_text(
        (310, 540),  # ตำแหน่งเริ่มต้น
        str(student.height),
        fontname="F0",  # ฟอนต์ที่ใช้
        fontsize=10,
        color=(0, 0, 0)  # สีฟ้า
    )

    # น้ำหนัก (Weight)
    page.insert_text(
        (470, 540),  # ตำแหน่งเริ่มต้น
        str(student.weight),
        fontname="F0",  # ฟอนต์ที่ใช้
        fontsize=10,
        color=(0, 0, 0)  # สีฟ้า
    )

    # โรคประจ าตัว ระบุ (Chronic disease: please specify)
    page.insert_text(
        (300, 558),  # ตำแหน่งเริ่มต้น
        student.disease,
        fontname="F0",  # ฟอนต์ที่ใช้
        fontsize=10,
        color=(0, 0, 0)  # สีฟ้า
    )

    # ที่อยู่ปัจจุบัน (Address)
    page.insert_text(
        (180, 576),  # ตำแหน่งเริ่มต้น
        student.address,
        fontname="F0",  # ฟอนต์ที่ใช้
        fontsize=10,
        color=(0, 0, 0)  # สีฟ้า
    )    

    # โทรศัพท์มือถือ (Mobile phone number)
    page.insert_text(
        (230, 595),  # ตำแหน่งเริ่มต้น
        student.mobile_phone,
        fontname="F0",  # ฟอนต์ที่ใช้
        fontsize=10,
        color=(0, 0, 0)  # สีฟ้า
    )   

    # E-mail address
    page.insert_text(
        (400, 595),  # ตำแหน่งเริ่มต้น
        student.email,
        fontname="F0",  # ฟอนต์ที่ใช้
        fontsize=10,
        color=(0, 0, 0)  # สีฟ้า
    ) 

    # บุคคลที่ติดต่อได้ในกรณีฉุกเฉิน (Contact person in case of emergency)
    # ชื่อ-นามสกุล (Name- Surname)
    page.insert_text(
        (210, 632),  # ตำแหน่งเริ่มต้น
        student.emergency_contact,
        fontname="F0",  # ฟอนต์ที่ใช้
        fontsize=10,
        color=(0, 0, 0)  # สีฟ้า
    )   

    # ความเกี่ยวข้องเป็น (Relationship)
    page.insert_text(
        (210, 650),  # ตำแหน่งเริ่มต้น
        student.relationship,
        fontname="F0",  # ฟอนต์ที่ใช้
        fontsize=10,
        color=(0, 0, 0)  # สีฟ้า
    )   

    # โทรศัพท์ (Tel)
    page.insert_text(
        (410, 650),  # ตำแหน่งเริ่มต้น
        student.emergency_phone,
        fontname="F0",  # ฟอนต์ที่ใช้
        fontsize=10,
        color=(0, 0, 0)  # สีฟ้า
    )

    # ลายมือชื่อผู้สมัคร (Applicant’s signature)
    page.insert_text(
        (400, 822),  # ตำแหน่งเริ่มต้น
        student.name,
        fontname="F0",  # ฟอนต์ที่ใช้
        fontsize=10,
        color=(0, 0, 0)  # สีฟ้า
    )

    """ search_words = [
        'ข้าพเจ้าชื่อ-สกุล (Name  Surname) (นาย/นางสาว)',
        'รหัสนิสิต (Student ID. No.)',
        'สาขาวิชา (Field of Study)',
        'นิสิตชั้นปีที่ (Year of study)',
        'ชื่ออาจารย์ที่ปรึกษา (Name of academic advisor)',
        'เกรดเฉลี่ยภาคการศึกษาที่ผ่านมา (recently received GPA)',
        'เกรดเฉลี่ยรวม (Cumulative GPA)'
        'บัตรออกให้เมื่อวันที่ (Issued date)',
        'หมดอายุวันที่ (Expiry date)',
        'เชื้อชาติ (Race)',
        'สัญชาติ (Nationality)',
        'ศาสนา (Religion)',
        'เพศ (Sex)',
        ' ส่วนสูง (Height)',
        'น้ำหนัก (Weight)',
        'โรคประจ าตัว ระบุ (Chronic disease: please specify)',
        'ที่อยู่ปัจจุบัน (Address)',
        'โทรศัพท์มือถือ (Mobile phone number)',
        'E-mail address',
        'ชื่อ-นามสกุล (Name- Surname)',
        'ความเกี่ยวข้องเป็น (Relationship)',
        'โทรศัพท์ (Tel)'
    ]
    
    # วนลูปทุกหน้าใน PDF
    for page_num, page in enumerate(doc):
        for word in search_words:
            rects = page.search_for(word)  # ค้นหาตำแหน่งของคำ
            for rect in rects:
                print(f"พบคำว่า '{word}' ที่หน้า {page_num + 1} ตำแหน่ง: {rect}") """
    
    # บันทึกไฟล์ PDF ที่แก้ไข
    doc.save(output_pdf)
    doc.close()

    # ส่งไฟล์ PDF ที่ถูกแก้ไขให้ผู้ใช้ดู
    return FileResponse(open(output_pdf, "rb"), content_type="application/pdf")