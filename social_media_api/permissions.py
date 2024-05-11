from rest_framework import permissions
from rest_framework.permissions import BasePermission


class AllowAllPermission(BasePermission):
    def has_permission(self, request, view):
        return True

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Дозволяє редагувати тільки власника об'єкта.
    """

    def has_object_permission(self, request, view, obj):
        # Дозволяє всім читати, але тільки власнику редагувати
        if request.method in permissions.SAFE_METHODS:
            return True

        # Дозволяє редагувати тільки власнику об'єкта
        return obj.created_by == request.user