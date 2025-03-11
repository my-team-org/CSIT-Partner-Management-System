from django.shortcuts import render, redirect
from .models import Student, Company
from .forms import StudentForm, CompanyForm  # แก้ไขตรงนี้

def application_form(request):
    if request.method == "POST":
        student_form = StudentForm(request.POST, request.FILES)
        company_form = CompanyForm(request.POST)

        if student_form.is_valid() and company_form.is_valid():
            company = company_form.save()  # บันทึก Company ก่อน
            student = student_form.save(commit=False)
            student.company = company  # เชื่อม Student กับ Company ถ้ามี ForeignKey
            student.save()
            return redirect('success_page')  # เปลี่ยนไปยังหน้าสำเร็จ
    else:
        student_form = StudentForm()
        company_form = CompanyForm()

    context = {
        'student_form': student_form,
        'company_form': company_form
    }
    return render(request, 'application_form.html', context)
