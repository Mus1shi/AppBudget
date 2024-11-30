from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    CategoryViewSet,
    CurrencyViewSet,
    TransactionViewSet,
    transaction_list,
    transaction_create,
    transaction_update,
    transaction_delete,
    transaction_summary,
    expense_summary,
)

# Routeur pour les APIs avec DRF
router = DefaultRouter()
router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'currencies', CurrencyViewSet, basename='currency')
router.register(r'transactions', TransactionViewSet, basename='transaction')

# URL patterns spécifiques à l'application "transactions"
urlpatterns = [
    # Routes API via le routeur DRF
    path('api/', include(router.urls)),

    # Routes fonctionnelles pour les templates HTML
    path('', transaction_list, name='transaction_list'),
    path('create/', transaction_create, name='transaction_create'),
    path('<int:pk>/update/', transaction_update, name='transaction_update'),
    path('<int:pk>/delete/', transaction_delete, name='transaction_delete'),

    # Routes API spécifiques
    path('api/summary/', transaction_summary, name='transaction_summary'),
    path('api/expense_summary/', expense_summary, name='expense_summary'),
]
