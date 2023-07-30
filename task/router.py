from rest_framework import routers

from .viewset import TaskListViewSet

app_name = 'task'
router = routers.DefaultRouter()

router.register(r'taskList', TaskListViewSet)
