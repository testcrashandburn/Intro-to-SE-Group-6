from django.shortcuts import render
from transaction.models import Transaction
from django.http import HttpResponse
# Create your views here.
def index(request):
    #print(Transaction.tex)
    return HttpResponse(Transaction.objects.all())