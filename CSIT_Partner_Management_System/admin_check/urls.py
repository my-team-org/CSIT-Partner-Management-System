from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('admin_check/<int:application_id>', views.admin_check, name='admin_check'),
]
