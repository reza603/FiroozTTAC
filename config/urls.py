from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

# Initialize the router
router = DefaultRouter()
# Register viewsets if any, e.g., router.register(r'users', UserViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    # Including app-specific URL configurations
    path('account/', include('account.urls')),
    path('inquiry/', include('inquiryHistory.urls')),
    path('products/', include('products.urls')),
    path('companies/', include('companies.urls')),
    path('inspections/', include('inspections.urls')),
    path('account/', include('django.contrib.auth.urls')),
    path('', include('order.urls')),

    # Adding the router URLs
    path('', include(router.urls)),

    # API token authentication
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
























# from django.conf import settings
# from django.conf.urls.static import static
# from django.contrib import admin
# from django.urls import path,include
# from rest_framework.authtoken.views import ObtainAuthToken
# from django.views.generic.base  import TemplateView
# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from rest_framework import views

# """config URL Configuration

# The `urlpatterns` list routes URLs to views. For more information please see:
#     https://docs.djangoproject.com/en/4.0/topics/http/urls/
# Examples:
# Function views
#     1. Add an import:  from my_app import views
#     2. Add a URL to urlpatterns:  path('', views.home, name='home')
# Class-based views
#     1. Add an import:  from other_app.views import Home
#     2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
# Including another URLconf
#     1. Import the include() function: from django.urls import include, path
#     2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
# """

# urlpatterns = [
#     path('admin/', admin.site.urls),


#     path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
   
#      path('account/',include('account.urls')),
#      path('inquiry/',include('inquiryHistory.urls')),
#      path('products/',include('products.urls')),
#      path('companies/',include('companies.urls')),
#     #  path('tasks/',include('Tasks.urls')),
#      path('inspections/',include('inspections.urls')),

#     #  path('shipping/',include('Shipping.urls')),
#     #  path('order/',include('order.urls')),
#      path('account/',include('django.contrib.auth.urls')), 

#      path ('',include('order.urls')),

# ]
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# from rest_framework.authtoken import views
# urlpatterns += [
#     path('api-token-auth/', views.obtain_auth_token)
# ]