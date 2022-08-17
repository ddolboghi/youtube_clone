from django.shortcuts import render, get_object_or_404, redirect
from .models import ToDo
from django.views.generic import ListView, CreateView
from .form import ToDoForm

class ToDoList(ListView):
  model = ToDo
  ordering = '-pk'

class ToDoNew(CreateView):
  form_class = ToDoForm
  success_url = 'list'
  template_name = 'to_do/new_todo.html'
  
def delete_todo(request, pk):
  todo = get_object_or_404(ToDo, pk=pk)
  todo.delete()
  # todo_list = ToDo.objects.order_by('-pk')
  # context = {'todo_list': todo_list}
  # if pk is not None:
  #   return render(request, 'to_do/todo_list.html', context)
  return redirect('list')
  