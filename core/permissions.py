from rest_framework.permissions import SAFE_METHODS, BasePermission

from authentication.models import DEFAULT_ROLES


class OperatorOnly(BasePermission):
    def has_permission(self, request, view):
        if request.user.role.id == DEFAULT_ROLES["admin"]:
            return True
        return False


class OperatorOrClientsReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):

        return bool(
            request.method in SAFE_METHODS
            and obj.client == request.user
            or request.user.role.id == DEFAULT_ROLES["admin"]
        )
