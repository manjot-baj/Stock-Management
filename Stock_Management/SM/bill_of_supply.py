from django.db import models
from django.utils import timezone
from .models import BaseModel
from .company_data import CompanyDetail, Client
from .product import Product
from .choices import Places, PaymentStatus, Prices, TaxType, TypeUOM
from django.core.validators import MaxValueValidator, MinValueValidator


class BillOfSupply(BaseModel):
    number = models.CharField(null=True, blank=True, max_length=100)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, null=True, blank=True)
    ship_to = models.TextField(null=False, blank=False)
    place_of_supply = models.CharField(choices=Places, null=True, blank=False)
    issue_date = models.DateTimeField(default=timezone.now, null=True, blank=False)
    payment_terms = models.CharField(choices=PaymentStatus, null=True, blank=False)
    due_date = models.DateField(null=True, blank=True)
    grand_total = models.DecimalField(decimal_places=2, max_digits=10, default=0.00)
    company = models.ForeignKey(CompanyDetail, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.client

    class Meta:
        db_table = 'bill_of_supply'
        verbose_name_plural = 'Bill Of Supply'


class BillOfSupplyLines(BaseModel):
    bill = models.ForeignKey(BillOfSupply, on_delete=models.CASCADE, null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    uom = models.CharField(choices=TypeUOM, max_length=20, null=True, blank=False)
    quantity = models.PositiveIntegerField(default=1, null=True, blank=False)
    unit_price = models.FloatField(null=True, blank=False, default=0.0)
    discount = models.PositiveIntegerField(null=True, blank=False,
                                           default=0, validators=[MaxValueValidator(100), MinValueValidator(0)])

    class Meta:
        db_table = 'Bill_of_supply_Lines'
        verbose_name_plural = 'Bill Of Supply Lines'
