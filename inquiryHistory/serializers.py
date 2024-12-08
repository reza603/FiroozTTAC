from rest_framework import serializers
from barcode.models import ScanLogs
# from account.models import  WarehouseOrders
from companies.models import Company
from companies.serializers import   CompanySerializer



 
class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScanLogs
        fields ="__all__"
class inquiryHistorySerializer(serializers.ModelSerializer):
# Define a Meta class with model and fields attributes
   company=Company
   class Meta:
    # Set the model attribute to Barcode
     model = ScanLogs

    # Set the fields attribute to "__all__" to include all fields
     fields =  "__all__"