from django.contrib import admin
from .models import Transaction, Category, Currency

# Enregistrement des modèles dans l'interface admin
@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('name', 'amount', 'date', 'category', 'currency')
    search_fields = ('name',)
    list_filter = ('category', 'currency', 'date')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
    list_display = ('name', 'symbol')
    search_fields = ('name',)
from django.contrib import admin

# Register your models here.
