from django import forms
from .models import Product
from  companies.models import Company

class ProductForm(forms.ModelForm):
 
  OC = forms.ModelChoiceField(queryset=Company.objects.all(), label='شرکت تولید کننده')

  class Meta:
   model = Product
   fields = ['OC', 'name', 'gtin', 'price', 'description', 'image', 'irc']



