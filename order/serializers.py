from rest_framework import serializers
from .models import Inspection
from account.models import CustomUser
from companies.models import  Company
from products.models import  Product
from .models import  tblOrder,tblXmlOrders,Orders

class CompanySerializer(serializers.ModelSerializer):
  class Meta:
    model = Company
    fields = "__all__"
class productsSerializer(serializers.ModelSerializer):
  class Meta:
    model = Product
    fields = "__all__"
class tblxmlorderSerializer(serializers.ModelSerializer):
  dc=CompanySerializer()
  class Meta:
    model = tblXmlOrders
    fields = "__all__"
class tblorderSerializer(serializers.ModelSerializer):
  document=tblxmlorderSerializer()
  class Meta:
    model = tblOrder
    fields = "__all__"
class OrderSerializer(serializers.ModelSerializer):

  class Meta:
    model = Orders
    fields = "__all__"





