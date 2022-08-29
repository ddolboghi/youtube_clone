from time import timezone
from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User

class ToDo(models.Model):
  content = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  
  author = models.ForeignKey(User, on_delete=models.CASCADE)
  
  def __str__(self):
    return f'To do({self.pk}) :: {self.author}'
  
  def get_absolute_url(self):
    return f'/to_do/{self.pk}/'