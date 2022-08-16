from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.ToDoList.as_view(), name='list'),
    path('new_todo/<int:pk>/', views.new_todo, name='new'),
    path('delete_todo/<int:pk>/', views.delete_todo, name='delete'),
]
