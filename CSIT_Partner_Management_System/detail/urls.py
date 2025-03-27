from django.urls import path, include
from . import views
from jobinfo.views import info

urlpatterns = [
    path('',views.detail, name='detail'),
    path('job/<int:job_id>/', info, name='job_info'), # เพิ่ม path สำหรับ job info
]