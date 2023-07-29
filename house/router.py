from rest_framework import routers

from .viewsets import HouseViewSets
app_name = 'house'

router = routers.DefaultRouter()

router.register(r'houses', HouseViewSets)
