from django.views.generic import CreateView

from django.db import models


class ShippingDetail(models.Model):
 shipping = models.ForeignKey('Shipping.Shipping', on_delete=models.CASCADE,blank=True,null=True)
 scanDateTime = models.DateTimeField()
 uid = models.CharField(max_length=20)
 date_created=models.DateTimeField(auto_now_add=True )
 date_modified = models.DateTimeField(auto_now=True)



