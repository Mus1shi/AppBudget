from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('transactions/', include('transactions.urls')),
    path('', lambda request: redirect('transaction_list')),  # Redirige vers la liste des transactions
]
