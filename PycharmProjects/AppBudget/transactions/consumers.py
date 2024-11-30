import json
from channels.generic.websocket import AsyncWebsocketConsumer

class TransactionConsumer(AsyncWebsocketConsumer):
    """
    WebSocket consumer pour gérer les transactions.
    """
    async def connect(self):
        """
        Méthode appelée lors de l'établissement d'une connexion WebSocket.
        """
        # Accepter la connexion WebSocket
        await self.accept()
        # Envoie un message de bienvenue au client
        await self.send(text_data=json.dumps({
            'type': 'connection_established',
            'message': 'WebSocket connection established'
        }))

    async def disconnect(self, close_code):
        """
        Méthode appelée lors de la déconnexion d'un client.
        """
        # Nettoyage ou journalisation si nécessaire
        print(f"WebSocket disconnected: {close_code}")

    async def receive(self, text_data):
        """
        Méthode appelée lorsqu'un message est reçu via WebSocket.
        """
        # Charger les données reçues en JSON
        data = json.loads(text_data)

        # Exemple de traitement : ajouter un champ 'status'
        response_data = {
            'type': 'transaction',
            'message': 'Transaction received',
            'data': data,
            'status': 'processed'  # Exemple de réponse enrichie
        }

        # Envoyer une réponse JSON au client
        await self.send(text_data=json.dumps(response_data))
