from django.urls import path

from rest_framework.routers import DefaultRouter
from .views import ShippingCreateView
from .views import ShippingViewSet

urlpatterns = [
path("shipping/create/", ShippingCreateView.as_view(), name="shipping_detail_create"),
]

router = DefaultRouter()
router.register("Shipping", ShippingViewSet)

urlpatterns += router.urls