from rest_framework.exceptions import NotFound

from core.models import Ticket


class TicketsCRUD:
    @staticmethod
    def change_resolved_status(instance: Ticket) -> Ticket:
        instance.resolved = not instance.resolved
        instance.save()


class CommentAllowance:
    @staticmethod
    def is_allowed_to_create(comment_api) -> bool:
        """User is allowed to create new coomment only if ticket not resolved and operator was assigned."""
        ticket_id: int = comment_api.kwargs[comment_api.lookup_url_kwarg]
        ticket = Ticket.objects.get(id=ticket_id)
        if ticket.resolved or not ticket.operator:
            raise NotFound("Comments not found")
        return True
