from rest_framework import serializers
from barcode.models import Barcode
from products.models import Product
from companies.models import Company
from companies.serializers   import CompanySerializer
from account.serializers   import CustomUserSerializer
from products.serializers import ProductSerializer

from order.models import tblOrder

 
# Import the serializers module from rest_framework
from rest_framework import serializers

# Import the Barcode model from .models
from .models import Barcode
class CompanySerializer(serializers.ModelSerializer):
  class Meta:
    model = tblOrder
    fields = "__all__"

# Define a BarcodeSerializer class that inherits from ModelSerializer
class BarcodeSerializer(serializers.ModelSerializer):
# Define a Meta class with model and fields attributes
   company=CompanySerializer
   class Meta:
    # Set the model attribute to Barcode
     model = Company

    # Set the fields attribute to "__all__" to include all fields
     fields =  "__all__"