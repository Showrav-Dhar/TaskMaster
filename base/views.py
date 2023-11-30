from django.shortcuts import render
# Create your views here.
# from django.http import HttpResponse #step 1 
#as we are doing class based view we can remove the HttpResponse instead of that we will use the following line 
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Task


class TaskList(ListView): 
    model = Task#this class now search for templates that has name like - Task_list.html
    context_object_name = 'tasks'


class TaskDetail(DetailView):
    model = Task#this class now search for templates that has name like - Task_detail.html
    context_object_name = 'task'
    template_name = 'base/task.html'
