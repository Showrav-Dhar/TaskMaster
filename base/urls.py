from django.urls import path #accessing all views from the taskmaster folder
# from . import views #accessing all views from the base folder
from .views import TaskList, TaskDetail, TaskCreate, TaskUpdate, DeleteView

urlpatterns = [
    path('', TaskList.as_view(), name='tasks'), #this is base url that is empty string in the beginning
    path('task/<int:pk>/', TaskDetail.as_view(), name='task'),#task/the task number
    path('task-create/', TaskCreate.as_view(), name='task-create'),
    path('task-update<int:pk>/', TaskUpdate.as_view(), name='task-update'),
    path('task-delete<int:pk>/', DeleteView.as_view(), name='task-delete'),
]
