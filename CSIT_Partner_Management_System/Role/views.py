from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from Core.models import Job, Company, HumanResource, HumanResourceJob
from .forms import JobForm
from django.utils.timezone import now
from django import forms

def is_hr_or_csit(user):
    """Check if user is HR or CSIT"""
    return (
        HumanResource.objects.filter(user=user).exists() or 
        user.groups.filter(name='CSIT').exists()
    )

def get_user_company(user):
    """Get company for HR or return None for CSIT (to allow selection)"""
    if HumanResource.objects.filter(user=user).exists():
        return HumanResource.objects.get(user=user).company
    # สำหรับ CSIT จะคืนค่า None เพื่อให้สามารถเลือกบริษัทได้
    return None

@login_required
@user_passes_test(is_hr_or_csit, login_url='/accounts/unauthorized/')
def add_job(request):
    try:
        is_csit = request.user.groups.filter(name='CSIT').exists()
        company = get_user_company(request.user)
        
        if request.method == "POST":
            form = JobForm(request.POST, request.FILES, user=request.user, company=company)
            
            if form.is_valid():
                job = form.save(commit=False)
                job.created_by = request.user
                
                # สำหรับ HR ที่ซ่อนฟิลด์ company
                if not is_csit and company:
                    job.company = company
                
                job.save()
                form.save_m2m()
                
                # เพิ่มข้อมูลในตาราง HumanResourceJob
                if not is_csit:  # ถ้าเป็น HR
                    human_resource = HumanResource.objects.get(user=request.user)
                    HumanResourceJob.objects.create(
                        human_resource=human_resource,
                        job=job
                    )
                
                messages.success(request, 'สร้างประกาศงานใหม่เรียบร้อยแล้ว!')
                return redirect('job_list')
            else:
                for field, errors in form.errors.items():
                    for error in errors:
                        messages.error(request, f"{field}: {error}")
        else:
            form = JobForm(user=request.user, company=company)
            
        return render(request, 'add_job.html', {
            'form': form,
            'is_csit': is_csit
        })

    except Exception as e:
        messages.error(request, f'เกิดข้อผิดพลาด: {str(e)}')
        return redirect('core:home')

@login_required
@user_passes_test(is_hr_or_csit)
def edit_add_job(request, job_id):
    try:
        company = get_user_company(request.user)
        job = get_object_or_404(Job, pk=job_id)
        
        # ตรวจสอบสิทธิ์การแก้ไข
        if not (request.user.groups.filter(name='CSIT').exists() or job.company == company):
            messages.error(request, 'คุณไม่มีสิทธิ์แก้ไขงานนี้')
            return redirect('core:home')
        
        if request.method == "POST":
            form = JobForm(request.POST, request.FILES, instance=job)
            
            if form.is_valid():
                job = form.save(commit=False)
                job.updated_at = now()
                job.save()
                
                if hasattr(form, 'save_m2m'):
                    form.save_m2m()
                
                messages.success(request, 'อัปเดตงานเรียบร้อยแล้ว!')
                return redirect('job_list')
            else:
                for field, errors in form.errors.items():
                    for error in errors:
                        messages.error(request, f"{form.fields[field].label}: {error}")
        else:
            form = JobForm(instance=job)
            form.fields['company'].widget = forms.HiddenInput()
            form.initial['company'] = job.company

        return render(request, 'edit_add_job.html', {
            'form': form,
            'job': job
        })

    except Exception as e:
        messages.error(request, f'เกิดข้อผิดพลาด: {str(e)}')
        return redirect('core:home')

@login_required
@user_passes_test(is_hr_or_csit)
def job_list(request):
    try:
        company = get_user_company(request.user)
        
        if request.user.groups.filter(name='CSIT').exists():
            # CSIT สามารถเห็นทุกงาน
            jobs = Job.objects.all().order_by('-job_posted')
        else:
            # HR เห็นเฉพาะงานของบริษัทตัวเอง
            jobs = Job.objects.filter(company=company).order_by('-job_posted')
        
        return render(request, 'job_list.html', {
            'jobs': jobs,
            'company': company,
            'is_csit': request.user.groups.filter(name='CSIT').exists()
        })

    except Exception as e:
        messages.error(request, f'เกิดข้อผิดพลาด: {str(e)}')
        return redirect('core:home')

@login_required
@user_passes_test(is_hr_or_csit)
def delete_job(request, job_id):
    try:
        company = get_user_company(request.user)
        job = get_object_or_404(Job, pk=job_id)
        
        # ตรวจสอบสิทธิ์การลบ
        if not (request.user.groups.filter(name='CSIT').exists() or job.company == company):
            messages.error(request, 'คุณไม่มีสิทธิ์ลบงานนี้')
            return redirect('home')
        
        if request.method == "POST":
            job.delete()
            messages.success(request, 'ลบประกาศงานเรียบร้อยแล้ว!')
            return redirect('job_list')
            
        return render(request, 'confirm_delete.html', {
            'job': job
        })

    except Exception as e:
        messages.error(request, f'เกิดข้อผิดพลาด: {str(e)}')
        return redirect('core:home')

def job_success(request):
    return render(request, 'job_success.html')