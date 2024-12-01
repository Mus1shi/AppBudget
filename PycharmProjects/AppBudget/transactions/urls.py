from django.urls import path
from . import views

urlpatterns = [
    # Vues API
    path('transaction_summary/', views.transaction_summary, name='transaction_summary'),
    path('transaction_detail/<int:id>/', views.transaction_detail_api, name='transaction_detail'),
    path('expense_summary/', views.expense_summary, name='expense_summary'),

    # Vues fonctionnelles (HTML)
    path('list/', views.transaction_list, name='transaction_list'),
    path('create/', views.transaction_create, name='transaction_create'),
    path('update/<int:pk>/', views.transaction_update, name='transaction_update'),
    path('delete/<int:pk>/', views.transaction_delete, name='transaction_delete'),

    # Routes pour les ViewSets
    path('categories/', views.CategoryViewSet.as_view({'get': 'list', 'post': 'create'}), name='categories'),
    path('categories/<int:pk>/', views.CategoryViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='category_detail'),
    path('currencies/', views.CurrencyViewSet.as_view({'get': 'list', 'post': 'create'}), name='currencies'),
    path('currencies/<int:pk>/', views.CurrencyViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='currency_detail'),
    path('transactions/', views.TransactionViewSet.as_view({'get': 'list', 'post': 'create'}), name='transactions'),
    path('transactions/<int:pk>/', views.TransactionViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='transaction_detail_viewset'),
]
