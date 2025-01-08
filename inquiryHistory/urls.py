from unicodedata import name
from django.urls import path
from . import  views
from django.urls import  path
from .views import InspectionUUIDAPIView 
urlpatterns = [
    path('inspectionuuid/', InspectionUUIDAPIView.as_view(), name='inspection_uuid'),
    path('rndesalat/', views.RndEsalatInquiry, name='RndEsalatInquiry'),
    path('uuid/', views.uuidInquiry, name='uuidInquiry'),
    # path('inspectionuuid/', views.uidinspection, name='uidinspection'),
    path('showform/', views.show_inquiry_form, name='showinquiryform'),
    path('getsms/', views.getSMS),
    path('sensms/', views.sendSMS),
] 

