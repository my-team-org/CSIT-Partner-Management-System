from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('Accounts.urls')),
    path('', include('Core.urls')),
    path('jobinfo/', include('Jobinfo.urls')),
    path('companydetail/', include('CompanyDetail.urls')),
    path('application_form/', include('Application_form.urls')),
    path('admincheck/', include('Admin_check.urls')),
    path('role/', include('Role.urls')),
    path('company/', include('Company.urls')),
    path('review/', include('Review.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)