
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include
#from django.views.generic.base  import TemplateView
"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""






urlpatterns = [
     path('admin/', admin.site.urls),
    #  path('order/',include('order.urls')),
     path('account/',include('django.contrib.auth.urls')),
     path('account/',include('account.urls')),
     path('inquiry/',include('inquiryHistory.urls')),
     path('products/',include('products.urls')),
     path('companies/',include('companies.urls')),
    #  path('tasks/',include('Tasks.urls')),
     path('inspections/',include('inspections.urls')),
     path('InspectionDetails/',include('InspectionDetails.urls')),
    #  path('shipping/',include('Shipping.urls')),
     
     
     
     path ('',include('order.urls')),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

