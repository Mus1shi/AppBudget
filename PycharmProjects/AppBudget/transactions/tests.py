from django.test import TestCase
from .models import Transaction, Category, Currency

class ModelsTestCase(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Food")
        self.currency = Currency.objects.create(name="Euro", symbol="€")
        self.transaction = Transaction.objects.create(
            name="Dinner",
            amount=50.00,
            date="2024-11-29",
            category=self.category,
            currency=self.currency,
            description="Dinner with friends"
        )

    def test_transaction_creation(self):
        self.assertEqual(self.transaction.name, "Dinner")
        self.assertEqual(self.transaction.amount, 50.00)
        self.assertEqual(self.transaction.category.name, "Food")
        self.assertEqual(self.transaction.currency.symbol, "€")
from django.test import TestCase

# Create your tests here.
