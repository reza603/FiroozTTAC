from django.db import models

class Barcode(models.Model):
   
    order=models.ForeignKey('order.tblOrder',on_delete=models.CASCADE)

    UUID=models.CharField(max_length=20,unique=True)
    UUIDCount=models.IntegerField(default=0)
    RndEsalat=models.CharField(max_length=140,unique=True)
    RndEsalatCount=models.IntegerField(default=0)
    parent=models.CharField(max_length=20,null=True)
    datatime_created=models.DateTimeField(auto_now_add=True)
    datatime_modified=models.DateTimeField(auto_now=True)
    levelid=models.SmallIntegerField(null=True)
    
    
    indexes = [
    models.Index(fields=['RndEsalat',]),
    models.Index(fields=['UUID',]),
]




class ScanLogs(models.Model):
    id = models.AutoField(primary_key=True)
    whOrderId = models.IntegerField(null=True, blank=True)
    whUserId = models.IntegerField(null=True, blank=True)
    uuid = models.CharField(max_length=20, null=True, blank=True)
    createdAt = models.DateTimeField(null=True, blank=True)
    updatedAt = models.DateTimeField(null=True, blank=True)

    class Meta:
        managed = False
        db_table = 'ScanLogs'
    constraints = [
    models.ForeignKey('WarehouseOrders', on_delete=models.CASCADE, db_column='whOrderId'),
    models.ForeignKey('WhUsers', on_delete=models.SET_NULL, null=True, db_column='whUserId')
    ]