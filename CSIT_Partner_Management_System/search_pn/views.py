from django.shortcuts import render
from main.models import Company, Job

def company_list(request):
    companies = Company.objects.all()
    jobs = Job.objects.all()

    # รับค่าค้นหาจากผู้ใช้
    company_name = request.GET.get('company_name')
    province = request.GET.get('province')
    job_name = request.GET.get('job_name')

    # กรองข้อมูลตามค่าค้นหาที่ได้รับ
    if company_name:
        companies = companies.filter(name_th__icontains=company_name)  # ค้นหาจากชื่อบริษัท
    if province:
        companies = companies.filter(province__icontains=province)  # ค้นหาจากจังหวัด
    if job_name:
        companies = companies.filter(job__job_name__job_type__icontains=job_name)  # ค้นหาตำแหน่งงาน

    context = {
        'companies': companies.distinct(),  # ใช้ distinct() เพื่อหลีกเลี่ยงข้อมูลซ้ำ
        'jobs': jobs,
    }
    return render(request, 'company_list.html', context)