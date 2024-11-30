from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    # Route pour l'interface admin
    path('admin/', admin.site.urls),

    # Inclusion des routes de l'application "transactions"
    path('', include('transactions.urls')),  # L'inclusion correcte
]
