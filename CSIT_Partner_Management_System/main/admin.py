from django.contrib import admin
from .models import Partner
# Register your models here.
@admin.register(Partner)
class Partner(admin.ModelAdmin):
    list_display = ('partner_id', 'username_pn', 'password_pn', 'email_pn','image_pn','name_en','name_th','contact_number','address','district','province','postal_code','description_pn')
