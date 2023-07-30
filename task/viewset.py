from rest_framework import viewsets, mixins

from .serializer import TaskListSerializer
from .models import TaskList
from .permission import AllowToEditTaskListElseNone


class TaskListViewSet(mixins.CreateModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.DestroyModelMixin,
                      mixins.ListModelMixin,
                      viewsets.GenericViewSet):
    queryset = TaskList.objects.all()
    serializer_class = TaskListSerializer
    permission_classes = [AllowToEditTaskListElseNone]