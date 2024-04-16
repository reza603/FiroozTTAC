from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
       Access_Level=(
       ('admin','مدیر'),
       ('user','کاربر'),
        ('ins','بازرس'),
      )
       AccessLevel=models.CharField(choices=Access_Level,max_length=5,null=True,blank=True,verbose_name="سطح دسترسی")
       fname=models.CharField(max_length=20,blank=True,verbose_name="نام کاربر")
       lname=models.CharField(max_length=20,blank=True,verbose_name="نام خانوادگی")
       mobile=models.CharField(max_length=11,blank=True,verbose_name="تلفن")
       address=models.CharField(max_length=500,blank=True,verbose_name="آدرس")
   
       def __str__(self):
         return str(self.fname)
