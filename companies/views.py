from django.views.generic import CreateView, ListView
from .models import Company 
from .forms import CompanyForm
from rest_framework import viewsets
from .serializers import  CompanySerializer
from rest_framework import generics
from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
import json
import datetime
from account.models import CustomUser


class CompanyCreateView(CreateView):
    model = Company
    form_class = CompanyForm
    template_name = "companies/company_form.html"
    success_url = "/companies/companylist" # change this to your desired url

class CompanyListView(ListView):
    model = Company
    template_name = "companies/company_list.html"
    
class CompanyAPIView(generics.ListAPIView):
  queryset = Company.objects.all()
  serializer_class = CompanySerializer
  


# def company_list(request):
#     companies = Company.objects.all()
#     return render(request, 'company_list.html', {'companies': companies})

