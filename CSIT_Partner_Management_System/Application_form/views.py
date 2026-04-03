import logging
import tempfile
from django.shortcuts import render, redirect, get_object_or_404, reverse
from datetime import date, datetime
from django.core.files import File
from django.http import FileResponse, HttpResponse, HttpResponseBadRequest
from django.contrib import messages
import fitz  # PyMuPDF
import os
from Core.models import *
from .forms import *

# กำหนด BASE_DIR และพาธฟอนต์
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def application_form(request, company_id):
    """
    ฟอร์มสมัครงานและสร้างใบสมัคร PDF
    """
    company = get_object_or_404(Company, id=company_id)
    
    # ดึงข้อมูล HR และงานที่เกี่ยวข้อง
    human_resource = HumanResource.objects.filter(company=company).first()
    human_resource_jobs = HumanResourceJob.objects.filter(human_resource=human_resource) if human_resource else None
    job = human_resource_jobs.first().job if human_resource_jobs and human_resource_jobs.exists() else None

    # ดึงข้อมูลนักศึกษาที่มีอยู่
    student = Student.objects.filter(user=request.user).first()

    if request.method == "POST":
        student_form = StudentForm(request.POST, request.FILES, instance=student)
        if student_form.is_valid():
            student = student_form.save(commit=False)
            student.user = request.user
            student.save()

            if job:
                # อัปเดตหรือสร้าง StudentJob
                StudentJob.objects.update_or_create(
                    student=student,
                    defaults={'job': job}
                )
                
                # สร้าง PDF โดยส่ง company_id ไปด้วย
                try:
                    return fill_and_show_pdf(request, company_id=company_id)
                except Exception as e:
                    logger.error(f"Error generating PDF: {str(e)}", exc_info=True)
                    messages.error(request, f"เกิดข้อผิดพลาดในการสร้างเอกสาร: {str(e)}")
                    return redirect('application_form:application_form', company_id=company_id)
            else:
                messages.error(request, "ไม่พบตำแหน่งงานที่เกี่ยวข้อง")
                return redirect('application_form:application_form', company_id=company_id)
        else:
            for field, errors in student_form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
    else:
        student_form = StudentForm(instance=student)

    context = {
        'student_form': student_form,
        'company': company,
        'human_resource': human_resource,
        'job': job,
    }
    return render(request, 'application_form.html', context)

logger = logging.getLogger(__name__)

