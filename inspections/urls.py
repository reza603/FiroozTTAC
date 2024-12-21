from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import (
InspectionCreateView,
InspectionViewSet,
inspectionListView,
inspectionListAPIView,
InspectionView,
mark_task_done
)

urlpatterns = [
path("Inspectioncreate/", InspectionCreateView.as_view(), name="create-inspection"),
path("GetTaskAPP/", InspectionView.as_view(), name="GetTaskAPP"),
path("inspectionlist/", inspectionListView.as_view(), name="inspectionlist"),
path("mark-task-done/", mark_task_done, name="mark-task-done"),
]

router = DefaultRouter()
router.register("inspection", InspectionViewSet, basename="inspection")
urlpatterns += router.urls
