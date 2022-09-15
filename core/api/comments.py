from rest_framework.generics import ListCreateAPIView

from core.models import Comment
from core.permissions import CommentClientOrOperatorOnly
from core.serializers import CommentSerializer
from core.services import CommentAllowance


class CommentListCreateAPI(ListCreateAPIView):
    http_method_names = ["get", "post"]
    serializer_class = CommentSerializer
    lookup_url_kwarg = "ticket_id"
    permission_classes = [CommentClientOrOperatorOnly]

    def get_queryset(self):
        ticket_id: int = self.kwargs[self.lookup_url_kwarg]
        return Comment.objects.filter(ticket_id=ticket_id)

    def post(self, request, *args, **kwargs):
        """Check if it's allowed to create new comment"""
        CommentAllowance.is_allowed_to_create(self)
        return super().post(request, *args, **kwargs)

    # def get_serializer_class(self):
    #     if self.request.method == "POST":
    #         self.serializer_class = CommentLightSerializer
    #     return super().get_serializer_class()

    # def get_ticket_id(self):
    #     return self.kwargs[self.lookup_url_kwarg]

    # def create(self, request, *args, **kwargs):
    #     ticket_id = self.get_ticket_id()
    #     request.data["ticket_id"] = ticket_id
    #     return super().create(request, *args, **kwargs)


# class CommentsListAPI(ListAPIView):
#     http_method_names = ["get"]
#     serializer_class = CommentSerializer
#     lookup_field = "ticket_id"
#     lookup_url_kwarg = "ticket_id"

#     def get_queryset(self):
#         ticket_id = self.kwargs[self.lookup_url_kwarg]

#         return Comment.objects.filter(ticket=ticket_id)
