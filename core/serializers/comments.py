from rest_framework import serializers

from core.models import Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"


class CommentLightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ["text"]

    def validate(self, attrs):
        ticket_id = self.initial_data["ticket_id"]
        attrs["ticket_id"] = ticket_id
        try:
            attrs["prev_comment_id"] = (
                Comment.objects.filter(ticket_id=ticket_id).last().id
            )
        except AttributeError:
            return attrs
        return attrs
