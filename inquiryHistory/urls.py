
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('rndesalat/', views.RndEsalatInquiry, name='RndEsalatInquiry'),
    path('uuid/', views.uuidInquiry, name='uuidInquiry'),
    path('inspectionuuid/', views.uidinspection, name='uidinspection'),
    path('showform/', views.show_inquiry_form, name='showinquiryform'),
    path('getsms/', views.getSMS),
    path('sensms/', views.sendSMS),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# from django.conf import settings
# from django.conf.urls.static import static
# from unicodedata import name
# from django.urls import path
# from . import views

# urlpatterns = [
#     path('rndesalat/', views.RndEsalatInquiry,name='RndEsalatInquiry'),
#     path('uuid/', views.uuidInquiry,name='uuidInquiry'),
#     path('inspectionuuid/', views.uidinspection,name='uidinspection'),#ok
#     path('showform/', views.show_inquiry_form,name='showinquiryform'),
#     path ('getsms/', views.getSMS),
#     path('sensms/', views.sendSMS),
# ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
