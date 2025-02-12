import os

from app.routing import \
    websocket_urlpatterns  # ✅ Ensure this matches your project
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": URLRouter(websocket_urlpatterns),  # ✅ Ensure WebSocket URLs are included
})
