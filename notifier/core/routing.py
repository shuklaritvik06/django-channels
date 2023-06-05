from django.urls import path
from .consumers import Consumer

websocket_routes = [path("ws/test/", Consumer.as_asgi())]
