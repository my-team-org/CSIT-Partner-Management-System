from django.contrib import admin
from django import forms
from .models import (
    Company, Review, Company_image, HumanResouce, HumnanResource_Job,
    Job, JobPosition, Jobbenefit, Student, Student_job, application_forms
)

# ✅ ฟอร์ม custom เฉพาะสำหรับหน้า Admin ของ Review
class ReviewAdminForm(forms.ModelForm):
    RECOMMEND_CHOICES = [
        (True, 'recommend'),
        (False, 'not recommend'),
    ]

    recommend = forms.ChoiceField(
        choices=RECOMMEND_CHOICES,
        widget=forms.RadioSelect,
        required=True,
        label="Recommend"
    )

    class Meta:
        model = Review
        fields = '__all__'

# ✅ ใช้ custom form ในหน้า Admin ของ Review
@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    form = ReviewAdminForm

# ✅ Register models อื่น ๆ แบบปกติ
@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    pass

@admin.register(Company_image)
class CompanyImageAdmin(admin.ModelAdmin):
    pass

@admin.register(HumanResouce)
class HumanResouceAdmin(admin.ModelAdmin):
    pass

@admin.register(HumnanResource_Job)
class HumnanResourceJobAdmin(admin.ModelAdmin):
    pass

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    pass

@admin.register(JobPosition)
class JobPositionAdmin(admin.ModelAdmin):
    pass

@admin.register(Jobbenefit)
class JobbenefitAdmin(admin.ModelAdmin):
    pass

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    pass

@admin.register(Student_job)
class StudentJobAdmin(admin.ModelAdmin):
    pass

@admin.register(application_forms)
class ApplicationFormsAdmin(admin.ModelAdmin):
    pass
