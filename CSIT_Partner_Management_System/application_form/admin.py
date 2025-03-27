from django.contrib import admin
from .models import Company, Student, Job, JobPosition, Jobbenefit, Company_image, HumanResouce, HumnanResource_Job, Student_job, application_forms, Review

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name_th', 'name_en', 'email', 'phone', 'company_type', 'description')
    search_fields = ('name_th', 'name_en', 'email', 'phone', 'company_type')

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'student_id', 'field_of_study', 'year', 'email', 'mobile_phone')
    search_fields = ('name', 'student_id', 'email', 'field_of_study', 'mobile_phone')

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('job_name', 'job_posted', 'job_quantity', 'job_status')
    search_fields = ('job_name__job_type', 'job_description', 'job_skill', 'job_department')

@admin.register(JobPosition)
class JobPositionAdmin(admin.ModelAdmin):
    list_display = ('job_type',)
    search_fields = ('job_type',)

@admin.register(Jobbenefit)
class JobbenefitAdmin(admin.ModelAdmin):
    list_display = ('saraly', 'lunch', 'delivery')
    search_fields = ('saraly', 'lunch', 'delivery')

@admin.register(Company_image)
class CompanyImageAdmin(admin.ModelAdmin):
    list_display = ('company', 'image')
    search_fields = ('company__name_th', 'company__name_en')

@admin.register(HumanResouce)
class HumanResouceAdmin(admin.ModelAdmin):
    list_display = ('user', 'company', 'contact_name', 'contact_position', 'contact_department', 'contact_email', 'contact_phone')
    search_fields = ('user__username', 'company__name_th', 'company__name_en', 'contact_name', 'contact_email', 'contact_phone')

@admin.register(HumnanResource_Job)
class HumnanResourceJobAdmin(admin.ModelAdmin):
    list_display = ('HumanResouce', 'Job')
    search_fields = ('HumanResouce__contact_name', 'Job__job_name__job_type')

@admin.register(Student_job)
class StudentJobAdmin(admin.ModelAdmin):
    list_display = ('student', 'job')
    search_fields = ('student__name', 'job__job_name__job_type')

@admin.register(application_forms)
class ApplicationFormsAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id', 'pdf_date', 'file')
    search_fields = ('user_id',)

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('company', 'recommend', 'overall_rating', 'benefits_rating', 'environment_rating', 'management_rating', 'created_at')
    search_fields = ('company__name_th', 'company__name_en', 'job_type', 'job_description')
