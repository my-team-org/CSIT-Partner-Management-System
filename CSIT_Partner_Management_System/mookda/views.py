from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from main.models import Company
from .form import CompanyForm

# ค่าคงที่สำหรับกลุ่มผู้ใช้
HR_GROUP = 'HR'
CSIT_GROUP = 'CSIT'

def is_HR(user):
    return user.groups.filter(name=HR_GROUP).exists() or user.is_superuser

def is_CSIT(user):
    return user.groups.filter(name=CSIT_GROUP).exists() or user.is_superuser

def check_company_owner(user, company):
    return company.company_own == user

@login_required
def company_list(request):
    """แสดงรายการบริษัท"""
    if request.user.groups.filter(name=CSIT_GROUP).exists() or request.user.is_superuser:
        companies = Company.objects.all()
        is_csit = True
    else:
        companies = Company.objects.filter(company_own=request.user)
        is_csit = False
    
    return render(request, 'company_list.html', {
        'companies': companies,
        'is_csit': is_csit,
        'is_hr': request.user.groups.filter(name=HR_GROUP).exists()
    })

@login_required
def company_create(request):
    """สร้างบริษัทใหม่"""
    if request.method == "POST":
        form = CompanyForm(request.POST, request.FILES)
        if form.is_valid():
            company = form.save(commit=False)
            company.company_own = request.user
            company.save()
            
            if request.user.groups.filter(name=HR_GROUP).exists():
                return redirect('company_own')
            return redirect('company_list')
    else:
        form = CompanyForm()
    
    return render(request, 'company_form.html', {
        'form': form,
        'is_hr': request.user.groups.filter(name=HR_GROUP).exists()
    })

@login_required
def company_edit(request, company_id):
    """แก้ไขข้อมูลบริษัท"""
    company = get_object_or_404(Company, id=company_id)
    
    # ตรวจสอบสิทธิ์
    if not (is_CSIT(request.user) or check_company_owner(request.user, company)):
        return redirect('company_list')
    
    if request.method == "POST":
        form = CompanyForm(request.POST, request.FILES, instance=company)
        if form.is_valid():
            form.save()
            if request.user.groups.filter(name=HR_GROUP).exists():
                return redirect('company_own')
            return redirect('company_list')
    else:
        form = CompanyForm(instance=company)
    
    return render(request, 'company_form.html', {
        'form': form,
        'is_hr': request.user.groups.filter(name=HR_GROUP).exists()
    })

@login_required
def company_delete(request, company_id):
    """ลบบริษัท"""
    company = get_object_or_404(Company, id=company_id)
    
    # ตรวจสอบสิทธิ์
    if not (is_CSIT(request.user) or check_company_owner(request.user, company)):
        return redirect('company_list')
    
    if request.method == "POST":
        company.delete()
        return redirect('company_list')
    
    return render(request, 'company_confirm_delete.html', {
        'company': company,
        'is_hr': request.user.groups.filter(name=HR_GROUP).exists()
    })

@login_required
def company_own(request):
    """แสดงบริษัทที่ผู้ใช้เป็นเจ้าของ"""
    companies = Company.objects.filter(company_own=request.user)
    return render(request, 'company_own.html', {
        'companies': companies,
        'is_hr': request.user.groups.filter(name=HR_GROUP).exists()
    })

@user_passes_test(is_HR)
@login_required
def HR_only_view(request):
    """View สำหรับผู้ใช้กลุ่ม HR"""
    companies = Company.objects.all()
    return render(request, 'company_own.html', {
        'companies': companies
    })

@user_passes_test(is_CSIT)
@login_required
def CSIT_only_view(request):
    """View สำหรับผู้ใช้กลุ่ม CSIT"""
    companies = Company.objects.all()
    return render(request, 'company_list.html', {
        'companies': companies
    })