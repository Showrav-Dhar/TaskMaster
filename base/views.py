from typing import Any
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.
# from django.http import HttpResponse #step 1 
#as we are doing class based view we can remove the HttpResponse instead of that we will use the following line 
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy#redirect user sucessfully to a different page
from django.contrib.auth.views import LoginView

from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Task



class CustomLoginView(LoginView):
    template_name = 'base/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('tasks')



class TaskList(LoginRequiredMixin, ListView): 
    model = Task#this class now search for templates that has name like - Task_list.html
    context_object_name = 'tasks'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user=self.request.user)
        context['count'] = context['tasks'].filter(complete=False).count
        return context

class TaskDetail(LoginRequiredMixin, DetailView):
    model = Task#this class now search for templates that has name like - Task_detail.html
    context_object_name = 'task'
    template_name = 'base/task.html'

class TaskCreate(LoginRequiredMixin, CreateView):#automatically created form and used the data from task model
    #this view looks for a template which name ends with _form.html
    #if we used function based view instead of class based view we would have to do all the work manually 
    model = Task
    fields = ['title', 'description', 'complete']
    success_url = reverse_lazy('tasks')#when we create a item send the user back to the list

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreate, self).form_valid(form)


#update view modifies the data
class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ['title', 'description', 'complete']
    success_url = reverse_lazy('tasks')

class DeleteView(LoginRequiredMixin, DeleteView):
    #this view looks for a template which name ends with _confirm_delete.html
    model = Task
    context_object_name = 'task' #tasks
    success_url = reverse_lazy('tasks')