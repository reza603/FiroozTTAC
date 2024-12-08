from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth import authenticate
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import CreateView, ListView  # Correct import for generic views
from django.views import generic  # Add this import

from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework import status

from .models import CustomUser
from .serializers import CustomUserSerializer
from .forms import CustomUserCrerationForm, CustomUserChangeForm

# User list and create view
class UserListCreateView(generics.ListCreateAPIView):
    model = CustomUser
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    template_name = "account/user_list.html"

# User retrieve, update, and destroy view
class UserRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

# Sign-up view
class SignUpView(generic.CreateView):
    form_class = CustomUserCrerationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['label_suffix'] = ""
        kwargs['initial'] = {
            "username": "نام کاربری",
            "password1": "کلمه عبور",
            "password2": "تایید کلمه عبور"
        }
        return kwargs

# Login view using DRF token authentication
class LoginAppView(APIView):
    def post(self, request, *args, **kwargs):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)

        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({
                "token": token.key,
                "user_id": user.pk,
                "username": user.username,
                "fname": user.first_name,
                "lname": user.last_name
            }, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)

# Function-based login view (if needed)
@csrf_exempt  
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            return JsonResponse({
                "user_id": user.pk,
                "username": user.username,
                "fname": user.first_name,
                "lname": user.last_name
            })
        else:
            return JsonResponse({'error': 'Invalid username or password'})
    else:
        return JsonResponse({'error': 'Only POST method is allowed'})
