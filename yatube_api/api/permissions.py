from rest_framework import permissions


class IsAuthor(permissions.BasePermission):
    """Проверка на авторство."""

    def has_object_permission(self, request, view, obj):
        return (
            obj.author == request.user
            or request.method in permissions.SAFE_METHODS
        )
