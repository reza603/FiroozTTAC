from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
 class Meta:
  model = Product
  fields =  ['producer_company_code', 'product_fr_name', 'gtin', 'price', 'info1', 'info2', 'irc']