from rest_framework import viewsets, mixins

from .serializer import TaskListSerializer, TaskSerializer, AttachementSerializer
from .models import TaskList, Task, Attachement
from .permission import AllowToEditTaskListElseNone, IsAllowTOEditTaskElseNone


class TaskListViewSet(mixins.CreateModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.DestroyModelMixin,
                      mixins.ListModelMixin,
                      viewsets.GenericViewSet):
    queryset = TaskList.objects.all()
    serializer_class = TaskListSerializer
    permission_classes = [AllowToEditTaskListElseNone,]


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAllowTOEditTaskElseNone]


class AttachementViewSet(mixins.CreateModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.DestroyModelMixin,
                      mixins.ListModelMixin,
                      viewsets.GenericViewSet):
    queryset = Attachement.objects.all()
    serializer_class = AttachementSerializer
    permission_classes = []

