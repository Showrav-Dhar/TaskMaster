from django.shortcuts import render
# Create your views here.
# from django.http import HttpResponse #step 1 
#as we are doing class based view we can remove the HttpResponse instead of that we will use the following line 
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy#redirect user sucessfully to a different page
from .models import Task


class TaskList(ListView): 
    model = Task#this class now search for templates that has name like - Task_list.html
    context_object_name = 'tasks'


class TaskDetail(DetailView):
    model = Task#this class now search for templates that has name like - Task_detail.html
    context_object_name = 'task'
    template_name = 'base/task.html'

class TaskCreate(CreateView):#automatically created form and used the data from task model
    #this view looks for a template which name ends with _form.html
    #if we used function based view instead of class based view we would have to do all the work manually 
    model = Task
    # fields = ['title','description']
    fields = '__all__'
    success_url = reverse_lazy('tasks')#when we create a item send the user back to the list

#update view modifies the data
class TaskUpdate(UpdateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('tasks')

class DeleteView(DeleteView):
    #this view looks for a template which name ends with _confirm_delete.html
    model = Task
    context_object_name = 'task' #tasks
    success_url = reverse_lazy('tasks')