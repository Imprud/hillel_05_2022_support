from django.contrib import admin
from django.urls import path

from core.api.exchange_rate import btc_usd, history, home
from core.api.tickets import get_all_tickets

# def home(request):
#     headers = {"Content-Type": "application/json"}
#     message = {"message": "Hello here"}
#     data = json.dumps(message)
#     return HttpResponse(data, headers=headers)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("home/", home),
    # exchange rates
    path("btc_usd/", btc_usd),
    path("history/", history),
    # tickets
    path("tickets/", get_all_tickets),
]
