from django.shortcuts import render
from django.http import HttpResponse #step 1
# Create your views here.

def tasklist(request): #step 2
    return HttpResponse('To Do List')
