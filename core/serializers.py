from rest_framework import serializers

from authentication.models import Role, User
from core.models import Ticket


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ["id"]


class UserSerializer(serializers.ModelSerializer):
    role = RoleSerializer()

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


class TicketSerializer(serializers.ModelSerializer):
    operator = UserSerializer(read_only=True)
    client = UserSerializer(read_only=True)

    # NOTE: this validation doesn't need by logic (we may change model field by unique value,
    # but logic of the support doesn't require this)
    def validate(self, attrs) -> dict:
        theme = attrs.get("theme")
        if not theme:
            return attrs

        try:
            Ticket.objects.get(theme=theme)
        except Ticket.DoesNotExist:
            return attrs

        raise ValueError("The ticket is already in the database.")

        # NOTE: it's for practice (just to try)
        # data = Ticket.objects.values_list('theme')
        # for elem in chain.from_iterable(data):
        #     if elem == theme:
        #         raise ValueError("The ticket is already in the database.")

    class Meta:
        model = Ticket
        exclude = ["created_at", "updated_at"]


class TicketLightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ["id", "theme", "resolved", "operator", "client"]
