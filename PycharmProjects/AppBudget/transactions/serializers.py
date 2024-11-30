from rest_framework import serializers
from .models import Transaction, Category, Currency

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = ['id', 'name', 'symbol']

class TransactionSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    currency = CurrencySerializer()

    class Meta:
        model = Transaction
        fields = ['id', 'name', 'amount', 'date', 'category', 'currency', 'description']
