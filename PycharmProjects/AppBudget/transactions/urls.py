from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, CurrencyViewSet, TransactionViewSet, transaction_list, transaction_detail

# Création d'un routeur pour les viewsets
router = DefaultRouter()
router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'currencies', CurrencyViewSet, basename='currency')
router.register(r'transactions', TransactionViewSet, basename='transaction')

urlpatterns = [
    # Routes des viewsets
    path('', include(router.urls)),

    # Routes pour les vues fonctionnelles
    path('transactions/static/', transaction_list, name='transaction_list'),
    path('transactions/static/<int:id>/', transaction_detail, name='transaction_detail'),
]
