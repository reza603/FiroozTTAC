from django import forms
from .models import Inspection
from jalali_date.fields import JalaliDateField
from jalali_date.widgets import AdminJalaliDateWidget

class InspectionForm(forms.ModelForm):
  referdate = JalaliDateField(widget=AdminJalaliDateWidget)
  done = forms.BooleanField(widget=forms.CheckboxInput(), required=False)

  class Meta:
    model = Inspection
    fields = ['task', 'user', 'company', 'referdate', 'done']