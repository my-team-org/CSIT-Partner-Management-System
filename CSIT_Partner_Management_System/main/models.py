from django.db import models

# Create your models here.
  
class Partner(models.Model):
    partner_id = models.AutoField(primary_key=True)  
    username_pn = models.CharField(max_length=255, unique=True)  
    password_pn = models.CharField(max_length=255) 
    email_pn = models.EmailField(unique=True)  
    image_pn = models.ImageField(upload_to='static/images/', null=True, blank=True)  
    name_en = models.CharField(max_length=255)  
    name_th = models.CharField(max_length=255) 
    contact_number = models.CharField(max_length=20) 
    address = models.CharField(max_length=255)
    district = models.CharField(max_length=255)
    province = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=255)
    description_pn = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return self.name_en