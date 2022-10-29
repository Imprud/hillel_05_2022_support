from django.urls import path

from apps.core.api import (
    CommentListCreateAPI,
    TicketAssignApi,
    TicketResolveApi,
    TicketRetriveUpdateDestroyAPI,
    TicketsListCreateAPI,
)

tickets_urls = [
    path("", TicketsListCreateAPI.as_view()),
    path("<int:id_>/", TicketRetriveUpdateDestroyAPI.as_view()),
    path("<int:id_>/assign/", TicketAssignApi.as_view()),
    path("<int:id_>/resolve/", TicketResolveApi.as_view()),
]

commets_urls = [
    path("<int:ticket_id>/comments/", CommentListCreateAPI.as_view()),
]
urlpatterns = tickets_urls + commets_urls
