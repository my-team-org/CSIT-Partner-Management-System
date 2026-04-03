from django.urls import path
from . import views

app_name = 'application_form'

urlpatterns = [
    path('application_form/<int:company_id>/', views.application_form, name='application_form'),
    path('form/<int:company_id>/pdf/', views.fill_and_show_pdf, name='generate_pdf'),
    path('application/history/', views.application_history, name='application_history'),
]
