from django.urls import path #accessing all views from the taskmaster folder
# from . import views #accessing all views from the base folder
from .views import TaskList, TaskDetail

urlpatterns = [
    path('', TaskList.as_view(), name='tasks'), #this is base url that is empty string in the beginning
    path('task/<int:pk>/', TaskDetail.as_view(), name='task'),#task/the task number
]
