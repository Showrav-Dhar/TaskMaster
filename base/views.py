from django.shortcuts import render
# Create your views here.
# from django.http import HttpResponse #step 1 
#as we are doing class based view we can remove the HttpResponse instead of that we will use the following line 
from django.views.generic.list import ListView
from .models import Task

def TaskList(request): #step 2
    model = Task


