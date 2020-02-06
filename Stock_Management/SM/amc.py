from django.db import models
from django.utils import timezone
from .models import BaseModel
from .company_data import Client
from .invoice import Invoice
import random


def random_string():
    return str(random.randint(10000, 99999))


class Product_type(BaseModel):
    product_type = models.CharField(max_length=100, null=True, blank=False)

    def __str__(self):
        return self.product_type


class AMC(BaseModel):
    number = models.CharField(default=random_string, max_length=50, null=True)
    client_name = models.ForeignKey(Client, on_delete=models.CASCADE, null=True, blank=True)
    invoice_no = models.ForeignKey(Invoice, on_delete=models.CASCADE, null=True, blank=True)
    product_types = models.ForeignKey(Product_type, on_delete=models.CASCADE, null=True, blank=False)
    description = models.TextField(null=True, blank=False)
    start_date = models.DateTimeField(default=timezone.now, null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.number
