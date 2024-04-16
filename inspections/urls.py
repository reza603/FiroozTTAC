
from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import  InspectionCreateView,InspectionViewSet,inspectionListView,inspectionListAPIView,InspectionView

urlpatterns = [
path("Inspectioncreate/", InspectionCreateView.as_view(), name="Inspection"),
path("GetTaskAPP/", InspectionView.as_view(), name="GetTaskAPP"),
path("createinspection/",InspectionCreateView.as_view(),name='createinspection'),
path('inspectionlist/', inspectionListView.as_view(), name='inspectionlist'),
]

# Define the router here
router = DefaultRouter()
router.register("inspection", InspectionViewSet, basename="inspection")#it is ok

# Append the router.urls here
urlpatterns += router.urls
