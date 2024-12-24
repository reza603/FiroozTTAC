from django import forms
from .models import Inspection
from jalali_date.fields import JalaliDateField
from jalali_date.widgets import AdminJalaliDateWidget

class InspectionForm(forms.ModelForm):
    refer_date = JalaliDateField(widget=AdminJalaliDateWidget)
    done = forms.BooleanField(widget=forms.CheckboxInput(), required=False)

    class Meta:
        model = Inspection
        fields = ['id','task', 'user', 'company', 'refer_date', 'done']




# class InspectionForm(forms.ModelForm):
#   refer_date = JalaliDateField(widget=AdminJalaliDateWidget)
#   done = forms.BooleanField(widget=forms.CheckboxInput(), required=False)

#   class Meta:
#     model = Inspection
#     fields = ['task', 'user', 'company', 'refer_date']

  
      
#     def __init__(self, *args, **kwargs):
#       super().__init__(*args, **kwargs)