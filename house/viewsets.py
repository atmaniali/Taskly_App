from rest_framework import viewsets

from .models import House
from .serializer import HouseSerializer
from .permission import IsManagerOrNull


class HouseViewSets(viewsets.ViewSet):
    queryset = House.objects.all()
    serializer_class = HouseSerializer
    permission_classes = [IsManagerOrNull]
