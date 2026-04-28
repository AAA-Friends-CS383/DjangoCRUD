from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("todos", views.todos_collection),
    path("todos/reorder", views.reorder_todos),
    path("todos/<int:id>", views.todo_detail),
    path("todos/<int:id>/toggle", views.toggle_todo),
]
