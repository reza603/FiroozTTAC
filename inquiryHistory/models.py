from django.db import models

class inquiryHistory(models.Model):
    Code_Type=(
        
    ('UUID','UUID'),
    ('RND','RndEsalat'),
    )
    
    Code_Id=models.ForeignKey('barcode.Barcode',on_delete=models.CASCADE)
    #Customer_Id=models.ForeignKey('customer.Customer',on_delete=models.CASCADE)
    requestText=models.CharField(max_length=1000)
    cellphone=models.CharField(max_length=15)
    datatime_created=models.DateTimeField(auto_now_add=True)
    datatime_modified=models.DateTimeField(auto_now=True)
    status=models.CharField(Code_Type,max_length=3)
    # userid=models.ForeignKey('auth.uder',on_delete=models.CASCADE)
