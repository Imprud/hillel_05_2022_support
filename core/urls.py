from django.urls import path

from core.api import TicketRetriveUpdateDestroyAPI, TicketsListCreateAPI

urlpatterns = [
    path("", TicketsListCreateAPI.as_view()),
    path("<int:id_>/", TicketRetriveUpdateDestroyAPI.as_view()),
]
