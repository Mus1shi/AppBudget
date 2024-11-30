from django.urls import re_path
from transactions.consumers import TransactionConsumer

# Définir les routes pour les WebSockets
websocket_urlpatterns = [
    re_path(r'ws/transactions/$', TransactionConsumer.as_asgi()),
]
