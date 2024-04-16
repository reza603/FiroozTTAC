from email.policy import default
from typing import Any
from django.db import models
from django.core.exceptions import ValidationError
from django.utils.deconstruct  import deconstructible


# class XmlValidator:
#     def __call__(self, value):
#         ext=value.name.split('.')[-1].lower()
#         if ext != 'xml':
#             raise ValidationError('Only XML files are allowed.')

# validate_xml = XmlValidator()

class Document(models.Model):
  
    File_addr = models.FileField(upload_to='XmlFiles/%Y/%m/%d/',verbose_name='انتخاب فایل')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
    
    
class tblXmlOrders (models.Model):
    STATUS_CHOICES=(
     ('en','قابل استعلام'),
     ('dis','غیرقابل استعلام'),
     )
    document = models.ForeignKey('order.Document',on_delete=models.CASCADE,null=True)
    User=models.ForeignKey('account.CustomUser',on_delete=models.CASCADE,null=True)
    oc=models.CharField(max_length=11)
    dc=models.ForeignKey('companies.company',on_delete=models.CASCADE,null=True)
    lc=models.CharField(max_length=11)
    no=models.PositiveIntegerField()
    px=models.PositiveIntegerField()
    date_created=models.DateTimeField(auto_now_add=True )
    date_modified = models.DateTimeField(auto_now=True)
    status=models.CharField(max_length=3,default='dis')
    indexes = [
    models.Index(fields=[' id',]),
  
    ]
    def __str__(self):
         return str(self. id)

class tblOrder (models.Model):
    STATUS_CHOICES=(
     ('en','قابل استعلام'),
     ('dis','غیرقابل استعلام'),
     )

    invoicenumber=models.ForeignKey('order.tblXmlOrders',on_delete=models.CASCADE)
    
    GTIN=models.ForeignKey('products.Product',on_delete=models.CASCADE)
    bn=models.CharField(max_length=14)
    md=models.CharField(max_length=10)
    ed=models.CharField(max_length=10)
    no=models.PositiveIntegerField()
   
    date_created=models.DateTimeField(auto_now_add=True )
    date_modified = models.DateTimeField(auto_now=True)
    status=models.CharField(STATUS_CHOICES,max_length=3,default='dis')
#     indexes = [
#     models.Index(fields=[' id',]),
   
# ]
 
   
    
    


