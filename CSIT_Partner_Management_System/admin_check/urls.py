from django.urls import path
from . import views

app_name = 'Admin_check'

urlpatterns = [
    path('', views.index, name='index'),
    path('admin_check/<int:application_id>', views.admin_check, name='admin_check'),
]
