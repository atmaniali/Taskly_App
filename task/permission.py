from rest_framework import permissions
import logging
import datetime

logger = logging.getLogger(__name__)


class AllowToEditTaskListElseNone(permissions.BasePermission):
    """
    Custom permission for TaskListViewSet to allow only  owner to edit
    """
    logger.debug(f"TaskList permission is raning {datetime.datetime.now()} hours. ")
    # print("####### TASK LIST PERMISSION ACTIVE")

    def has_permission(self, request, view):

        if request.method in permissions.SAFE_METHODS:
            # print(f'True {request.method}')
            return True

        if not request.user.is_anonymous:
            # print(f'True {request.user.profile}')
            return True
        # print('False')
        return False
        # return True

    def has_object_permission(self, request, view, obj):
        return request.user.profile == obj.created_by
        # return True


class IsAllowTOEditTaskElseNone(permissions.BasePermission):
    """
    Custom permission for TaskViewSet to Allow only members of house to access to its task
    """
    logger.info("Task  permission is running")

    def has_permission(self, request, view):
        logger.debug(">> has permission is runing")
        if not request.user.is_anonymous:
            permission_test = request.user.profile.house != None
            print(f'permission test {permission_test}')
            logger.debug(
                f"permissions of task/permission user : {request.user.username} has permission == {permission_test} at {datetime.datetime.now()} ")
            return request.user.profile.house != None

        return False

    def has_object_permission(self, request, view, obj):
        return request.user.profile.house == obj.task_list.house


class IsAllowToEditAttachementOrNone(permissions.BasePermission):
    """
    Custom permission for AttachementViewSet to Allow
    """

    def has_permission(self, request, view):
        if not request.user.is_anonymous:
            return request.user.profile.house != None

        return False

    def has_object_permission(self, request, view, obj):
        return request.user.profile.house == obj.task.task_list.house
