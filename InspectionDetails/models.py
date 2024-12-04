from django.views.generic import CreateView

from django.db import models


class inspectionDetail(models.Model):
    Inspection = models.ForeignKey('inspections.Inspection', on_delete=models.CASCADE)
    scanDateTime = models.DateTimeField(auto_now=True)
    uid = models.ForeignKey('barcode.Barcode', on_delete=models.CASCADE)
    date_created=models.DateTimeField(auto_now_add=True )
    date_modified = models.DateTimeField(auto_now=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')









    