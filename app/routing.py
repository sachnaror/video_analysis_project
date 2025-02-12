from app.consumers import (ChatConsumer,  # ✅ Ensure import works
                           ProgressConsumer)
from django.urls import path

websocket_urlpatterns = [
    path("ws/progress/", ProgressConsumer.as_asgi()),  # ✅ WebSocket for progress updates
    path("ws/chat/", ChatConsumer.as_asgi()),  # ✅ WebSocket for chat responses
]
