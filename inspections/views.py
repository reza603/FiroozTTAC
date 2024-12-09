from django.shortcuts import render,redirect
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import InspectionSerializer
from django.views.generic import CreateView, ListView
from django.views.generic import CreateView
from .models import Inspection
from .forms import InspectionForm
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .models import Inspection
from .serializers import InspectionSerializer
from rest_framework import generics
from rest_framework import viewsets

from .serializers import InspectionSerializer


class InspectionCreateView(CreateView):
 model = Inspection
 form_class = InspectionForm
 template_name = "inspections/inspection_form.html"
 success_url = "/inspections/inspectionlist" # change this to your desired url


class InspectionViewSet(viewsets.ReadOnlyModelViewSet):#it is ok
    # This viewset will only allow GET requests (list and retrieve)
    permission_classes = [IsAuthenticated] # This will require a valid token for authentication
    serializer_class = InspectionSerializer

    def get_queryset(self):
    # This will filter the inspection records by the user id of the current user
     return Inspection.objects.filter(user_id=self.request.user.id)






class inspectionListView(ListView):
    model = Inspection
    template_name = "/inspections/inspection_list.html"
# class InspectionViewSet(viewsets.ModelViewSet):
#  #permission_classes = [IsAuthenticated]
#  queryset = Inspection.objects.all()
#  serializer_class = InspectionSerializer

class inspectionListAPIView(generics.ListAPIView):
    queryset = Inspection.objects.all()
    serializer_class = InspectionSerializer
class InspectionView(APIView):
    http_method_names = ["CreateAPIInspection", "getTaskAPI"]
    permission_classes = [IsAuthenticated]

    def CreateAPIInspection(self, request, format=None):
    # Get the user from the request
        user = request.user
        # Get the data from the request
        data = request.data
        # Add the user id to the data
        data["user_id"] = user.id
        # Serialize the data using the serializer
        serializer = InspectionSerializer(data=data)
        # Validate and save the data if valid
        if serializer.is_valid():
         serializer.save()
         # Return the serialized data and status code 201 (Created)
         return Response(serializer.data, status=status.HTTP_201_CREATED)
        # Return the validation errors and status code 400 (Bad Request)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class InspectionView(APIView):
    http_method_names = ["getTaskAPI"]
   # permission_classes = [IsAuthenticated]
    def getTaskAPI(self, request, format=None):
        # Get all the inspections from the database
        inspections = Inspection.objects.all()
        # Serialize them to JSON using the serializer
        serializer = InspectionSerializer(inspections, many=True)
        # Return the JSON response with status code 200 (OK)
        return Response(serializer.data, status=status.HTTP_200_OK)
