from django.shortcuts import render
from .models import Task
from django.views.generic import CreateView, ListView
from .models import  Task
from .forms import TaskForm
from rest_framework import viewsets
from .serializers import  TaskSerializer
from rest_framework import generics

class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = "Tasks/task_form.html"
    success_url = "/tasks/taskslist/" # change this to your desired url

class TaskListView(ListView):
    model = Task
    template_name = "Tasks/taskslist.html"


class TaskListAPIView(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer