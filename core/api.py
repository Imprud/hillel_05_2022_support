from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response

from authentication.models import Role, User
from core.models import Ticket


class TicketsService:
    def get_all_tickets(self):
        return {}


class RoleSerrializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ["id"]


class UserSerrializer(serializers.ModelSerializer):
    role = RoleSerrializer()

    class Meta:
        model = User
        fields = [
            "id",
            "role",
            "email",
            "username",
            "first_name",
            "last_name",
            "age",
            "phone",
        ]


class TicketSerrializer(serializers.ModelSerializer):
    operator = UserSerrializer()
    client = UserSerrializer()

    class Meta:
        model = Ticket
        exclude = ["created_at", "updated_at"]


@api_view(["GET"])
def get_all_tickets(request):
    tickets = Ticket.objects.all()
    data = TicketSerrializer(tickets, many=True).data
    return Response(data=data)
