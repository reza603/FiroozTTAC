from django.urls import path
from .views import TaskCreateView,TaskListView,TaskListAPIView
urlpatterns = [
path("taskslist/", TaskListView.as_view(),name='taskslist'),
path("createtask/",TaskCreateView.as_view(),name='createtask'),
]


urlpatterns += [
path('tasks/', TaskListAPIView.as_view(), name='task-list'),
]