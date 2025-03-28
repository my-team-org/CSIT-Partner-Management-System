from django.shortcuts import render, redirect, get_object_or_404
from .models import Job
from .forms import JobForm
from django.utils.timezone import now



def add_job(request):
    if request.method == "POST":
        form = JobForm(request.POST, request.FILES)  # เพิ่ม request.FILES
        if form.is_valid():
            form.save()
            return redirect('job_list')  # ใช้ชื่อ URL pattern
        else:
            print(form.errors)  # พิมพ์ข้อผิดพลาดของฟอร์ม
    else:
        form = JobForm()
    return render(request, 'add_job.html', {'form': form})

def job_success(request):
    return render(request, 'job_success.html')

def edit_add_job(request, job_id):
    job = get_object_or_404(Job, pk=job_id)  # ดึงข้อมูลงานที่ต้องการแก้ไข
    if request.method == "POST":
        form = JobForm(request.POST, request.FILES, instance=job)
        if form.is_valid():

            job = form.save()  # ยังไม่บันทึกลงฐานข้อมูล
            return redirect('job_list')  # เปลี่ยนเส้นทางหลังจากบันทึกสำเร็จ
    else:
        form = JobForm(instance=job)  # โหลดข้อมูลเดิมในฟอร์ม

    return render(request, 'edit_add_job.html', {'form': form}) 

from django.shortcuts import render, get_object_or_404, redirect
from .models import Job

def job_list(request):
    jobs = Job.objects.all()  # ดึงข้อมูลทั้งหมดจากฐานข้อมูล
    return render(request, 'job_list.html', {'jobs': jobs})  # ส่งไปที่เทมเพลต

def delete_job(request, job_id):
    job = get_object_or_404(Job, pk=job_id)
    job.delete()
    return redirect('job_list')  # รีเฟรชหน้า job_list หลังลบเสร็จ
