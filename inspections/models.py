from django.views.generic import CreateView
from django.db import models

class Inspection(models.Model):
 task = models.CharField( max_length=50,verbose_name="عنوان ")
 user= models.ForeignKey('account.CustomUser', on_delete=models.CASCADE,verbose_name="بازرس")
 company = models.ForeignKey('companies.Company', to_field='national_id',db_column='NationalId', on_delete=models.CASCADE, verbose_name="مکان مراجعه")
 referdate = models.DateTimeField(verbose_name="تاریخ مراجعه")
 date_created=models.DateTimeField(auto_now_add=True )
 date_modified = models.DateTimeField(auto_now=True)


 class Meta:
    managed = False  