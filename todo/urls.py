
from django.urls import path
from .views import todo_home, Todos, Todo_detail


urlpatterns = [

    path('api/', todo_home),
    path('list-create/', Todos.as_view()),
    path('detail/<int:pk>/', Todo_detail.as_view())

]
