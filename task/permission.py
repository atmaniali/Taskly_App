from rest_framework import permissions


class AllowToEditTaskListElseNone(permissions.BasePermission):
    """
    Custom permission for TaskListViewSet to allow only  owner to edit
    """
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        if not request.user.is_anonymous:
            return True

        return False

    def has_object_permission(self, request, view, obj):
        return request.user.profile == obj.createb_by


class IsAllowTOEditTaskElseNone(permissions.BasePermission):
    """
    Custom permission for TaskViewSet to Allow only members of house to access to its task
    """
    def has_permission(self, request, view):
        if not request.user.is_anonymous:
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

