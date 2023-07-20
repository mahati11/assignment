from rest_framework import serializers
from .models import Invoice,InvoiceDetail

class InvoiceDetailserializer(serializers.ModelSerializer):
    class Meta:
        model= InvoiceDetail
        fields='__all__'
class Invoiceserializer(serializers.ModelSerializer):
    details = InvoiceDetailserializer(many=True, required=False)

    class Meta:
        model = Invoice
        fields = '__all__'

    def create(self, validated_data):
        details_data = validated_data.pop('details', [])
        invoice = Invoice.objects.create(**validated_data)
        for detail_data in details_data:
            InvoiceDetail.objects.create(invoice=invoice, **detail_data)
        return invoice