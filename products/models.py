from django.db import models


class Product(models.Model):
  

    OC=models.ForeignKey("companies.company",on_delete=models.CASCADE,verbose_name='شرکت تولید کننده')
    name=models.CharField(max_length=100,verbose_name='نام محصول')
    gtin=models.CharField(primary_key=True,max_length=14,verbose_name='کد جهانی تجاری')
    price = models.DecimalField(max_digits=10, decimal_places=2,null=True,verbose_name='قیمت')
    description = models.CharField(max_length=100,verbose_name='توضیحات')
    image = models.ImageField(upload_to="products/",null=True,verbose_name='عکس')
    irc =models.CharField(max_length=16,null=True,verbose_name='پروانه بهداشتی')
    datatime_created=models.DateTimeField(auto_now_add=True)
    datatime_modified=models.DateTimeField(auto_now=True)
    


    