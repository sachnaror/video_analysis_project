from app.consumers import ChatConsumer, ProgressConsumer
from django.urls import path

websocket_urlpatterns = [
    path("ws/progress/", ProgressConsumer.as_asgi()),  # ✅ WebSocket endpoint
    path("ws/chat/", ChatConsumer.as_asgi()),  # ✅ WebSocket for chat
]
