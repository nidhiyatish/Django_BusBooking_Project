from django.db import models

# Create your models here.
from django.contrib.auth.models import User 


class DriverProfile(models.Model):
    user= models.OneToOneField(User,on_delete=models.CASCADE,related_name="driver_profile")
    name = models.CharField(max_length=100)
    phone_no = models.CharField(max_length=15, unique=True)
    image = models.ImageField(upload_to="driver/images/")
    
    
    def __str__(self):
        return f"{self.name} ({self.phone_no})"
