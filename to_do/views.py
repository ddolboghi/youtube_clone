from django.shortcuts import get_object_or_404, redirect, render
from .models import ToDo
from django.views.generic import ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

class ToDoList(ListView):
  model = ToDo
  ordering = '-pk'
  
class DoneList(ListView):
  model = ToDo
  template_name = 'to_do/done_list.html'
  context_object_name = 'done_list'
  ordering = '-pk'
  
def done_todo(request, pk):
  todo = get_object_or_404(ToDo, pk=pk)
  todo.is_done = True
  todo.save()
  return redirect('list')
  
  # def form_valid(self, form):
  #   current_user = self.request.user
  #   if current_user.is_authenticated:
  #     form.instance.author = current_user
  #     return super(ToDoNew, self).form_valid(form)
  #   else:
  #     return redirect('list')
    
def new_todo(request):
  if request.method == 'POST':
    content = request.POST.get('content')
    author = request.user
    if author.is_authenticated:
      cur_user = author
      ToDo.objects.create(content=content, author=cur_user)
    else:
      cur_user = None
      ToDo.objects.create(content=content, author=cur_user)
  return redirect('list')

def delete_todo(request, pk):
  todo = get_object_or_404(ToDo, pk=pk)
  cur_user = request.user
  if cur_user.is_authenticated:
    todo.delete()
    return redirect('done_list')
  else:
    todo.delete()
    return redirect('list')
    