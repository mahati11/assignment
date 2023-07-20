from django.shortcuts import render
from rest_framework import viewsets
from .models import Invoice, InvoiceDetail
from .serializers import Invoiceserializer
# Create your views here.

class InvoiceViewSet(viewsets.ModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = Invoiceserializer
