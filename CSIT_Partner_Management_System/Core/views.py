from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from .models import Company, Job, Student
from .forms import StudentProfileForm

# ฟังก์ชันตรวจสอบว่านิสิตหรือไม่
def is_student(user):
    return user.groups.filter(name='student').exists()

def is_company(user):
    return user.groups.filter(name='hr').exists()

def is_csit(user):
    return user.groups.filter(name='csit').exists()

@login_required
def index(request):
    if is_student(request.user):
        return render(request, 'Core/home_st.html')
    if is_company(request.user):
        return render(request, 'Core/home_hr.html')
    if is_csit(request.user):
        return render(request, 'Core/home_csit.html')


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
    return render(request, 'Core/company_list.html', context)

@login_required
def edit_student(request):
    student = get_object_or_404(Student, user=request.user)

    if request.method == 'POST':
        form = StudentProfileForm(
            request.POST, 
            request.FILES, 
            instance=student
        )
        if form.is_valid():
            # ตรวจสอบว่าไม่มีการใช้รหัสนิสิตซ้ำ
            new_student_id = form.cleaned_data['student_id']
            if Student.objects.exclude(pk=student.pk).filter(student_id=new_student_id).exists():
                messages.error(request, "รหัสนิสิตนี้ถูกใช้งานแล้ว")
            else:
                form.save()
                messages.success(request, "อัปเดตข้อมูลเรียบร้อยแล้ว!")
                return redirect('student_profile')
    else:
        form = StudentProfileForm(instance=student)

    return render(request, 'Core/edit_student.html', {
        'form': form,
        'student': student
    })