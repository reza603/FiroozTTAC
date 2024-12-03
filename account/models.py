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




from django.db import models

class WhUsers(models.Model):
  id = models.AutoField(primary_key=True)
  fname = models.CharField(max_length=255, null=True, blank=True)
  lname = models.CharField(max_length=255, null=True, blank=True)
  username = models.CharField(max_length=255, null=True, blank=True)
  password = models.CharField(max_length=255, null=True, blank=True)
  phone = models.CharField(max_length=20, null=True, blank=True)
  createdAt = models.DateTimeField(null=True, blank=True)
  updatedAt = models.DateTimeField(null=True, blank=True)
  is_active = models.BooleanField(null=True, blank=True)
  company_nid = models.CharField(max_length=12, null=True, blank=True)
  accepter_user_id = models.IntegerField(null=True, blank=True)

class Meta:
  managed = False
  db_table = 'WhUsers'

class WarehouseOrders(models.Model):
  id = models.AutoField(primary_key=True)
  OrderId = models.IntegerField(unique=True)
  GTIN = models.CharField(max_length=14, null=True, blank=True)
  BatchNumber = models.CharField(max_length=20, null=True, blank=True)
  ExpDate = models.CharField(max_length=10, null=True, blank=True)
  InsertDate = models.CharField(max_length=10, null=True, blank=True)
  LastXMLDate = models.CharField(max_length=10, null=True, blank=True)
  DistributerCompanyNid = models.CharField(max_length=11, null=True, blank=True)
  ProductionOrderId = models.CharField(max_length=20, null=True, blank=True)
  createdAt = models.DateTimeField(default=models.F('createdAt'), null=True, blank=True)
  updatedAt = models.DateTimeField(default=models.F('updatedAt'), null=True, blank=True)
  DeviceId = models.CharField(max_length=20, null=True, blank=True, default=None)
  ordertype = models.CharField(max_length=20, null=True, blank=True)
  details = models.CharField(max_length=100, null=True, blank=True)
  userId = models.IntegerField(null=True, blank=True)
  documentCode = models.CharField(max_length=20, null=True, blank=True)

  class Meta:
     managed = False
     db_table = 'WarehouseOrders'