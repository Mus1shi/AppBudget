from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.db.models import Sum
from django.contrib import messages
from .models import Category, Currency, Transaction
from .serializers import CategorySerializer, CurrencySerializer, TransactionSerializer
from .forms import TransactionForm

# === Viewsets pour les API REST ===
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CurrencyViewSet(viewsets.ModelViewSet):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer

class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

# === Vues fonctionnelles pour les templates HTML ===
def transaction_list(request):
    transactions = Transaction.objects.select_related('category', 'currency').all()
    return render(request, 'transactions/transaction_list.html', {'transactions': transactions})

def transaction_create(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Transaction créée avec succès !")
            return redirect('transaction_list')
    else:
        form = TransactionForm()
    return render(request, 'transactions/transaction_create.html', {'form': form})

def transaction_update(request, pk):
    transaction = get_object_or_404(Transaction, pk=pk)
    if request.method == 'POST':
        form = TransactionForm(request.POST, instance=transaction)
        if form.is_valid():
            form.save()
            messages.success(request, "Transaction modifiée avec succès !")
            return redirect('transaction_list')
    else:
        form = TransactionForm(instance=transaction)
    return render(request, 'transactions/transaction_update.html', {'form': form})

def transaction_delete(request, pk):
    transaction = get_object_or_404(Transaction, pk=pk)
    if request.method == 'POST':
        transaction.delete()
        messages.success(request, "Transaction supprimée avec succès !")
        return redirect('transaction_list')
    return render(request, 'transactions/transaction_delete.html', {'transaction': transaction})

# === Vues API ===
@api_view(['GET'])
def transaction_summary(request):
    summary = (
        Transaction.objects.values('category__name')
        .annotate(total=Sum('amount'))
        .order_by('-total')
    )
    return Response(summary)

@api_view(['GET'])
def transaction_detail_api(request, id):
    transaction = get_object_or_404(Transaction, pk=id)
    serializer = TransactionSerializer(transaction)
    return Response(serializer.data)

@api_view(['GET'])
def expense_summary(request):
    data = (
        Transaction.objects.values('category__name')
        .annotate(total=Sum('amount'))
        .order_by('-total')
    )
    return Response(data)
