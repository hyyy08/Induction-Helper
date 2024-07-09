from rest_framework.permissions import BasePermission

class IsSuperUser(BasePermission):
    """
    permission to only allow superusers to access a view.
    """

    def has_permission(self, request, view):
        return request.user and request.user.is_superuser