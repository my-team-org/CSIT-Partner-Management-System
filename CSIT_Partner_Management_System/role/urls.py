from django.urls import path
from .views import add_job, job_success, edit_add_job, job_list, delete_job

urlpatterns = [
    path('add/', add_job, name='add_job'),
    path('success/', job_success, name='job_success'),
    path('edit/<int:job_id>/', edit_add_job, name='edit_add_job'),
    path('jobs/', job_list, name='job_list'),
    path('delete/<int:job_id>/', delete_job, name='delete_job'),

]
