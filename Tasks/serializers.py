from rest_framework import serializers
from .models import Task
# serializers.py
from rest_framework import serializers
from .models import Task
from account.serializers import CustomUserSerializer # import from account app
from companies.serializers import CompanySerializer # import from companies app

class TaskSerializer(serializers.ModelSerializer):
 user = CustomUserSerializer() 
 store = CompanySerializer()
 class Meta:
  model = Task
  fields = ['id', 'user', 'referraldate', 'store']

