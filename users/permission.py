from rest_framework import permissions
from .models import Profile


class IsUserOwnerOrGetOrPostOnly(permissions.BasePermission):
    """
    Custom permission to allow only owner user to edit profile. Otherwise Get or Post create profile 
    """

    def has_permission(self, request, view):
        return True

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        if not request.user.is_anonymous:
            return request.user == obj

        return False


class IsProfileOwnerOrGetOrPostOnly(permissions.BasePermission):
    """
    Custom permission for Profiel to allow only owner profile to edit profile. Otherwise Get or Post create profile 
    """

    def has_permission(self, request, view):
        return True

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        if not request.user.is_anonymous:
            # print(f"_____ {obj}")
            # print(f"_____ REQUEST USER {request.user}")
            try:
                return request.user.profile == obj
            except Profile.DoesNotExist:
                return False

        return False
