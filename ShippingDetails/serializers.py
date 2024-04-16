from rest_framework import serializers
from .models import ShippingDetail

class ShippingDetailSerializer(serializers.ModelSerializer):
 class Meta:
  model = ShippingDetail
#   fields = "__all__"
  fields =  ["id"]


