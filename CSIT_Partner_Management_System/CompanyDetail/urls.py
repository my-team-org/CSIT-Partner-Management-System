from django.urls import path, include
from . import views
from Jobinfo.views import info

app_name = 'CompanyDetail'

urlpatterns = [
    path('<int:company_id>',views.detail, name='detail'),
    path('job/<int:job_id>/', info, name='job_info'), # เพิ่ม path สำหรับ job info
]