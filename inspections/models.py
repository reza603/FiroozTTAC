from django.db import models # type: ignore
from companies.models import Company
class Inspection(models.Model):
  task = models.CharField(max_length=50, verbose_name="عنوان")
  user = models.ForeignKey('account.CustomUser', on_delete=models.CASCADE, verbose_name="بازرس")
  company = models.ForeignKey('companies.Company', to_field='national_id', db_column='company_id', on_delete=models.CASCADE, verbose_name="مکان مراجعه")
  referdate = models.DateTimeField(verbose_name="تاریخ مراجعه")
  done = models.BooleanField(default=False, verbose_name="status")
  date_created = models.DateTimeField(auto_now_add=True)
  date_modified = models.DateTimeField(auto_now=True)

  class Meta:
   managed = True
   db_table = 'inspections_inspection'
   
   
   
   # from django.db import models
# from companies.models import Company
# class Inspection(models.Model):
#    task = models.CharField(max_length=50, verbose_name="عنوان")
#    user = models.ForeignKey('account.CustomUser', on_delete=models.CASCADE, verbose_name="بازرس")
#    company = models.ForeignKey('companies.Company', to_field='national_id', db_column='company_id', on_delete=models.CASCADE, verbose_name="مکان مراجعه")
#    referdate = models.DateTimeField(verbose_name="تاریخ مراجعه")
#    date_created = models.DateTimeField(auto_now_add=True)
#    date_modified = models.DateTimeField(auto_now=True)
#    class Meta:
#      managed = False
#      db_table = 'inspections_inspection'