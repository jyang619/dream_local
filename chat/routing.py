# chat/routing.py
from django.urls import include, path

from . import consumers

websocket_urlpatterns = [
    path('ws/chat/<str:testroom>/', consumers.ChatConsumer),
]