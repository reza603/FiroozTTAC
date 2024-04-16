from django.shortcuts import render
from django.views  import generic
from .models import CustomUser
from .serializers import CustomUserSerializer
from .forms  import  CustomUserCrerationForm,CustomUserChangeForm
from django.urls import reverse_lazy
from rest_framework import generics
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from django.contrib.auth import authenticate
from django.http import JsonResponse
from django.views.generic import CreateView, ListView




class UserListCreateView(generics.ListCreateAPIView):
    # A view for listing and creating users
     model = CustomUser
     queryset = CustomUser.objects.all()
     serializer_class = CustomUserSerializer

     template_name = "account/user_list.html"
    
class CustomUserListView(ListView):
    model = CustomUser
    template_name = "account/user_list.html"
class UserRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    # A view for retrieving, updating, and deleting a single user
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

class UserListPublishedView(generics.ListAPIView):
    # A view for listing all published users
    queryset = CustomUser.objects.filter(is_active=True)
    serializer_class = CustomUserSerializer

class SignUpView(generic.CreateView):
     form_class=CustomUserCrerationForm
     template_name='registration/signup.html'
     success_url= reverse_lazy('login')
     def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['label_suffix'] = ""
        kwargs['initial'] = {
        "username": "نام کاربری",
        "password1": "کلمه عبور",
        "password2": "تایید کلمه عبور"
        }
        return kwargs
class userAPIView(generics.ListAPIView):
  queryset = CustomUser.objects.all()
  serializer_class = CustomUserSerializer
  
class LoginView(ObtainAuthToken):#this is ok
   def post(self, request, *args, **kwargs):
     username = request.data.get("username")
     password = request.data.get("password")
     user = authenticate(username=username, password=password)
     if user:
      # token, created = Token.objects.get_or_create(user=user)
       result = Token.objects.get_or_create(user=user)
       token = result[0]
       created = result[1]  
       
       return Response({
        "token": token.key,
        "user_id": user.pk,
        "username": user.username,
        "fname":user.fname,
        "lname":user.lname
                    })
     else:
      return Response({"error": "Invalid credentials"}, status=400)



@csrf_exempt  
def login(request):
  if request.method == 'POST':
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)
    print(user)
    if user is not None:
    # login successful, return the user object as JSON
     return JsonResponse(user.to_dict())
    else:
  # login failed, return an error message
     return JsonResponse({'error': 'Invalid username or password'})
  else:
  # not a POST request, return an error message
    return JsonResponse({'error': 'Only POST method is allowed'})
  
  
  
  