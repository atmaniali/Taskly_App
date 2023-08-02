from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth.models import User
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

from .models import House
from .serializer import HouseSerializer
from .permission import IsManagerOrNull


class HouseViewSets(viewsets.ModelViewSet):
    queryset = House.objects.all()
    serializer_class = HouseSerializer
    permission_classes = [IsManagerOrNull]
    filter_backends = [SearchFilter, OrderingFilter, DjangoFilterBackend]
    search_fields = ['name', 'description']
    ordering_fileds = ['point', 'compelted_task_count', 'not_compelted_task_count']
    ordering = ['point']
    filterset_fields = ['members']

    @action(detail=True, methods=['post'], name='Join', permission_classes=[])
    def join(self, request, pk=None):
        house = self.get_object()
        user_profile = request.user.profile
        try:
            if user_profile.house == None:
                user_profile.house = house
                user_profile.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
            elif user_profile in house.members.all():
                return Response({'detail': 'user is already exist. '}, status=status.HTTP_404_NOT_FOUND)
            else:
                return Response({'detail': 'user not member in this house. '}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as err:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @action(detail=True, methods=['post'], name='Leave', permission_classes=[])
    def leave(self, request, pk=None):
        try:
            user_profile = request.user.profile
            house = self.get_object()
            if user_profile in house.members.all():
                user_profile.house = None
                user_profile.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
            else:
                Response({'detail': 'user not member in this house. '},
                         status=status.HTTP_400_BAD_REQUEST)
        except Exception as err:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @action(detail=True, methods=['post'], name='remove member')
    def remove_members(self, request, pk=None):
        try:
            user_id = request.date.get('user_id', None)
            house = self.get_object()
            if user_id == None:
                return Response(status=status.HTTP_400_BAD_REQUEST)
            user_profile = User.objects.get(pk=user_id).profile
            house_members = house.members

            if user_profile in house_members.all():
                house_members.remove(user_profile)
                house_members.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
            else:
                return Response({'detail': 'user not member in this house. '}, status=status.HTTP_400_BAD_REQUEST)
        except User.DoesNotExist as e:
            return Response({'detail': 'user provider does not exist. '}, status=status.HTTP_400_BAD_REQUEST)
