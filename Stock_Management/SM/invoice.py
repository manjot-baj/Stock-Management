from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils import timezone
from .models import BaseModel
from .company_data import CompanyDetail, Client
from .product import Product
from .choices import Places, PaymentStatus, Prices, TaxType, TypeUOM


class Invoice(BaseModel):
    number = models.CharField(null=True, blank=True, max_length=100)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, null=True, blank=True)
    ship_to = models.TextField(null=True, blank=False, max_length=250)
    place_of_supply = models.CharField(max_length=50,choices=Places, null=True, blank=False)
    issue_date = models.DateTimeField(default=timezone.now, null=True, blank=False)
    payment_terms = models.CharField(max_length=50, choices=PaymentStatus, null=True, blank=False)
    due_date = models.DateTimeField(null=True, blank=True)
    grand_total = models.DecimalField(decimal_places=2, max_digits=10, default=0.00, null=True, blank=True)
    company = models.ForeignKey(CompanyDetail, on_delete=models.SET_NULL, null=True, blank=False)

    def __str__(self):
        return self.number

    class Meta:
        db_table = 'invoice'
        verbose_name_plural = 'Invoice'


class InvoiceLines(BaseModel):
    invoice = models.ForeignKey(Invoice, null=True, on_delete=models.PROTECT)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=False)
    description = models.TextField(null=True, blank=True)
    uom = models.CharField(choices=TypeUOM, max_length=20, null=True, blank=False)
    quantity = models.PositiveIntegerField(default=1, null=True, blank=False)
    unit_price = models.FloatField(null=True, blank=False, default=0.0)
    discount = models.PositiveIntegerField(null=True, blank=False,
                                           default=0, validators=[MaxValueValidator(100), MinValueValidator(0)])
    tax = models.CharField(choices=TaxType, max_length=50, null=True, blank=False)

    class Meta:
        db_table = 'Invoice_Lines'
        verbose_name_plural = 'Invoice Lines'
