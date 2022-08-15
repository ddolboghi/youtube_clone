from typing import List
from django.shortcuts import render
from django.views.generic import ListView
from .models import ToDo

class ToDoList(ListView):
  model = ToDo
  ordering = '-pk'