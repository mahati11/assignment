from django.urls import path, include
from .views import InvoiceViewSet

urlpatterns = [
    path('invoices/', InvoiceViewSet.as_view({'get': 'list', 'post': 'create'}), name='invoice-list'),
 
]