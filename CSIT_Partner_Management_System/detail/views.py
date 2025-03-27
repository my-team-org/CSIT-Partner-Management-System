from django.shortcuts import get_object_or_404, render
from main.models import *

def detail(request):
    company = get_object_or_404(Company, pk=1)
    company_image = Company_image.objects.filter(company=company).first()
    hr = get_object_or_404(HumanResouce, company=company)
    hr_job = HumnanResource_Job.objects.filter(HumanResouce=hr)
    jobs = Job.objects.filter(job_id__in=hr_job.values_list('Job', flat=True))  # ดึงข้อมูล Job ที่เกี่ยวข้อง
    reviews = Review.objects.filter(company=company)
    return render(request, 'detail.html', {
        "company": company,
        "company_img": company_image,
        "hr": hr,
        "hr_job": hr_job,
        "jobs": jobs,  # ส่งข้อมูล Job ไปยัง template
        "reivews": reviews
    })