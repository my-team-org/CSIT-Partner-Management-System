from django.urls import path
from application_form import views

urlpatterns = [
    path('', views.application_form, name='application_form'),
    path('company<int:company_id>/', views.application_form, name='application_form_with_company'),
    path('show_pdf/', views.fill_and_show_pdf, name='show_pdf'),
    path('success/', views.success_page, name='success_page'),
]
