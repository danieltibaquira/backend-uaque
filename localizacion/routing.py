from django.urls import re_path
from . import consumers

#Direcciones de los sockets. Segundo argumento es quien consume los mensages (LocConsumer)
websocket_urlpatterns = [
    re_path(r'ws/loc/biblioteca', consumers.LocConsumer.as_asgi()),
]
