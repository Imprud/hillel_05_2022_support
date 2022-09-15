from rest_framework import serializers

from core.models import Comment, Ticket


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"
        read_only_fields = ["ticket", "user", "prev_comment"]

    def validate(self, attrs: dict) -> dict:
        request = self.context["request"]
        ticket_id: int = request.parser_context["kwargs"]["ticket_id"]
        ticket: Ticket = Ticket.objects.get(id=ticket_id)
        attrs["ticket"] = ticket
        attrs["user"] = request.user

        last_comment: Comment | None = ticket.comments.last()

        attrs["prev_comment"] = last_comment if last_comment else None

        return attrs

    def create(self, validated_data):
        instance = Comment.objects.create(**validated_data)
        return instance

        # def validate(self, attrs):

    #     ticket_id = self.initial_data["ticket_id"]
    #     attrs["ticket_id"] = ticket_id
    #     try:
    #         attrs["prev_comment_id"] = (
    #             Comment.objects.filter(ticket_id=ticket_id).last().id
    #         )
    #     except AttributeError:
    #         return attrs
    #     return attrs


# class CommentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Comment
#         fields = "__all__"
