from django.core.exceptions import ObjectDoesNotExist
from django.forms import ValidationError
from rest_framework.exceptions import NotFound
from rest_framework.permissions import SAFE_METHODS, BasePermission

from apps.authentication.models import DEFAULT_ROLES
from apps.core.models import Ticket


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


class CommentClientOrOperatorOnly(BasePermission):
    """only Operator or Client can create or read comments and ticket must be unresolved"""

    def has_permission(self, request, view):
        ticket_id = request.parser_context["kwargs"]["ticket_id"]
        try:
            ticket = Ticket.objects.get(id=ticket_id)
            return bool(
                ticket.client == request.user or ticket.operator == request.user
            )
        except ObjectDoesNotExist:
            raise NotFound("Comments not found")
