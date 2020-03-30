from django.db import models
# from django.utils import timezone
from .models import BaseModel

from .company_data import CompanyDetail


# from .PO import POData


# class Invoice(BaseModel):
#     client_name = models.ForeignKey(Client, on_delete=models.CASCADE, null=True, blank=True)
#     v_a_t_no = models.CharField(max_length=100, null=True, blank=False)
#     invoice_no = models.CharField(max_length=100, null=True, blank=False)
#     p_o_no = models.ForeignKey(POData, on_delete=models.CASCADE, null=True, blank=True)
#     issue_date = models.CharField(max_length=100, null=True, blank=False)
#     due_date = models.CharField(max_length=100, null=True, blank=False)
#     amount_before_tax = models.CharField(max_length=100, null=True, blank=False)
#     discount = models.CharField(max_length=100, null=True, blank=False)
#     tax = models.CharField(max_length=100, null=True, blank=False)
#     total = models.CharField(max_length=100, null=True, blank=False)
#     status = models.CharField(max_length=100, null=True, blank=False)
#     amount_paid = models.CharField(max_length=100, null=True, blank=False)
#     balance = models.CharField(max_length=100, null=True, blank=False)
#     dr_or_cr = models.CharField(max_length=100, null=True, blank=False)
#     date_of_payment = models.CharField(max_length=100, null=True, blank=False)
#     invoice_type = models.CharField(max_length=100, null=True, blank=False)
#     private_note = models.TextField(null=True, blank=False)
#     payments = models.TextField(null=True, blank=False)
#
#     def __str__(self):
#         return self.client_name
#
#
# class Quotation(BaseModel):
#     client_name = models.ForeignKey(Client, on_delete=models.CASCADE, null=True, blank=True)
#     estimate_no = models.CharField(max_length=100, null=True, blank=False)
#     p_o_no = models.ForeignKey(POData, on_delete=models.CASCADE, null=True, blank=True)
#     issue_date = models.CharField(max_length=100, null=True, blank=False)
#     valid_until = models.CharField(max_length=100, null=True, blank=False)
#     amount = models.CharField(max_length=100, null=True, blank=False)
#     tax = models.CharField(max_length=100, null=True, blank=False)
#     discount = models.CharField(max_length=100, null=True, blank=False)
#     total = models.CharField(max_length=100, null=True, blank=False)
#     invoiced = models.CharField(max_length=100, null=True, blank=False)
#     quotation_type = models.CharField(max_length=100, null=True, blank=False)
#
#     def __str__(self):
#         return self.client_name
#
#
# class Bill(BaseModel):
#     vendor_name = models.ForeignKey(Vendor, on_delete=models.CASCADE, null=True, blank=True)
#     GSTIN = models.CharField(max_length=100, null=True, blank=False)
#     bill_no = models.CharField(max_length=100, null=True, blank=False)
#     invoice_no = models.ForeignKey(Invoice, on_delete=models.CASCADE, null=True, blank=True)
#     po_no = models.ForeignKey(POData, on_delete=models.CASCADE, null=True, blank=True)
#     issue_date = models.CharField(max_length=100, null=True, blank=False)
#     due_date = models.CharField(max_length=100, null=True, blank=False)
#     shipping_charges = models.CharField(max_length=100, null=True, blank=False)
#     amount_before_tax = models.CharField(max_length=100, null=True, blank=False)
#     discount = models.CharField(max_length=100, null=True, blank=False)
#     amount_before_tax_after_discount = models.CharField(max_length=100, null=True, blank=False)
#     tax = models.CharField(max_length=100, null=True, blank=False)
#     CGST = models.CharField(max_length=100, null=True, blank=False)
#     SGST = models.CharField(max_length=100, null=True, blank=False)
#     IGST = models.CharField(max_length=100, null=True, blank=False)
#     CESS = models.CharField(max_length=100, null=True, blank=False)
#     total = models.CharField(max_length=100, null=True, blank=False)
#     status = models.CharField(max_length=100, null=True, blank=False)
#     amount_paid = models.CharField(max_length=100, null=True, blank=False)
#     balance = models.CharField(max_length=100, null=True, blank=False)
#     Dr_Cr = models.CharField(max_length=100, null=True, blank=False)
#     date_of_payment = models.CharField(max_length=100, null=True, blank=False)
#     private_notes = models.CharField(max_length=100, null=True, blank=False)
#     payments = models.CharField(max_length=100, null=True, blank=False)
#
#     def __str__(self):
#         return self.vendor_name
