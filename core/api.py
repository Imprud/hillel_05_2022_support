from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from core.models import Ticket
from core.serializers import TicketLightSerializer, TicketSerializer


@api_view(["GET", "POST"])
@permission_classes([IsAuthenticatedOrReadOnly])
def get_post_tickets(request):
    if request.method == "GET":
        tickets = Ticket.objects.all()
        data = TicketLightSerializer(tickets, many=True).data
        return Response(data=data)
    serializer = TicketSerializer(data=request.data)
    serializer.is_valid()

    instance = serializer.create(serializer.validated_data)
    results = TicketSerializer(instance).data
    return Response(data=results, status=status.HTTP_201_CREATED)


@api_view(["GET", "PUT", "DELETE"])
@permission_classes([IsAuthenticatedOrReadOnly])
def retrieve_update_delete_ticket(request, id_: int):

    try:
        ticket = Ticket.objects.get(id=id_)
    except Ticket.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        data = TicketSerializer(ticket).data
        return Response(data)

    # NOTE: I commented this because in this case we need to accept all required fields to update the ticket -
    # we need to get 'theme" and 'description'
    #
    # elif request.method == "PUT":
    #     serializer = TicketSerializer(ticket, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # NOTE: Here I tried to update the ticket even if we get only 1 field (from 2 required).
    # it works, but looks like not the best solution
    elif request.method == "PUT":
        new_data = TicketSerializer(ticket).data
        for key, value in request.data.items():
            new_data[key] = value

        serializer = TicketSerializer(ticket, data=new_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        ticket.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
