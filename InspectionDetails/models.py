from django.views.generic import CreateView
from django.db import models
from barcode.models import ScanLog



class inspectionDetail(models.Model):
    Inspection = models.ForeignKey('inspections.Inspection', on_delete=models.CASCADE)
    scanDateTime = models.DateTimeField(auto_now=True)
    uid = models.ForeignKey('barcode.Scanlog', on_delete=models.DO_NOTHING)
    date_created=models.DateTimeField(auto_now_add=True )
    date_modified = models.DateTimeField(auto_now=True)
    result= models.CharField(max_length = 20,null=True)
    
    # parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')



