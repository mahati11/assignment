from django.db import models

# Create your models here.
class Invoice(models.Model):
    customer_name=models.CharField( max_length=255,default='',null=True)
    invoice_no=models.IntegerField(default=0,null=False)
    date=models.DateField( auto_now=False, auto_now_add=False)
    def __str__(self):
        return str(self.invoice_no)

class InvoiceDetail(models.Model):

    invoice=models.ForeignKey("Invoice", on_delete=models.CASCADE,related_name='details',null=True)
    description=models.CharField( max_length=500,null=True,default='')
    quantity=models.PositiveIntegerField(default=0,null=True)
    unit_price=models.DecimalField( max_digits=50, decimal_places=2)
    price=models.DecimalField( max_digits=50, decimal_places=2)