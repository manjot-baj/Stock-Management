from django.db import models
# from django.utils import timezone
from .models import BaseModel

from .company_data import CompanyDetail, Client
from .invoice import Product


class Quotation(BaseModel):
    number = models.CharField(max_length=100, null=True, blank=True)
    client_name = models.ForeignKey(Client, on_delete=models.CASCADE, null=True, blank=False)
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
    Tax_Type = (
        ('1', '1% GST'),
        ('3', '3% GST'),
        ('5', '5% GST'),
        ('12', '12% GST'),
        ('18', '18% GST'),
        ('28', '28% GST'),
    )
    quotation = models.ForeignKey(Quotation, null=True, on_delete=models.PROTECT)
    product = models.ForeignKey(Product, null=True, blank=False, on_delete=models.CASCADE)
    uom = models.CharField(choices=TYPE_UOM, max_length=20, null=True, blank=False)
    quantity = models.PositiveIntegerField(default=1, null=True, blank=False)
    unit_price = models.FloatField(null=True, blank=False, default=0.0)
    tax = models.CharField(choices=Tax_Type, max_length=50, null=True, blank=False)

    class Meta:
        db_table = 'quotation_line'
        verbose_name_plural = 'Quotation Line'
