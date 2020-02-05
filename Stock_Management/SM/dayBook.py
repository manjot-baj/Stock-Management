from django.utils import timezone

from django.db import models
import random
from .models import BaseModel


def random_string():
    return str(random.randint(10000, 99999))


class DayBook(BaseModel):
    number = models.CharField(default=random_string, max_length=50, null=True)
    date = models.DateTimeField(default=timezone.now, null=True, blank=False)
    customerType = (
        ("Customer", "Customer"),
        ("Employ", "Employ"),
        ("Vendor", "Vendor"),
    )
    type = models.CharField(max_length=32, choices=customerType)
    name = models.CharField(max_length=100, null=True, blank=False)
    description = models.TextField(max_length=200, null=True, blank=False)
    statusType = (
        ("Credit", "Credit"),
        ("Debit", "Debit"),
        ("Cash", "Cash"),
        ("Others", "Others"),
    )
    status = models.CharField(max_length=100, choices=statusType)
    amount = models.DecimalField(max_digits=30, decimal_places=2)

    def __str__(self):
        return self.name
