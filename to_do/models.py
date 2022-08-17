from time import timezone
from django.db import models

class ToDo(models.Model):
  content = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  
  def __str__(self):
    return f'To do({self.pk})'
  
  def get_absolute_url(self):
    return f'/to_do/{self.pk}/'