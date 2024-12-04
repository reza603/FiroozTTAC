
from django.urls import path
from .views import (
InspectionListView, InspectionDetailView, InspectionCreateView,
InspectionUpdateView, InspectionDeleteView, InspectionListAPIView,
InspectionDetailAPIView, InspectionCreateAPIView, InspectionUpdateAPIView,
InspectionDeleteAPIView,UserInspectionListAPIView
)

urlpatterns = [
path('api/inspection/', UserInspectionListAPIView.as_view(), name='user-inspection-list'),
path('', InspectionListView.as_view(), name='inspection-list'),
path('<int:pk>/', InspectionDetailView.as_view(), name='inspection-detail'),
path('create/', InspectionCreateView.as_view(), name='create-inspection'),
path('<int:pk>/update/', InspectionUpdateView.as_view(), name='inspection-update'),
path('<int:pk>/delete/', InspectionDeleteView.as_view(), name='inspection-delete'), path('api/inspections/', InspectionListAPIView.as_view(), name='api-inspection-list'),
path('api/inspections/<int:pk>/', InspectionDetailAPIView.as_view(), name='api-inspection-detail'),
path('api/inspections/create/', InspectionCreateAPIView.as_view(), name='api-inspection-create'),
path('api/inspections/<int:pk>/update/', InspectionUpdateAPIView.as_view(), name='api-inspection-update'),
path('api/inspections/<int:pk>/delete/', InspectionDeleteAPIView.as_view(), name='api-inspection-delete'),
]

# from django.urls import path
# from .views import (
# InspectionListView, InspectionDetailView, InspectionCreateView,
# InspectionUpdateView, InspectionDeleteView
# )

# urlpatterns = [
# path('', InspectionListView.as_view(), name='inspection-list'),
# path('<int:pk>/', InspectionDetailView.as_view(), name='inspection-detail'),
# path('create/', InspectionCreateView.as_view(), name='create-inspection'),
# path('<int:pk>/update/', InspectionUpdateView.as_view(), name='inspection-update'),
# path('<int:pk>/delete/', InspectionDeleteView.as_view(), name='inspection-delete'),
# ]