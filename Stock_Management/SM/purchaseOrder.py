from django.db import models
from .models import BaseModel


class PurchaseOrder(BaseModel):
    name = models.CharField(max_length=100, null=True, blank=False)
    GSTIN = models.CharField(max_length=100, null=True, blank=False)
    purchase_order_no = models.CharField(max_length=100, null=True, blank=False)
    po_no = models.CharField(max_length=100, null=True, blank=False)
    issue_date = models.CharField(max_length=100, null=True, blank=False)
    valid_until = models.CharField(max_length=100, null=True, blank=False)
    amount = models.CharField(max_length=100, null=True, blank=False)
    tax = models.CharField(max_length=100, null=True, blank=False)
    CGST = models.CharField(max_length=100, null=True, blank=False)
    SGST = models.CharField(max_length=100, null=True, blank=False)
    IGST = models.CharField(max_length=100, null=True, blank=False)
    CESS = models.CharField(max_length=100, null=True, blank=False)
    total = models.CharField(max_length=100, null=True, blank=False)
    billed = models.CharField(max_length=100, null=True, blank=False)
    advanced_payments = models.CharField(max_length=100, null=True, blank=False)

    def __str__(self):
        return self.name


class Bill(BaseModel):
    name = models.CharField(max_length=100, null=True, blank=False)
    GSTIN = models.CharField(max_length=100, null=True, blank=False)
    bill_no = models.CharField(max_length=100, null=True, blank=False)
    invoice_no = models.CharField(max_length=100, null=True, blank=False)
    po_no = models.CharField(max_length=100, null=True, blank=False)
    issue_date = models.CharField(max_length=100, null=True, blank=False)
    due_date = models.CharField(max_length=100, null=True, blank=False)
    shipping_charges = models.CharField(max_length=100, null=True, blank=False)
    amount_before_tax = models.CharField(max_length=100, null=True, blank=False)
    discount = models.CharField(max_length=100, null=True, blank=False)
    amount_before_tax_after_discount = models.CharField(max_length=100, null=True, blank=False)
    tax = models.CharField(max_length=100, null=True, blank=False)
    CGST = models.CharField(max_length=100, null=True, blank=False)
    SGST = models.CharField(max_length=100, null=True, blank=False)
    IGST = models.CharField(max_length=100, null=True, blank=False)
    CESS = models.CharField(max_length=100, null=True, blank=False)
    total = models.CharField(max_length=100, null=True, blank=False)
    status = models.CharField(max_length=100, null=True, blank=False)
    amount_paid = models.CharField(max_length=100, null=True, blank=False)
    balance = models.CharField(max_length=100, null=True, blank=False)
    Dr_Cr = models.CharField(max_length=100, null=True, blank=False)
    date_of_payment = models.CharField(max_length=100, null=True, blank=False)
    private_notes = models.CharField(max_length=100, null=True, blank=False)
    payments = models.CharField(max_length=100, null=True, blank=False)

    def __str__(self):
        return self.name
