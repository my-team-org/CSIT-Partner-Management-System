from django.contrib import admin
from .models import Company, Student

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name_th', 'email', 'phone')
    search_fields = ('name_th', 'name_en', 'email')

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'student_id', 'field_of_study', 'year')
    search_fields = ('name', 'student_id', 'email')
