import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from transactions.routing import websocket_urlpatterns

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'AppBudget.settings')

application = get_asgi_application()
ASGI_APPLICATION = 'budget_app.asgi.application'

application = ProtocolTypeRouter({
    "http": get_asgi_application(),  # Gestion des requêtes HTTP normales
    "websocket": AuthMiddlewareStack(
        URLRouter(
            websocket_urlpatterns
        )
    ),
})