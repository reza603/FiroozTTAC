from rest_framework import serializers
from barcode.models import Barcode
from products.models import Product
from companies.models import Company
from order.models import tblOrder

 
# Import the serializers module from rest_framework
from rest_framework import serializers

# Import the Barcode model from .models
from .models import Barcode
class tblorderSerializer(serializers.ModelSerializer):
  class Meta:
    model = tblOrder
    fields = "__all__"

# Define a BarcodeSerializer class that inherits from ModelSerializer
class BarcodeSerializer(serializers.ModelSerializer):
# Define a Meta class with model and fields attributes
   tblorder=tblorderSerializer()
   class Meta:
    # Set the model attribute to Barcode
     model = Barcode

    # Set the fields attribute to "__all__" to include all fields
     fields = [ 'uid']