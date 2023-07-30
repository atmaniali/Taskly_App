from rest_framework import routers

from .viewset import TaskListViewSet, TaskViewSet, AttachementViewSet

app_name = 'task'
router = routers.DefaultRouter()

router.register(r'taskList', TaskListViewSet)
router.register(r'task', TaskViewSet)
router.register(r'attachement', AttachementViewSet)
