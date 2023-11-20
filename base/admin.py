from django.contrib import admin
from .models import Task #it is importing Task model from the models.py file of the base folder
# Register your models here.

admin.site.register(Task) #now we have registered our table with the admin panel