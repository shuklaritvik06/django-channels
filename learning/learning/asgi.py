import os
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from django.core.asgi import get_asgi_application
import home.routing as routes


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "learning.settings")

application = ProtocolTypeRouter(
    {
        "http": get_asgi_application(),
        "websocket": AllowedHostsOriginValidator(
            URLRouter(routes=routes.websocket_routes)
        ),
    }
)
