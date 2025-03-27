from django.shortcuts import render, redirect
from .models import *
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from .forms import ApplicationForm
# Create your views here.
def index(request):
    applications = application_forms.objects.filter(status='pending')
    start_date = request.GET.get('start_date' , None)
    end_date = request.GET.get('end_date', None)
    student_id = request.GET.get('student_id', None)
    if start_date:
        applications = applications.filter(pdf_date__gte=start_date)  # กรองวันที่เริ่มต้น
    if end_date:
        applications = applications.filter(pdf_date__lte=end_date)  # กรองวันที่สิ้นสุด
    if student_id:
        applications = applications.filter(student__student_id__icontains=student_id)
    content = {'applications': applications}
    return render(request, 'index.html' , content)

def admin_check(request , application_id):
    application_instance = get_object_or_404(application_forms , pk=application_id)
    if request.method == 'POST':
        reason = request.POST.get('reason', '')
        action = request.POST.get('status_action', '')
        # Update the application instance with new comment and status
        if action == 'approve':
            application_instance.comment = reason
            application_instance.status = 'approved'
        elif action == 'reject':
            application_instance.comment = reason
            application_instance.status = 'rejected'
        # Save the updated application instance
        application_instance.save()
        return redirect('index')
    else:
        form = ApplicationForm(instance=application_instance)

    return render(request, 'Checkapp.html' , {'form': form , 'application_instance': application_instance}) 


