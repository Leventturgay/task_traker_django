from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import Todo
from .serializers import TodoSerializers
from rest_framework.generics import ListCreateAPIView, RetrieveDestroyAPIView
from rest_framework.response import Response
# Create your views here.


@api_view()
def todo_home(request):
    return Response('Api mize Hoşgeldiniz')


class Todos(ListCreateAPIView):
    queryset = Todo.objects.filter(is_done=False)
    serializer_class = TodoSerializers


class Todo_detail(RetrieveDestroyAPIView):
    queryset = Todo.objects.filter(is_done=False)
    serializer_class = TodoSerializers
