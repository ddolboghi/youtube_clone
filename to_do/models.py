from time import timezone
from django.db import models

class ToDo(models.Model):
  title = models.CharField(max_length=100)
  content = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  
  def __str__(self):
    return f'{self.title}({self.pk})'