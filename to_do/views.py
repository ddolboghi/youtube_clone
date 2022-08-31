from django.shortcuts import get_object_or_404, redirect
from .models import ToDo
from django.views.generic import ListView, CreateView
from .form import ToDoForm
from django.contrib.auth.mixins import LoginRequiredMixin

class ToDoList(ListView):
  model = ToDo
  ordering = '-pk'

class ToDoNew(LoginRequiredMixin, CreateView):
  form_class = ToDoForm
  success_url = '/to_do'
  template_name = 'to_do/new_todo.html'
  
  def form_valid(self, form):
    current_user = self.request.user
    if current_user.is_authenticated:
      form.instance.author = current_user
      return super(ToDoNew, self).form_valid(form)
    else:
      return redirect('/to_do/')
  
def delete_todo(request, pk):
  todo = get_object_or_404(ToDo, pk=pk)
  todo.delete()
  return redirect('list')
  