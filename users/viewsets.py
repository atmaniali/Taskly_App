from rest_framework import viewsets
from django.contrib.auth.models import User

from .serializer import UserSerializer, ProfileSerializer
from .permission import IsUserOwnerOrGetOrPostOnly, IsProfileOwnerOrGetOrPostOnly
from .models import Profile
from .logger import logger


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    logger.info("USER VIEWSET IS RUN OK")
    permission_classes = [IsUserOwnerOrGetOrPostOnly]


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsProfileOwnerOrGetOrPostOnly]
