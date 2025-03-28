from django.contrib import admin
from .models import Job , JobPosition 

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('job_id', 'job_name', 'job_department', 'job_posted','job_updated','job_description','job_updated')  # แสดงคอลัมน์หลักใน Admin
    list_filter = ('job_department', 'job_posted')  # เพิ่มตัวกรองให้ค้นหาได้ง่าย
    search_fields = ('job_name', 'job_skill', 'job_department')  # เพิ่มช่องค้นหา
    ordering = ('-job_posted',)  # เรียงจากงานล่าสุด
    readonly_fields = ('job_posted',)  # ป้องกันการแก้ไขวันที่ประกาศ
admin.site.register(JobPosition)