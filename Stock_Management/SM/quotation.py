from django.db import models
# from django.utils import timezone
from .models import BaseModel
from .company_data import CompanyDetail, Client
from .product import Product
from .choices import Places, PaymentStatus, Prices, TaxType, TypeUOM


class Quotation(BaseModel):
    number = models.CharField(max_length=100, null=True, blank=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, null=True, blank=False)
    ship_to = models.TextField(null=True, blank=False)
    issue_date = models.DateField(null=True, blank=False)
    due_date = models.DateField(null=True, blank=False)
    grand_total = models.FloatField(null=True, blank=True, default=0.0)
    company = models.ForeignKey(CompanyDetail, on_delete=models.SET_NULL, null=True, blank=False)

    def __str__(self):
        return self.number

    class Meta:
        db_table = 'quotation'
        verbose_name_plural = 'Quotation'


class Quotation_lines(BaseModel):
    quotation = models.ForeignKey(Quotation, null=True, on_delete=models.PROTECT)
    product = models.ForeignKey(Product, null=True, blank=False, on_delete=models.CASCADE)
    uom = models.CharField(choices=TypeUOM, max_length=20, null=True, blank=False)
    quantity = models.PositiveIntegerField(default=1, null=True, blank=False)
    unit_price = models.FloatField(null=True, blank=False, default=0.0)
    tax = models.CharField(choices=TaxType, max_length=50, null=True, blank=False)

    class Meta:
        db_table = 'quotation_line'
        verbose_name_plural = 'Quotation Line'
