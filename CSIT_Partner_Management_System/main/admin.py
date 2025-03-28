from django.contrib import admin
from .models import Company


class CompanyAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(company_own=request.user)  # แสดงเฉพาะบริษัทที่ผู้ใช้เป็นเจ้าของ

admin.site.register(Company, CompanyAdmin)

