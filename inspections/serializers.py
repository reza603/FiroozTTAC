from rest_framework import serializers
from .models import Inspection
from account.models import CustomUser
from companies.models import  Company
# class UserSerializer(serializers.ModelSerializer):
#   class Meta:
#     model = CustomUser
#     fields = ['id', 'fname', 'lname', 'mobile', 'username', 'password']

# class CompanySerializer(serializers.ModelSerializer):
#   class Meta:
#     model = Company
#     fields = [ 'name', 'nid', 'address', 'tel', 'address']
class InspectionSerializer(serializers.ModelSerializer):
  # user = UserSerializer() # use the nested serializer for the user field
  # company = CompanySerializer() # use the nested serializer for the company field
  class Meta:
    model = Inspection
    #fields = "__all__"
    fields = ['id', 'user', 'company', 'task','referdate']

