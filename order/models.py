from email.policy import default
from typing import Any
from django.db import models
from django.core.exceptions import ValidationError
from django.utils.deconstruct  import deconstructible
from django.db import models
class Orders(models.Model):
    Id = models.BigAutoField(primary_key=True)
    OrderCode = models.CharField(max_length=20, unique=True)
    ProductCode = models.CharField(max_length=14, null=True, blank=True)
    SupplierCode = models.CharField(max_length=11, null=True, blank=True)
    PublisherCode = models.CharField(max_length=11, null=True, blank=True)
    Numberinpack = models.IntegerField(default=0, null=True, blank=True)
    NumberOfOrder = models.IntegerField(default=0, null=True, blank=True)
    PakingLevel = models.SmallIntegerField(default=0, null=True, blank=True)
    BatchNumber = models.CharField(max_length=80, null=True, blank=True)
    ProduceDate = models.CharField(max_length=10, null=True, blank=True)
    ExpDate = models.CharField(max_length=10, null=True, blank=True)
    ReleaseNumber = models.CharField(max_length=64, null=True, blank=True)
    ReleaseDate = models.CharField(max_length=10, null=True, blank=True)
    OrderDate = models.CharField(max_length=10, null=True, blank=True)
    NumberOfCoded = models.IntegerField(default=0, null=True, blank=True)
    LastCodingDate = models.CharField(max_length=20, null=True, blank=True)
    factoryPrice = models.IntegerField(null=True, blank=True)
    Price = models.IntegerField(null=True, blank=True)
    UserCode = models.CharField(max_length=50, null=True, blank=True)
    InsertDate = models.CharField(max_length=10, default=models.F('InsertDate'), null=True, blank=True)
    Done = models.SmallIntegerField(null=True, blank=True)
    FullPackcount = models.IntegerField(null=True, blank=True)
    TotalCount = models.IntegerField(null=True, blank=True)
    MiniOrigin = models.SmallIntegerField(null=True, blank=True)
    invoiceNumber = models.CharField(max_length=100, null=True, blank=True)
    TempIRC = models.CharField(max_length=50, null=True, blank=True)
    Selected = models.BooleanField(null=True, blank=True)
    Accepted = models.BooleanField(null=True, blank=True)
    NumberOfPrinted = models.IntegerField(default=0, null=True, blank=True)
    Userid = models.IntegerField(null=True, blank=True)
    XmlStatus = models.BooleanField(default=False, null=True, blank=True)
    archiveprefix = models.CharField(max_length=3, null=True, blank=True)
    version = models.CharField(max_length=50, null=True, blank=True)
    prefix = models.CharField(max_length=5, null=True, blank=True)

    class Meta:
        managed = False
        db_table = 'Orders'
constraints = [
models.ForeignKey('Products', on_delete=models.CASCADE, db_column='ProductCode')
]

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
 
   
    
    


