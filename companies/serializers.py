from rest_framework import serializers
from .models import Company

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ["national_id", "company_fa_name","phone","address", "prefix"]  
