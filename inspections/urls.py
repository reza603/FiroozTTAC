
from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import  InspectionCreateView,InspectionViewSet,inspectionListView,inspectionListAPIView,InspectionView

urlpatterns = [
path("Inspectioncreate/", InspectionCreateView.as_view(), name="create-inspection"),
path("GetTaskAPP/", InspectionView.as_view(), name="GetTaskAPP"),
path('inspectionlist/', inspectionListView.as_view(), name='inspection-list'),
]

router = DefaultRouter()
router.register("inspection", InspectionViewSet, basename="inspection")#it is ok
urlpatterns += router.urls
