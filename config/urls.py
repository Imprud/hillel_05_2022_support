from django.contrib import admin
from django.urls import path

from config.api import btc_usd, history, home

# def home(request):
#     headers = {"Content-Type": "application/json"}
#     message = {"message": "Hello here"}
#     data = json.dumps(message)
#     return HttpResponse(data, headers=headers)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("home/", home),
    path("btc_usd/", btc_usd),
    path("history/", history),
]
