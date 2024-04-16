from django.views.generic import CreateView, ListView
from .models import Company 
from .forms import CompanyForm
from rest_framework import viewsets
from .serializers import  CompanySerializer
from rest_framework import generics
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
  
  
  

