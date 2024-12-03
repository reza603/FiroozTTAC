from django import forms
from .models import Company
class CompanyForm(forms.ModelForm):
  class Meta:
   model = Company
   fields = ["national_id", "company_fa_name","phone","address", "prefix"]  


