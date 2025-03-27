from django.urls import path 
from .views import company_list

urlpatterns = [
    path('',company_list, name='company_list'),
]