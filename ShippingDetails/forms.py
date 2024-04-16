from django import forms
from .models import ShippingDetail
class shippingDetailsForm(forms.ModelForm):
  class Meta:
   model = ShippingDetail
   fields = "__all__"


