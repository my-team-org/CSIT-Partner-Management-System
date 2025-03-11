from django.urls import path
from application_form import views

urlpatterns = [
    path('', views.application_form, name='application_form'),
]
