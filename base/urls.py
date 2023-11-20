from django.urls import path #accessing all views from the taskmaster folder
from . import views #accessing all views from the base folder

urlpatterns = [
    path('', views.tasklist, name='tasks'), #this is base url that is empty string in the beginning
]
