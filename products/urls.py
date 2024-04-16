from django.urls import path
from .views import ProductAPIView,ProductCreateView,ProductListView

urlpatterns = [
path("productslist/", ProductListView.as_view(),name='productslist'),
path("createproduct/",ProductCreateView.as_view(),name='createproduct'),
]
urlpatterns += [
path('productsapilist/', ProductAPIView.as_view(), name='productsapilist'),
]