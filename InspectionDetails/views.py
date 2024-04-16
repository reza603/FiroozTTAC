from django.shortcuts import render,redirect
from rest_framework.response import Response
from rest_framework.decorators import api_view
import json
from django.views.generic import CreateView
from django.http import JsonResponse
from .forms import inspectionDetail
from rest_framework import viewsets
from .models import inspectionDetail
from .serializers import inspectionDetailSerializer

from rest_framework import generics, permissions

















def inspectiondetail_createAPI(request):
 if request.method == 'POST':
    # get the token object from the request
    token = request.auth
    # check if the token is valid
    if token and token.user.is_active:
    # proceed with the rest of the view logic
     json_data = request.data # get the JSON data from the request
     for obj in json_data: # loop through the array of objects
    # create an instance of InspectionDetails model with the fields from the object
        inspection_detail = inspectionDetail(
        Inspection=obj['Inspection'],
        uid=obj['uid'],
        scanDateTime=obj['scanDateTime']
                                            )        
    # save the instance to the database
        inspection_detail.save()
    # return a success response
        return JsonResponse({'message': 'Inspection details created successfully'}, status=201)
     else:
    # return an unauthorized response
       return JsonResponse({'message': 'Invalid token'}, status=401)
 else:
    # return a bad request response
    return JsonResponse({'message': 'Invalid request method'}, status=400)

    
    

 
from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import inspectionDetail
from .serializers import inspectionDetailSerializer
from barcode.models import Barcode
from barcode.serializers import BarcodeSerializer

from products.models import Product
from companies.models import Company
from order.models import tblOrder
@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def inspection_detail_create_api(request):
   # Initialize an empty dictionary for barcode data
   barcode_data = {}
   # Create an inspection detail serializer with the request data
   serializer = inspectionDetailSerializer(data=request.data)
   print(serializer)
   # Check if the serializer is valid
   if serializer.is_valid():
      # Save the inspection detail object
      inspection_detail = serializer.save()
      print(serializer.data)
      # Get the uid of the inspection detail
      uid = serializer.validated_data["uid"]
      print(uid)
      # Get the barcode queryset that matches the uid
      barcode_queryset = Barcode.objects.filter(UUID=uid)
      # Check if the barcode queryset is not empty
      if barcode_queryset:
       # Create a barcode serializer with the barcode queryset and many=True
       serializer = BarcodeSerializer(barcode_queryset, many=True)
       # Get the JSON data from the barcode serializer
       barcode_data = serializer.data
      # Return a 201 response with the barcode data
       return Response(barcode_data, status=status.HTTP_201_CREATED)
      else:
      # Return a 404 response with an error message
        return Response({"error": "No barcode found for this uid"}, status=status.HTTP_404_NOT_FOUND)
   else:
   # Return a 400 response with an error message
    return Response({"error": "Invalid inspection detail data"}, status=status.HTTP_400_BAD_REQUEST)
   

class inspectiondetailsViewSet(viewsets.ReadOnlyModelViewSet):#it is ok
    # This viewset will only allow GET requests (list and retrieve)
    permission_classes = [IsAuthenticated] # This will require a valid token for authentication
    serializer_class = inspectionDetailSerializer

    def get_queryset(self):
    # This will filter the inspection records by the user id of the current user
     return Barcode.objects.filter(uuid=self.request.uid)

    
@api_view(['GET'])
def inspectiondetail_trackAPI(request):
 uid = request.query_params.get('uid', None) # get the uid parameter from the query string
 if uid is not None:
  inspection_details = inspectionDetail.objects.filter(uid=uid).order_by('scanDateTime') # filter and sort the inspectionDetail objects by the uid and scanDateTime
  serializer = inspectionDetailSerializer(inspection_details, many=True) # serialize the queryset as a list of JSON objects
  return Response(serializer.data) # return the JSON data as a response
 else:
  return Response(status=status.HTTP_400_BAD_REQUEST) # return a bad request response if no uid parameter is given
# inspection_details = inspectionDetail.objects.filter(uid=uid).order_by('-scanDateTime')



