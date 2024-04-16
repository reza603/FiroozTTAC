from django import forms
from order.models import tblOrder,Document

class InqueryForm(forms.ModelForm):

    class Meta:
        model = Document
        fields = ('File_addr',)


