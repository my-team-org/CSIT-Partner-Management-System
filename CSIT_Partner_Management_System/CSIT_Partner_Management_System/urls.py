from django.contrib import admin
from django.urls import path, include 
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views # เพิ่มการตั้งค่าการเข้าสู่ระบบและออกจากระบบ

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),  # สร้างหน้าแรก
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/login/'), name='logout'),
    path('companies/', include('mookda.urls')),  # เชื่อมโยงกับ urls.py ของแอป mookda
]
# เพิ่มการตั้งค่า static สำหรับ media
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)