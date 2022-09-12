from django.forms import ValidationError
from rest_framework.permissions import SAFE_METHODS, BasePermission

from authentication.models import DEFAULT_ROLES


class OperatorOnly(BasePermission):
    def has_permission(self, request, view) -> bool:
        if request.user.role.id == DEFAULT_ROLES["admin"]:
            return True
        return False


class OperatorOrClientsReadOnly(BasePermission):
    """Only operator can change the ticket"""

    def has_object_permission(self, request, view, obj) -> bool:

        return bool(
            request.method in SAFE_METHODS
            and obj.client == request.user
            or request.user.role.id == DEFAULT_ROLES["admin"]
        )


class AuthenticatedAndCreateTicketClientOnly(BasePermission):
    """GET method can do al authenticated users, but POST method can do only clients"""

    def has_permission(self, request, view) -> bool:
        is_user_admin = request.user.role.id == DEFAULT_ROLES["admin"]
        if request.method == "POST" and is_user_admin:
            raise ValidationError("Only users can create a new ticket")

        return bool(request.user and request.user.is_authenticated)
