from django.urls import path 
from .views import company_list, company_create, company_edit, company_delete , company_own, HR_only_view, CSIT_only_view

urlpatterns = [
    path('companies/', company_list, name='company_list'), # เชื่อมโยงกับ urls.py ของแอป main และเรียกใช้ฟังก์ชัน company_list 
    path('companies/add/', company_create, name='company_create'), # เชื่อมโยงกับ urls.py ของแอป main และเรียกใช้ฟังก์ชัน company_create
    path('companies/edit/<int:company_id>/', company_edit, name='company_edit'), # เชื่อมโยงกับ urls.py ของแอป main และเรียกใช้ฟังก์ชัน company_edit
    path('companies/delete/<int:company_id>/', company_delete, name='company_delete'), # เชื่อมโยงกับ urls.py ของแอป main และเรียกใช้ฟังก์ชัน company_delete
    path('companies/own/', company_own, name='company_own'), 
    path('hr-dashboard/', HR_only_view, name='hr_dashboard'),
    path('csit-dashboard/', CSIT_only_view, name='csit_dashboard'),
]
