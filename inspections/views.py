from django.views.generic.list import ListView
from .models import Inspection

class InspectionListView(ListView):
    model = Inspection
    template_name = 'inspections/inspection_list.html'
    context_object_name = 'inspections'
    paginate_by = 10


from django.views.generic.detail import DetailView
from .models import Inspection

class InspectionDetailView(DetailView):
    model = Inspection
    template_name = 'inspections/inspection_detail.html'
    context_object_name = 'inspection'

from django.views.generic.edit import CreateView
from .models import Inspection
from .forms import InspectionForm

class InspectionCreateView(CreateView):
    model = Inspection
    form_class = InspectionForm
    template_name = 'inspections/inspection_form.html'
    success_url = '/inspections/'

from django.views.generic.edit import UpdateView
from .models import Inspection
from .forms import InspectionForm

class InspectionUpdateView(UpdateView):
    model = Inspection
    form_class = InspectionForm
    template_name = 'inspections/inspection_form.html'
    success_url = '/inspections/'


from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from .models import Inspection

class InspectionDeleteView(DeleteView):
    model = Inspection
    template_name = 'inspections/inspection_confirm_delete.html'
    success_url = reverse_lazy('inspections')


from rest_framework.generics import ListAPIView
from .models import Inspection
from .serializers import InspectionSerializer

class InspectionListAPIView(ListAPIView):
    queryset = Inspection.objects.all()
    serializer_class = InspectionSerializer



from rest_framework.generics import RetrieveAPIView
from .models import Inspection
from .serializers import InspectionSerializer

class InspectionDetailAPIView(RetrieveAPIView):
    queryset = Inspection.objects.all()
    serializer_class = InspectionSerializer



from rest_framework.generics import CreateAPIView
from .models import Inspection
from .serializers import InspectionSerializer

class InspectionCreateAPIView(CreateAPIView):
    queryset = Inspection.objects.all()
    serializer_class = InspectionSerializer



from rest_framework.generics import UpdateAPIView
from .models import Inspection
from .serializers import InspectionSerializer

class InspectionUpdateAPIView(UpdateAPIView):
    queryset = Inspection.objects.all()
    serializer_class = InspectionSerializer

from rest_framework.generics import DestroyAPIView
from .models import Inspection
from .serializers import InspectionSerializer

class InspectionDeleteAPIView(DestroyAPIView):
    queryset = Inspection.objects.all()
    serializer_class = InspectionSerializer

from django import forms
from .models import Inspection

class InspectionForm(forms.ModelForm):
    class Meta:
        model = Inspection
        fields = ['task', 'user', 'company', 'referdate']

from rest_framework import serializers
from .models import Inspection
from account.models import CustomUser
from companies.models import Company

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'fname', 'lname', 'mobile', 'username', 'password']

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
     model = Company
     fields = ["company", "company_fa_name", "phone", "address", "prefix"]

class InspectionSerializer(serializers.ModelSerializer):
    user = UserSerializer()  # Nested serializer for the user field
    company = CompanySerializer()  # Nested serializer for the company field

    class Meta:
     model = Inspection
    fields = "__all__"