from django.db import models
from django.utils import timezone
from .models import BaseModel

from .company_data import CompanyDetail, Client
from .invoice import Product


# from .PO import POData


class Invoice(BaseModel):
    client_name = models.ForeignKey(Client, on_delete=models.CASCADE, null=True, blank=True)
    ship_to = models.TextField(null=False, blank=False, max_length=250)
    place_of_supply = models.CharField(null=False, blank=False, max_length=100)
    document_number = models.CharField(null=True, blank=False, max_length=100)
    issue_date = models.DateTimeField(default=timezone.now, null=True, blank=False)
    payment_status = (
        ("Net 7", "Net 7"),
        ("Net 10", "Net 10"),
        ("Net 15", "Net 15"),
        ("Net 30", "Net 30"),
        ("Net 45", "Net 45"),
        ("Net 60", "Net 60"),
        ("Net 90", "Net 90"),
        ("Due on Receipt", "Due on Receipt"),
        ("Due on The Specified Date", "Due on The Specified Date"),
    )
    payment_terms = models.CharField(max_length=50, choices=payment_status, null=True, blank=False)
    due_date = models.DateTimeField()

    grand_total = models.DecimalField(decimal_places=2, max_digits=10, default=0.00)
    company = models.ForeignKey(CompanyDetail, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.client_name

    class Meta:
        db_table = 'invoice'
        verbose_name_plural = 'Invoice'


class InvoiceLines(BaseModel):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE, null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    TYPE_UOM = (
        ('Boxes', 'Boxes'),
        ('CFT', 'CFT'),
        ('Centimerets', 'Centimerets'),
        ('Cubic Meters', 'Cubic Meters'),
        ('Gram', 'Gram'),
        ('Hours', 'Hours'),
        ('Inches', 'Inches'),
        ('Killowgrams', 'Killowgrams'),
        ('Piece', 'Piece'),
    )
    uom = models.CharField(choices=TYPE_UOM, max_length=20, null=True, blank=False)
    quantity = models.PositiveIntegerField(default=1, null=True, blank=False)
    unit_price = models.FloatField(null=True, blank=False, default=0.0)

    discount = models.FloatField(null=True, blank=False, default=0.0)

    Tax_Type = (
        ('1', '1% GST'),
        ('3', '3% GST'),
        ('5', '5% GST'),
        ('12', '12% GST'),
        ('18', '18% GST'),
        ('28', '28% GST'),
    )
    tax = models.CharField(choices=Tax_Type, max_length=50, null=True, blank=False)


    class Meta:
        db_table = 'Invoice_Lines'
