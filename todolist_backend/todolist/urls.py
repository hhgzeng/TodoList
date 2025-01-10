from django.urls import path
from . import views

urlpatterns = [
    path('api/get-todo', views.get_todo_list, name='get_todo_list'),
    path('api/add-todo', views.add_todo, name='add_todo'),
    path('api/update-todo/', views.update_todo, name='update_todo'),
    path('api/del-todo/', views.delete_todo, name='delete_todo'),
]
