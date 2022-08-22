from django.urls import path
from . import views

urlpatterns = [
    path('', views.ToDoList.as_view(), name='list'),
    path('new_todo/', views.ToDoNew.as_view(), name='new'),
    path('delete_todo/<int:pk>/', views.delete_todo, name='delete'),
]
