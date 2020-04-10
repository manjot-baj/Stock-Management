from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils import timezone
from .models import BaseModel
from .company_data import CompanyDetail, Client
from .product import Product
from .choices import Places, PaymentStatus, Prices, TaxType, TypeUOM
import random


def random_string():
    return str(random.randint(10000, 99999))


class Invoice(BaseModel):
    no = models.CharField(default=random_string, max_length=50, null=True)
    number = models.CharField(null=True, blank=True, max_length=100)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, null=True, blank=True)
    ship_to = models.TextField(null=True, blank=False, max_length=250)
    place_of_supply = models.CharField(max_length=50, choices=Places, null=True, blank=False)
    issue_date = models.DateTimeField(default=timezone.now, null=True, blank=False)
    payment_terms = models.CharField(max_length=50, choices=PaymentStatus, null=True, blank=False)
    due_date = models.DateTimeField(null=True, blank=True)
    grand_total = models.DecimalField(decimal_places=2, max_digits=10, default=0.00, null=True, blank=True)
    company = models.ForeignKey(CompanyDetail, on_delete=models.SET_NULL, null=True, blank=False)
    with_gst = models.BooleanField(null=True, blank=True)

    def __str__(self):
        return self.no

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

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if self.pk is None:
            if self.tax == 0:
                company = list(Invoice.objects.filter(no=self.invoice).values('company'))
                count = Invoice.objects.filter(company_id=company[0].get('company'), with_gst=False).count()
                Invoice.objects.filter(no=self.invoice).update(number=count+1, with_gst=False)
                invoice_save = super(InvoiceLines, self).save(force_insert=False, force_update=False, using=None,
                                                              update_fields=None)
            elif not self.tax == 0:
                company = list(Invoice.objects.filter(no=self.invoice).values('company'))
                count = Invoice.objects.filter(company_id=company[0].get('company'), with_gst=True).count()
                Invoice.objects.filter(no=self.invoice).update(number=count+1, with_gst=True)
                invoice_save = super(InvoiceLines, self).save(force_insert=False, force_update=False, using=None,
                                                              update_fields=None)
        else:
            invoice_save = super(InvoiceLines, self).save(force_insert=False, force_update=False, using=None,
                                                          update_fields=None)
        return invoice_save
