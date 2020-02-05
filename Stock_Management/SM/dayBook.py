from django.utils import timezone

from django.db import models
import random
from .models import BaseModel
from .company_data import Client, Vendor
from .employee_data import Employee


def random_string():
    return str(random.randint(10000, 99999))


class DayBook(BaseModel):
    number = models.CharField(default=random_string, max_length=50, null=True)
    date = models.DateTimeField(default=timezone.now, null=True, blank=False)
    customerType = (
        ("Customer", "Customer"),
        ("Employee", "Employee"),
        ("Vendor", "Vendor"),
        ("Other", "Other")
    )
    type = models.CharField(max_length=32, choices=customerType, default="Other")
    name = models.CharField(max_length=100, null=True, blank=False)
    customer_name = models.ForeignKey(Client, on_delete=models.CASCADE, null=True, blank=True)
    employee_name = models.ForeignKey(Employee, on_delete=models.CASCADE, null=True, blank=True)
    vendor_name = models.ForeignKey(Vendor, on_delete=models.CASCADE, null=True, blank=True)
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
