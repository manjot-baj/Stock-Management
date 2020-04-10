from django.db import models
# from django.utils import timezone
from .models import BaseModel
from .company_data import CompanyDetail, Client
from .product import Product
from .choices import Places, PaymentStatus, Prices, TaxType, TypeUOM
import random


def random_string():
    return str(random.randint(10000, 99999))


class Quotation(BaseModel):
    no = models.CharField(default=random_string, max_length=50, null=True)
    number = models.CharField(max_length=100, null=True, blank=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, null=True, blank=False)
    ship_to = models.TextField(null=True, blank=False)
    issue_date = models.DateField(null=True, blank=False)
    due_date = models.DateField(null=True, blank=False)
    grand_total = models.FloatField(null=True, blank=True, default=0.0)
    company = models.ForeignKey(CompanyDetail, on_delete=models.SET_NULL, null=True, blank=False)
    with_gst = models.BooleanField(null=True, blank=True)

    def __str__(self):
        return self.no

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

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if self.pk is None:
            if self.tax == 0:
                company = list(Quotation.objects.filter(no=self.quotation).values('company'))
                count = Quotation.objects.filter(company_id=company[0].get('company'), with_gst=False).count()
                Quotation.objects.filter(no=self.quotation).update(number=count + 1, with_gst=False)
                quotation_save = super(Quotation_lines, self).save(force_insert=False, force_update=False, using=None,
                                                                   update_fields=None)
            elif not self.tax == 0:
                company = list(Quotation.objects.filter(no=self.quotation).values('company'))
                count = Quotation.objects.filter(company_id=company[0].get('company'), with_gst=True).count()
                Quotation.objects.filter(no=self.quotation).update(number=count + 1, with_gst=True)
                quotation_save = super(Quotation_lines, self).save(force_insert=False, force_update=False, using=None,
                                                                   update_fields=None)

        else:
            quotation_save = super(Quotation_lines, self).save(force_insert=False, force_update=False, using=None,
                                                               update_fields=None)
        return quotation_save
