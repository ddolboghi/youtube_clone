from django.shortcuts import get_object_or_404, redirect
from .models import ToDo
from django.views.generic import ListView, CreateView
from .form import ToDoForm

class ToDoList(ListView):
  model = ToDo
  ordering = '-pk'

class ToDoNew(CreateView):
  form_class = ToDoForm
  success_url = '/to_do'
  template_name = 'to_do/new_todo.html'
  
def delete_todo(request, pk):
  todo = get_object_or_404(ToDo, pk=pk)
  todo.delete()
  return redirect('list')
  