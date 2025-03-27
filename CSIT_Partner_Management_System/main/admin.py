from django.contrib import admin
from .models import Company, Job, Review, JobPosition, Jobbenefit, Company_image, HumanResouce, HumnanResource_Job, Student, Student_job

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name_th', 'name_en', 'company_type', 'phone')  
    search_fields = ('name_th', 'name_en')  
    list_filter = ('company_type',)  

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('job_name', 'job_department', 'job_quantity', 'job_status')  
    search_fields = ('job_name__job_type', 'job_department')  
    list_filter = ('job_status', 'job_department')  

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('company', 'overall_rating', 'recommend', 'created_at')  
    search_fields = ('company__name_th', 'job_type')  
    list_filter = ('recommend', 'overall_rating')  

# เพิ่ม Model อื่นๆ เข้าไปใน Django Admin
admin.site.register(JobPosition)
admin.site.register(Jobbenefit)
admin.site.register(Company_image)
admin.site.register(HumanResouce)
admin.site.register(HumnanResource_Job)
admin.site.register(Student)
admin.site.register(Student_job)
