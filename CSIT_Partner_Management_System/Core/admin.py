from django.contrib import admin
from Core.models import Company, Job, CompanyImage, JobPosition, HumanResource, HumanResourceJob, Student, StudentJob, application_forms

admin.site.register(Student)
admin.site.register(StudentJob)
admin.site.register(Company)
admin.site.register(Job)
admin.site.register(CompanyImage)
admin.site.register(JobPosition)
admin.site.register(HumanResource)
admin.site.register(HumanResourceJob)
admin.site.register(application_forms)