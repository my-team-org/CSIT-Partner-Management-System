from django.shortcuts import render,get_object_or_404
from main.models import *

def info(request, job_id):
    # ดึงข้อมูล Job ตาม job_id
    job = get_object_or_404(Job, pk=job_id)
    # ดึง HumanResouce ที่เกี่ยวข้องกับ Job
    hr_job = get_object_or_404(HumnanResource_Job, Job=job)
    hr = hr_job.HumanResouce  # HumanResouce ที่เกี่ยวข้อง
    # ดึง Company ที่เกี่ยวข้องกับ HumanResouce
    company = hr.company
    company_image = Company_image.objects.filter(company=company).first()
    
    return render(request, 'info.html', {
        "job": job,
        "hr": hr,
        "company": company,  # ส่งข้อมูล Company ไปยัง template
        "company_img": company_image,
    })
