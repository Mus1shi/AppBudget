from rest_framework import viewsets  # Import nécessaire pour utiliser viewsets
from django.http import JsonResponse
from .models import Category, Currency, Transaction
from .serializers import CategorySerializer, CurrencySerializer, TransactionSerializer

# Viewsets pour les modèles
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CurrencyViewSet(viewsets.ModelViewSet):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer

class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

# Vues fonctionnelles
def transaction_list(request):
    # Exemple de réponse statique
    return JsonResponse({"transactions": []})

def transaction_detail(request, id):
    # Exemple de réponse statique pour une transaction spécifique
    return JsonResponse({"transaction": {"id": id}})
