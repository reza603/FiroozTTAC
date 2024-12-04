from django.urls import path
from .views import (
InspectionListView, InspectionDetailView, InspectionCreateView,
InspectionUpdateView, InspectionDeleteView
)

urlpatterns = [
path('', InspectionListView.as_view(), name='inspection-list'),
path('<int:pk>/', InspectionDetailView.as_view(), name='inspection-detail'),
path('create/', InspectionCreateView.as_view(), name='create-inspection'),
path('<int:pk>/update/', InspectionUpdateView.as_view(), name='inspection-update'),
path('<int:pk>/delete/', InspectionDeleteView.as_view(), name='inspection-delete'),
]