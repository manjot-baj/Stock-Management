# from django.db import models
# from .models import BaseModel
# from .company_data import Vendor
#
#
# class POData(BaseModel):
#     purchase_order_no = models.CharField(max_length=100, null=True, blank=False)
#     vendor_name = models.ForeignKey(Vendor, on_delete=models.CASCADE, null=True, blank=True)
#     GSTIN = models.CharField(max_length=100, null=True, blank=False)
#     issue_date = models.CharField(max_length=100, null=True, blank=False)
#     valid_until = models.CharField(max_length=100, null=True, blank=False)
#     amount = models.CharField(max_length=100, null=True, blank=False)
#     tax = models.CharField(max_length=100, null=True, blank=False)
#     CGST = models.CharField(max_length=100, null=True, blank=False)
#     SGST = models.CharField(max_length=100, null=True, blank=False)
#     IGST = models.CharField(max_length=100, null=True, blank=False)
#     CESS = models.CharField(max_length=100, null=True, blank=False)
#     total = models.CharField(max_length=100, null=True, blank=False)
#     billed = models.CharField(max_length=100, null=True, blank=False)
#     advanced_payments = models.CharField(max_length=100, null=True, blank=False)
#
#     def __str__(self):
#         return self.purchase_order_no
#
