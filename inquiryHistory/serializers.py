from rest_framework import serializers
from barcode.models import Barcode
 
class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Barcode
        fields = ['UUID','RndEsalat']