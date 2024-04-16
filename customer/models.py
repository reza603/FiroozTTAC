from django.db import models


class Customer(models.Model):
  
    id=models.BigAutoField(primary_key=True)
    nameLast=models.CharField(max_length=20,null=True)
    cellphone=models.CharField(max_length=11)
    city=models.CharField(max_length=20,null=True)
    job=models.CharField(blank=True,max_length=20,null=True)
    datatime_created=models.DateTimeField(auto_now_add=True)
    datatime_modified=models.DateTimeField(auto_now=True)
    