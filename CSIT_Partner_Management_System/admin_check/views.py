from django.shortcuts import render
from .models import *
# Create your views here.
def index(request):
    applications = application_forms.objects.all()
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')
    student_id = request.GET.get('student_id')

    if start_date:
        applications = applications.filter(pdf_date=start_date)
    
    if end_date:
        applications = applications.filter(pdf_date=end_date)

    if student_id:
        applications = applications.filter(student_id=student_id)
        
    content = {'applications': applications}
    return render(request, 'index.html' , content)

def admin_check(request):
    applications = application_forms.objects.all()

    content = {'applications': applications}

    
    return render(request, 'Check_Application.html' , content)