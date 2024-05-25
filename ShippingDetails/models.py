from django.views.generic import CreateView

from django.db import models
from django.views.generic import CreateView

from django.db import models


class ShippingDetail(models.Model):
 shipping = models.ForeignKey('Shipping.Shipping', on_delete=models.CASCADE,blank=True,null=True)
 scanDateTime = models.DateTimeField()
 uid = models.CharField(max_length=20)
 date_created=models.DateTimeField(auto_now_add=True )
 date_modified = models.DateTimeField(auto_now=True)




class WarehouseOrders(models.Model):
    OrderId = models.IntegerField(primary_key=True)
    GTIN = models.CharField(max_length=14, blank=True, null=True)
    BatchNumber = models.CharField(max_length=20, blank=True, null=True)
    ExpDate = models.CharField(max_length=10, blank=True, null=True)
    InsertDate = models.CharField(max_length=10, blank=True, null=True)
    LastXMLDate = models.CharField(max_length=10, blank=True, null=True)
    DistributerCompanyNid = models.CharField(max_length=11, blank=True, null=True)
    ProductionOrderId = models.CharField(max_length=20, blank=True, null=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    DeviceId = models.CharField(max_length=20, blank=True, null=True, default=None)
    ordertype = models.CharField(max_length=20, blank=True, null=True)
    details = models.CharField(max_length=100, blank=True, null=True)
    userId = models.IntegerField(blank=True, null=True)
    documentCode = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
     db_table = 'WarehouseOrders'
class WareHouseOrderLevels(models.Model):
    OrderId = models.ForeignKey('WarehouseOrders', on_delete=models.CASCADE, db_column='OrderId', blank=True, null=True)
    LevelId = models.ForeignKey('Levels', on_delete=models.CASCADE, db_column='LevelId', blank=True, null=True)
    NumberOfOrder = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'WareHouseOrderLevels'
        constraints = [
        models.UniqueConstraint(fields=['id'], name='PK_WareHouseOrderLevels')
        ]
class WarehouseOrderProducts(models.Model):
    Orderid = models.ForeignKey('WarehouseOrders', on_delete=models.CASCADE, db_column='OrderId', blank=True, null=True)
    Gtin = models.ForeignKey('Products', on_delete=models.CASCADE, db_column='GTIN', blank=True, null=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'WarehouseOrderProducts'
        constraints = [
        models.UniqueConstraint(fields=['id'], name='PK_WhOrderProducts')
        ]


class WarehouseOrderProductLevels(models.Model):
    OrderProductid = models.ForeignKey('WarehouseOrderProducts', on_delete=models.CASCADE, db_column='OrderProductid', blank=True, null=True)
    Levelid = models.ForeignKey('Levels', on_delete=models.CASCADE, db_column='Levelid', blank=True, null=True)
    qty = models.IntegerField(blank=True, null=True)
    LimitMax = models.IntegerField(default=0)

    class Meta:
        db_table = 'WarehouseOrderProductLevels'
        constraints = [
        models.UniqueConstraint(fields=['id'], name='PK_WarehouseOrderProductLevels')
        ]
class ScanLogs(models.Model):
    whOrderId = models.ForeignKey('WarehouseOrders', on_delete=models.CASCADE, db_column='whOrderId', blank=True, null=True)
    whUserId = models.ForeignKey('WhUsers', on_delete=models.SET_NULL, db_column='whUserId', blank=True, null=True)
    uuid = models.CharField(max_length=20, blank=True, null=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    class Meta:
     db_table = 'ScanLogs'



class WhUsers(models.Model):
    fname = models.CharField(max_length=255, blank=True, null=True)
    lname = models.CharField(max_length=255, blank=True, null=True)
    username = models.CharField(max_length=255, blank=True, null=True)
    password = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    class Meta:
      db_table = 'WhUsers'
