from django import forms
from .models import Inspection

class InspectionForm(forms.ModelForm):
  referdate = forms.DateTimeField(widget=forms.DateInput(attrs={'type': 'date'}))
  done = forms.BooleanField(widget=forms.CheckboxInput(), required=False)

  class Meta:
   model = Inspection
   fields = ['task', 'user', 'company', 'referdate']
