from django.db import models
from django.contrib.auth.models import User #user model takes care of the user information(username,email,passwords)
# Create your models here.

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    #there will be many to one relationship with user model.because one user can have many task
    #on_delete=models.CASCADE means if a user is deleted than all the task related to the user will be deleted too

    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['complete']#any complete task will go the bottom of the listss