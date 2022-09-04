from django.urls import path

from to_do.models import ToDo
from . import views

urlpatterns = [
    path('', views.ToDoList.as_view(), name='list'),
    path('done_list/', views.DoneList.as_view(), name='done_list'),
    path('new_todo/', views.ToDoNew.as_view(), name='new'),
    path('done_todo/<int:pk>/', views.done_todo, name='done'),
    path('delete_todo/<int:pk>/', views.delete_todo, name='delete'),
]
