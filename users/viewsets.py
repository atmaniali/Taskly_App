from rest_framework import viewsets, mixins
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


class ProfileViewSet(viewsets.GenericViewSet, mixins.RetrieveModelMixin, mixins.UpdateModelMixin):
    """_summary_
    custom viewset to just retreive and update Profile model
    Args:
        viewsets (_type_): _description_
        mixins (_type_): _description_
        mixins (_type_): _description_
    """
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsProfileOwnerOrGetOrPostOnly]
