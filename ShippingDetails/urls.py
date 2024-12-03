from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import ShippingDetailViewSet
from .views import ShippingDetailCreateView
urlpatterns = [
path("shippingdetail/create/", ShippingDetailCreateView.as_view(), name="shipping_detail_create"),
]
router = DefaultRouter()
router.register("shippingdetails", ShippingDetailViewSet)
urlpatterns += router.urls




