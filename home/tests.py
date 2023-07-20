from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Invoice,InvoiceDetail

# Create your tests here.
class InvoiceAPITestCase(APITestCase):
    def test_create_invoice(self):
        url = '/invoices/'
        data = {
            'date': '2023-07-21',
            'invoice_no': '004',
            'customer_name': 'thomas shelby',
            'details': [
                {
                    'description': 'Car',
                    'quantity': 2,
                    'unit_price': '50.00',
                    'price': '100.00',
                },
                {
                    'description': 'Book',
                    'quantity': 1,
                    'unit_price': '30.00',
                    'price': '30.00',
                },
            ],
        }

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Invoice.objects.count(), 1)
        self.assertEqual(Invoice.objects.get().customer_name, 'thomas shelby')
    
 
