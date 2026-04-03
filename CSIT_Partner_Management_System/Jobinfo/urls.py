from django.urls import path, include
from . import views

app_name = 'Jobinfo'

urlpatterns = [
    path('<int:job_id>/', views.info, name='info')
]