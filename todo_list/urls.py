from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("todos", views.todos_collection),
    path("todos/<int:id>", views.todo_detail),
]
