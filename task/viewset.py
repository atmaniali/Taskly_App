from rest_framework import viewsets

from .serializer import TaskListSerializer
from .models import TaskList


class TaskListViewSet(viewsets.ModelViewSet):
    queryset = TaskList.objects.all()
    serializer_class = TaskListSerializer
    # permission_classes = []
