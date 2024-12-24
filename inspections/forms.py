from django import forms
from .models import Inspection

class InspectionForm(forms.ModelForm):
  refer_date =forms.DateTimeField(widget=forms.DateInput(attrs={'type': 'date'}))
  # done = forms.BooleanField(widget=forms.CheckboxInput(), required=False)

  class Meta:
    model = Inspection
    fields = ['id','task', 'user', 'company', 'refer_date']
    exclude = ['done']