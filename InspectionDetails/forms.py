from django import forms
from .models import inspectionDetail
class inspectionDetailForm(forms.ModelForm):
  class Meta:
   model = inspectionDetail
   fields = "__all__"