def fill_and_show_pdf(request, company_id):
    """
    สร้างไฟล์ PDF และ redirect ไปหน้าประวัติ
    """
    try:
        company = get_object_or_404(Company, id=company_id)
        student = get_object_or_404(Student, user=request.user)
        student_job = get_object_or_404(StudentJob, student=student)
        job = student_job.job  # ตัวแปร job ที่หายไป
        
        # เตรียม path ไฟล์
        input_pdf = os.path.join(BASE_DIR, "static/application_form/pdf/SC_Co-op_01.pdf")
        
        temp_dir = tempfile.mkdtemp()
        output_filename = f"application_{student.student_id}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
        output_pdf_path = os.path.join(temp_dir, output_filename)

        # สร้างและกรอกข้อมูล PDF
        doc = fitz.open(input_pdf)
        try:
            page = doc[0]
            font = fitz.Font("figo")
            page.insert_font(fontname="F0", fontbuffer=font.buffer)

            # ฟังก์ชันช่วยในการแทรกข้อความ
            def insert_text(position, text, fontsize=10):
                if text:
                    page.insert_text(
                        position,
                        str(text),
                        fontname="F0",
                        fontsize=fontsize,
                        color=(0, 0, 0)
                    )

            # กรอกข้อมูลบริษัท
            insert_text((100, 135), company.name_th)
            insert_text((250, 153), job.job_name)
            insert_text((360, 172), student.internship_start_date.strftime('%d/%m/%Y') if student.internship_start_date else "")
            insert_text((475, 172), student.internship_end_date.strftime('%d/%m/%Y') if student.internship_end_date else "")
            insert_text((270, 190), company.head_position)
            insert_text((270, 209), company.head_name)
            
            # ที่อยู่บริษัท
            insert_text((180, 227), company.address_no)
            insert_text((265, 227), company.address_building)
            insert_text((420, 227), company.address_soi)
            insert_text((533, 227), company.address_moo)
            insert_text((100, 245), company.address_road)
            insert_text((230, 245), company.subdistrict)
            insert_text((400, 245), company.district)
            insert_text((110, 263), company.province)
            insert_text((290, 263), company.postal_code)
            insert_text((430, 263), company.phone)
            insert_text((280, 282), company.website)
            insert_text((472, 282), company.email)
            
            # รายละเอียดงาน
            insert_text((90, 318), job.job_description)

            # ข้อมูลนักศึกษา
            insert_text((270, 380), student.name)
            insert_text((177, 398), student.student_id)
            insert_text((393, 398), student.field_of_study)
            insert_text((185, 415), student.year)
            insert_text((265, 435), student.advisor)
            insert_text((300, 453), student.gpa_term)
            insert_text((500, 453), student.gpa_total)
            
            # ข้อมูลส่วนตัว
            insert_text((140, 522), student.national)
            insert_text((310, 522), student.citizenship)
            insert_text((460, 522), student.religion)
            insert_text((130, 540), student.get_gender_display())
            insert_text((310, 540), student.height)
            insert_text((470, 540), student.weight)
            insert_text((300, 558), student.disease)
            insert_text((180, 576), student.address)
            insert_text((230, 595), student.mobile_phone)
            insert_text((400, 595), student.email)
            
            # ผู้ติดต่อฉุกเฉิน
            insert_text((210, 632), student.emergency_contact)
            insert_text((210, 650), student.relationship)
            insert_text((410, 650), student.emergency_phone)
            
            # ลายเซ็น
            insert_text((400, 822), student.name)

            # บันทึกไฟล์ PDF
            doc.save(output_pdf_path)
        finally:
            doc.close()

        # บันทึกข้อมูล ApplicationForm
        with open(output_pdf_path, 'rb') as pdf_file:
            application_forms.objects.update_or_create(
                student=student,
                company=company,
                defaults={
                    'pdf_date': date.today(),
                    'pdf_file': File(pdf_file, name=output_filename),
                    'status': 'pending'
                }
            )

        # สร้าง URL สำหรับดูไฟล์ PDF
        pdf_url = request.build_absolute_uri(
            f'/media/application_forms/{output_filename}'
        )
        
        # ลบไฟล์ชั่วคราว
        try:
            os.remove(output_pdf_path)
            os.rmdir(temp_dir)
        except Exception as e:
            logger.error(f"Error cleaning temp files: {str(e)}")

    # ส่ง URL ไฟล์ PDF ไปยัง template พร้อม redirect
        messages.success(request, "สร้างใบสมัครเรียบร้อยแล้ว")
        return render(request, 'pdf_redirect.html', {
            'pdf_url': pdf_url,
            'history_url': reverse('application_form:application_history')
        })

    except Exception as e:
        logger.error(f"Error in fill_and_show_pdf: {str(e)}", exc_info=True)
        messages.error(request, f"เกิดข้อผิดพลาดในการสร้างเอกสาร: {str(e)}")
        return redirect('application_form:application_form', company_id=company_id)
    
def application_history(request):
    """
    หน้าประวัติการสมัคร
    """
    student = get_object_or_404(Student, user=request.user)
    applications = application_forms.objects.filter(student=student).select_related('company').order_by('-pdf_date')
    
    # นับจำนวนใบสมัคร
    application_count = applications.count()
    
    context = {
        'student': student,
        'applications': applications,
        'application_count': application_count,
    }
    return render(request, 'application_history.html', context)