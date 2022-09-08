from django.db.models import Q
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from authentication.models import DEFAULT_ROLES
from core.models import Ticket
from core.permissions import (
    AuthenticatedAndCreateTicketClientOnly,
    OperatorOrClientsReadOnly,
)
from core.serializers import TicketLightSerializer, TicketSerializer


class TicketsListCreateAPI(ListCreateAPIView):
    permission_classes = [AuthenticatedAndCreateTicketClientOnly]
    http_method_names = ["get", "post"]
    queryset = Ticket.objects.all()
    serializer_class = TicketLightSerializer

    def get_serializer_class(self):
        if self.request.method == "POST":
            self.serializer_class = TicketSerializer
        return super().get_serializer_class()

    def get_queryset(self):
        user = self.request.user

        if user.role.id == DEFAULT_ROLES["admin"]:
            return Ticket.objects.filter(Q(operator=None) | Q(operator=user))

        return Ticket.objects.filter(client=user)


class TicketRetriveUpdateDestroyAPI(RetrieveUpdateDestroyAPIView):
    permission_classes = [OperatorOrClientsReadOnly]
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    lookup_url_kwarg = "id_"

    def get_queryset(self):
        user = self.request.user
        return Ticket.objects.filter(client=user)


# class TicketsListAPI(ListAPIView):
#     permission_classes = [IsAuthenticated]
#     serializer_class = TicketLightSerializer
#     queryset = Ticket.objects.all()
#     permission_classes = [IsAuthenticatedOrReadOnly]

#     # def get_serializer(self, *args, **kwargs):
#     #     return TicketLightSerializer if self.request.method == 'GET' else TicketSerializer


# class TicketsCreateAPI(CreateAPIView):
#     serializer_class = TicketSerializer
#     queryset = Ticket.objects.all()
#     permission_classes = [IsAuthenticated]


# class TicketsRetrieveAPI(RetrieveAPIView):
#     queryset = Ticket.objects.all()
#     serializer_class = TicketSerializer
#     lookup_url_kwarg = "id_"

# @api_view(["GET", "PUT", "DELETE"])
# @permission_classes([IsAuthenticatedOrReadOnly])
# def retrieve_update_delete_ticket(request, id_: int):

#     try:
#         ticket = Ticket.objects.get(id=id_)
#     except Ticket.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == "GET":
#         data = TicketSerializer(ticket).data
#         return Response(data)

#     # NOTE: I commented this because in this case we need to accept all required fields to update the ticket -
#     # we need to get 'theme" and 'description'
#     #
#     # elif request.method == "PUT":
#     #     serializer = TicketSerializer(ticket, data=request.data)
#     #     if serializer.is_valid():
#     #         serializer.save()
#     #         return Response(serializer.data)
#     #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     # NOTE: Here I tried to update the ticket even if we get only 1 field (from 2 required).
#     # it works, but looks like not the best solution
#     elif request.method == "PUT":
#         new_data = TicketSerializer(ticket).data
#         for key, value in request.data.items():
#             new_data[key] = value

#         serializer = TicketSerializer(ticket, data=new_data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == "DELETE":
#         ticket.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# @api_view(["GET", "POST"])
# @permission_classes([IsAuthenticatedOrReadOnly])
# def get_post_tickets(request):
#     if request.method == "GET":
#         tickets = Ticket.objects.all()
#         data = TicketLightSerializer(tickets, many=True).data
#         return Response(data=data)
#     serializer = TicketSerializer(data=request.data)
#     serializer.is_valid()

#     instance = serializer.create(serializer.validated_data)
#     results = TicketSerializer(instance).data
#     return Response(data=results, status=status.HTTP_201_CREATED)


# @api_view(["GET", "PUT", "DELETE"])
# @permission_classes([IsAuthenticatedOrReadOnly])
# def retrieve_update_delete_ticket(request, id_: int):

#     try:
#         ticket = Ticket.objects.get(id=id_)
#     except Ticket.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == "GET":
#         data = TicketSerializer(ticket).data
#         return Response(data)

#     # NOTE: I commented this because in this case we need to accept all required fields to update the ticket -
#     # we need to get 'theme" and 'description'
#     #
#     # elif request.method == "PUT":
#     #     serializer = TicketSerializer(ticket, data=request.data)
#     #     if serializer.is_valid():
#     #         serializer.save()
#     #         return Response(serializer.data)
#     #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     # NOTE: Here I tried to update the ticket even if we get only 1 field (from 2 required).
#     # it works, but looks like not the best solution
#     elif request.method == "PUT":
#         new_data = TicketSerializer(ticket).data
#         for key, value in request.data.items():
#             new_data[key] = value

#         serializer = TicketSerializer(ticket, data=new_data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == "DELETE":
#         ticket.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
