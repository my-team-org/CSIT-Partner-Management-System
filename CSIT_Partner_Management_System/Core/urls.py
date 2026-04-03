from django.urls import path
from .views import *

app_name = 'core'

urlpatterns = [
    path('', index, name='home'),
    path('company/', company_list, name='company_list'),
    path('edit/', edit_student, name='edit_student'),
]
