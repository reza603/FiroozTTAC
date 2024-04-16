from django.urls import path
from .views import inspectiondetail_createAPI
from rest_framework.routers import DefaultRouter

from django.urls import path
from .views import inspectiondetail_createAPI,inspection_detail_create_api
# urlpatterns = [
# path('inspectiondetailsAPIScanUid/', inspectiondetail_createAPI, name='inspectiondetail_createAPI'),
# ]
# Define the router here

urlpatterns = [
path('scan/', inspectiondetail_createAPI, name='inspectiondetail_createAPI'),
# path('inspectiondetails/track/', inspectiondetail_trackAPI, name='inspectiondetail_trackAPI'),
]
# router = DefaultRouter()
# router.register("inspectiondetail", inspectiondetailsViewSet, basename="inspectiondetails")#it is ok

# # Append the router.urls here
# urlpatterns += router.urls
# urlpatterns += [
# path('inspectiondetailslist/', inspectionDetailsCreateView.as_view(), name='inspectiondetailslist'),
# ]


 
#  http://localhost:8000/inspectiondetails/inspectiondetails/track/?uid=
