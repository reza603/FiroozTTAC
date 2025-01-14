from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import UserListCreateView, UserRetrieveUpdateDestroyView, SignUpView
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
        
urlpatterns = [
    path('loginAPP/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('users/', UserListCreateView.as_view(), name='user-list-create'),
    path('users/<int:pk>/', UserRetrieveUpdateDestroyView.as_view(), name='user-detail'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('logout/', views.custom_logout, name='logout'),

    # API token authentication
    # path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]


# from django.urls import path
# from .views import userAPIView,login,LoginView,CustomUserListView,UserRetrieveUpdateDestroyView,UserListPublishedView
# from . import views
# urlpatterns = [
#      path('signup/', views.SignUpView.as_view(),name='signup'),
#    # path('login/', login_page, name='login'),
#      path('APIUserLogin/', login, name='APIlogin'),
#      path('loginAPP/', views.LoginView.as_view(), name='loginapi'),#this is for login 
#      #path('users/', UserListCreateView.as_view(), name='user-list-create'),
#      path('users/<int:pk>/', UserRetrieveUpdateDestroyView.as_view(), name='user-retrieve-update-destroy'),
#      path('users/published/', UserListPublishedView.as_view(), name='user-list-published'),
#      path('userslist/', CustomUserListView.as_view(), name='userslist'),

#         ]