from django.urls import path
from .import views
from .views import CompanyCreateView, CompanyListView,CompanyAPIView

urlpatterns = [
path("companycreate/", CompanyCreateView.as_view(), name="companycreate"),
path("companylist/", CompanyListView.as_view(), name="companylist"),

]


urlpatterns += [
# path('companieslist/', views.company_list, name='companieslist'),
]