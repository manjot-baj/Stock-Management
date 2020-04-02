from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from .models import BaseModel
from .company_data import Vendor, CompanyDetail
from .product import Product
from .choices import Places, PaymentStatus, Prices, TaxType, TypeUOM


class Bill(BaseModel):
    number = models.CharField(max_length=100, null=True, blank=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, null=True, blank=False)
    issue_date = models.DateField(null=True, blank=False)
    due_date = models.DateField(null=True, blank=True)
    payment_terms = models.CharField(max_length=50, choices=PaymentStatus, null=True, blank=False)
    prices_are = models.CharField(max_length=50, choices=Prices, null=True, blank=False)
    place_of_supply = models.CharField(max_length=50, choices=Places, null=True, blank=False)
    grand_total = models.FloatField(null=True, blank=True, default=0.0)
    company = models.ForeignKey(CompanyDetail, on_delete=models.SET_NULL, null=True, blank=False)

    def __str__(self):
        return self.number

    class Meta:
        db_table = 'bill'
        verbose_name_plural = 'Bill'


class BillLines(BaseModel):
    bill = models.ForeignKey(Bill, null=True, on_delete=models.PROTECT)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=False)
    description = models.TextField(null=True, blank=True)
    uom = models.CharField(choices=TypeUOM, max_length=20, null=True, blank=False)
    quantity = models.PositiveIntegerField(default=1, null=True, blank=False)
    purchase_rate = models.FloatField(null=True, blank=True, default=0.0)
    discount = models.PositiveIntegerField(null=True, blank=False,
                                           default=0, validators=[MaxValueValidator(100), MinValueValidator(0)])
    tax = models.CharField(choices=TaxType, max_length=50, null=True, blank=False)

    class Meta:
        db_table = 'bill_lines'
        verbose_name_plural = 'Bill Lines'


class PurchaseOrder(BaseModel):
    number = models.CharField(max_length=100, null=True, blank=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, null=True, blank=False)
    issue_date = models.DateField(null=True, blank=False)
    due_date = models.DateField(null=True, blank=True)
    payment_terms = models.CharField(max_length=50, choices=PaymentStatus, null=True, blank=False)
    prices_are = models.CharField(max_length=50, choices=Prices, null=True, blank=False)
    place_of_supply = models.CharField(max_length=50, choices=Places, null=True, blank=False)
    grand_total = models.FloatField(null=True, blank=True, default=0.0)
    company = models.ForeignKey(CompanyDetail, on_delete=models.SET_NULL, null=True, blank=False)

    def __str__(self):
        return self.number

    class Meta:
        db_table = 'purchase_order'
        verbose_name_plural = 'Purchase Order'


class PurchaseOrderLines(BaseModel):
    purchase_order = models.ForeignKey(PurchaseOrder, null=True, on_delete=models.PROTECT)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=False)
    description = models.TextField(null=True, blank=True)
    uom = models.CharField(choices=TypeUOM, max_length=20, null=True, blank=False)
    quantity = models.PositiveIntegerField(default=1, null=True, blank=False)
    purchase_rate = models.FloatField(null=True, blank=True, default=0.0)
    discount = models.PositiveIntegerField(null=True, blank=False,
                                           default=0, validators=[MaxValueValidator(100), MinValueValidator(0)])
    tax = models.CharField(choices=TaxType, max_length=50, null=True, blank=False)

    class Meta:
        db_table = 'purchase_order_lines'
        verbose_name_plural = 'PurchaseOrder Lines'
