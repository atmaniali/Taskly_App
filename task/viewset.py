from rest_framework import viewsets, mixins
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status as st
from django.utils import timezone
from django_filters.rest_framework import DjangoFilterBackend, OrderingFilter
from rest_framework.filters import SearchFilter
import logging
import datetime

from .serializer import TaskListSerializer, TaskSerializer, AttachementSerializer
from .models import TaskList, Task, Attachement, COMPLET, NOT_COMPLET
from .permission import AllowToEditTaskListElseNone, IsAllowTOEditTaskElseNone

logger = logging.getLogger(__name__)


class TaskListViewSet(mixins.CreateModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.DestroyModelMixin,
                      # mixins.ListModelMixin,
                      mixins.RetrieveModelMixin,
                      viewsets.GenericViewSet):
    logger.debug(f"TaskListViewSet is called {datetime.datetime.now()} hours ")
    queryset = TaskList.objects.all()
    serializer_class = TaskListSerializer
    permission_classes = [AllowToEditTaskListElseNone]


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAllowTOEditTaskElseNone]
    filter_backends = [SearchFilter, OrderingFilter, DjangoFilterBackend]
    search_fields = ['description', 'name']
    ordering_fields = ['name', 'description']
    ordering = ['name']
    filterset_fields = ['status']

    def get_queryset(self):
        """
        overide query set to show only task billow to user specefique
        """
        queryset = super(TaskViewSet, self).get_queryset()
        profile = self.request.user.profile
        updated_queryset = queryset.filter(created_by=profile)
        return updated_queryset

    @action(methods=['patch'], detail=True)
    def update_task_status(self, request, pk=None):
        try:
            user_profile = request.user.profile
            status = request.data['status']
            task = self.get_object()
            if status == NOT_COMPLET:
                if task.status == COMPLET:
                    task.status = NOT_COMPLET
                    task.completed_by = None
                    task.completed_on = None
                else:
                    raise Exception('Task already mark as not complete')
            elif status == COMPLET:
                if task.status == NOT_COMPLET:
                    task.status = COMPLET
                    task.completed_by = user_profile
                    task.completed_on = timezone.now()
                else:
                    raise Exception('Task already mark as complete')
            else:
                raise Exception('Incorrect status provided')
            task.save()
            serializer = TaskSerializer(instance=task, context={'request':request})
            return Response(serializer.data, status=st.HTTP_200_OK)
        except Exception as e:
            return Response({'detail': str(e)}, status=st.HTTP_400_BAD_REQUEST)


class AttachementViewSet(mixins.CreateModelMixin,
                         mixins.UpdateModelMixin,
                         mixins.DestroyModelMixin,
                         mixins.RetrieveModelMixin,
                         # mixins.ListModelMixin,
                         viewsets.GenericViewSet):
    queryset = Attachement.objects.all()
    serializer_class = AttachementSerializer
    permission_classes = []
