from django import forms
from .models import Product
from  companies.models import Company

class ProductForm(forms.ModelForm):
 
   class Meta:
    model = Product
    fields = ['producer_company_code', 'product_fr_name', 'gtin', 'price', 'irc']


