from django.shortcuts import render,redirect
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import InspectionSerializer
from django.views.generic import CreateView, ListView
from django.views.generic import CreateView
from .models import Inspection
from .forms import InspectionForm
from django.http import request

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .models import Inspection
from .serializers import InspectionSerializer
from rest_framework import generics
from rest_framework import viewsets
# from jalali_date import datetime2jalali
from .utils import datetime2jalali  # type: ignore
from .serializers import InspectionSerializer



class InspectionCreateView(CreateView):
    model = Inspection
    form_class = InspectionForm
    template_name = "inspections/inspection_form.html"
    success_url = "/inspections/inspectionlist"  # Change this to your desired URL
def my_view(request):
    inspection = Inspection.objects.get(id=1)
    jalali_date = datetime2jalali(inspection.refer_date).strftime('%Y/%m/%d')
    return render(request, 'inspections/inspection_form.html', {'jalali_date': jalali_date})


# Create your views here.


class InspectionViewSet(viewsets.ReadOnlyModelViewSet):#it is ok
    # This viewset will only allow GET requests (list and retrieve)
    permission_classes = [IsAuthenticated] # This will require a valid token for authentication
    serializer_class = InspectionSerializer

    def get_queryset(self):
    # This will filter the inspection records by the user id of the current user
     return Inspection.objects.filter(user_id=self.request.user.id)


from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from .models import Inspection

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def mark_task_done(request):
    task_id = request.data.get('taskid')
    if not task_id:
        return Response({"error": "Task ID is required"}, status=status.HTTP_400_BAD_REQUEST)

    try:
        inspection = Inspection.objects.get(id=task_id, user=request.user)
        inspection.done = True
        inspection.save()
        return Response({"message": "Task marked as done"}, status=status.HTTP_200_OK)
    except Inspection.DoesNotExist:
        return Response({"error": "Task not found or you do not have permission to modify this task"}, status=status.HTTP_404_NOT_FOUND)

# class MarkTaskDoneView(APIView):
#     permission_classes = [IsAuthenticated]

#     def post(self, request, format=None):
#      task_id = request.data.get('taskid')
#      if not task_id:
#         return Response({"error": "Task ID is required"}, status=status.HTTP_400_BAD_REQUEST)

#      try:
#             inspection = Inspection.objects.get(id=task_id, user=request.user)
#             inspection.done = True
#             inspection.save()
#             return Response({"message": "Task marked as done"}, status=status.HTTP_200_OK)
#         except Inspection.DoesNotExist:
#             return Response({"error": "Task not found or you do not have permission to modify this task"}, status=status.HTTP_404_NOT_FOUND)

from jalali_date import datetime2jalali, date2jalali

def my_view(request):
	jalali_join = datetime2jalali(request.user.date_joined).strftime('%y/%m/%d _ %H:%M:%S')


class inspectionListView(ListView):
    model = Inspection
    template_name = "/inspections/inspection_list.html"
    context_object_name = 'object_list'
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
