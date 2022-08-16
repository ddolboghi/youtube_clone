from django.shortcuts import render, get_object_or_404, redirect
from .models import ToDo
from django.views.generic import ListView
from .form import ToDoForm

class ToDoList(ListView):
  model = ToDo
  ordering = '-pk'

def new_todo(request, pk):
  todo_form = ToDoForm
  todo_form.save()
  return render(request, 'to_do/todo_list.html')
  
def delete_todo(request, pk):
  todo = get_object_or_404(ToDo, pk=pk)
  todo.delete()
  todo_list = ToDo.objects.order_by('-pk')
  context = {'todo_list': todo_list}
  if pk is None:
    return render(request, 'to_do/todo_list.html', context)
  return redirect('list')
  