from django.db import models
from django.utils import timezone
from .models import BaseModel

from .company_data import CompanyDetail, Client
from .product import Product


class Payment_document(BaseModel):
    client_name = models.ForeignKey(Client, on_delete=models.CASCADE, null=True, blank=True)
    Payment_status = (
        ("Received", "Received"),
        ("Mad", "Mad"),
    )
    payment_status = models.CharField(max_length=20, null=True, blank=True, choices=Payment_status)
    number = models.CharField(null=True, blank=True, max_length=100)
    reference = models.CharField(null=True, blank=True, max_length=100)
    amount = models.DecimalField(decimal_places=2, max_digits=10, default=0.00)
    Payment_Type = (
        ("Cash", "Cash"),
        ("Cash Memo", "Cash Memo"),
        ("Credit Note", "Credit Note"),
        ("Credit Card", "Credit Card"),
        ("Check", "Check"),
        ("Cheque", "Cheque"),
        ("Bank Transfer", "Bank Transfer"),
        ("Pay Slip", "Pay Slip"),
    )
    payment_type = models.CharField(max_length=20, null=True, blank=True, choices=Payment_Type)
    pay_date = models.DateTimeField(default=timezone.now, null=True, blank=False)
    bank_charges = models.DecimalField(decimal_places=2, max_digits=10, default=0.00)
    note = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.client_name
