from django.shortcuts import render,redirect
from .forms import ProductForm
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Product
from .serializers import ProductSerializer
from django.views.generic import CreateView, ListView
class ProductCreateView(CreateView):
    model = Product
    form_class =ProductForm
    template_name = "products/product_form.html"
    success_url = "/products/productslist" # change this to your desired url

class ProductListView(ListView):
    model = Product
    template_name = "products/product_list.html"
    
class ProductAPIView(generics.ListAPIView):
  queryset = Product.objects.all()
  serializer_class = ProductSerializer

  
  
  