from rest_framework import serializers
from barcode.models import ScanLog
from account.models import  WarehouseOrder
from companies.models import Company
from companies.serializers import   CompanySerializer 
from inspections.serializers import InspectionSerializer
from .models import inquiryHistory
class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScanLog
        fields ="__all__"
class inquiryHistorySerializer(serializers.ModelSerializer):
# Define a Meta class with model and fields attributes
    class Meta:
        model = inquiryHistory
        fields =  "__all__"       
class inquiryHistorySerializer(serializers.ModelSerializer):
# Define a Meta class with model and fields attributes
    class Meta:
        model = inquiryHistory
        fields =  "__all__"