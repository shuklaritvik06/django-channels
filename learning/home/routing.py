from django.urls import path
from home.consumers import Consumer, AsynConsumer

websocket_routes = [
    path("ws/test/", Consumer.as_asgi()),
    path("ws/json/", AsynConsumer.as_asgi()),
]
