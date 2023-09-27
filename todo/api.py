from .models import Todo
from rest_framework import viewsets, permissions
from .serializers import TodoSerializer


class TodoViewSet(viewsets.ModelViewSet):
    queryser = Todo.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class =  TodoSerializer
