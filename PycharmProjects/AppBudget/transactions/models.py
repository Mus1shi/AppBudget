from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Currency(models.Model):
    name = models.CharField(max_length=50)
    symbol = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.name} ({self.symbol})"

class Transaction(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='transactions')
    currency = models.ForeignKey('Currency', on_delete=models.CASCADE, related_name='transactions')
    name = models.CharField(max_length=100, default="Transaction sans nom")

    def __str__(self):
        return self.name
