from django.db import models
# from django.utils import timezone
from .models import BaseModel

from .company_data import CompanyDetail, Client


class Product(BaseModel):
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
    Product_Type = (('Product', 'Product'), ('Service', 'Service'))
    type = models.CharField(max_length=50, choices=Product_Type, null=True, blank=False)
    sn = models.CharField(max_length=100, null=True, blank=True)
    uom = models.CharField(choices=TYPE_UOM, max_length=20, null=True, blank=False)
    sku = models.CharField(max_length=100, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=False)
    description = models.TextField(null=True, blank=True)
    hsn = models.CharField(max_length=100, null=True, blank=True)
    sac = models.CharField(max_length=100, null=True, blank=True)
    unit_price = models.FloatField(null=True, blank=False, default=0.0)
    purchase_rate = models.FloatField(null=True, blank=True, default=0.0)
    tax = models.CharField(choices=Tax_Type, max_length=50, null=True, blank=False)
    company = models.ForeignKey(CompanyDetail, on_delete=models.SET_NULL, null=True, blank=False)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'product'
        verbose_name_plural = 'Product'

# class Invoice(BaseModel):
#     client_name = models.ForeignKey(Client, on_delete=models.CASCADE, null=True, blank=True)
#     product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
#     #     v_a_t_no = models.CharField(max_length=100, null=True, blank=False)
#     invoice_no = models.CharField(max_length=100, null=True, blank=False)
#     # p_o_no = models.ForeignKey(POData, on_delete=models.CASCADE, null=True, blank=True)
#     issue_date = models.DateTimeField()
#     due_date = models.DateTimeField()
#     amount = models.FloatField(null=True, blank=True, default=0.0)
#     #     discount = models.CharField(max_length=100, null=True, blank=False)
#     Tax_Type = (
#         ('1', '1% GST'),
#         ('3', '3% GST'),
#         ('5', '5% GST'),
#         ('12', '12% GST'),
#         ('18', '18% GST'),
#         ('28', '28% GST'),
#     )
#     tax = models.CharField(choices=Tax_Type, max_length=50, null=True, blank=False)
#
#     total = models.FloatField(null=True, blank=True, default=0.0)
#     status = (
#         ('Paid', 'Paid'),
#         ('Unpaid', 'Unpaid'),
#         ('Partial', 'Partial'),
#         ('Overdue', 'Overdue'),
#         ('Unpaid/Partial', 'Unpaid/Partial'),
#
#     )
#     status = models.CharField(max_length=50, choices=status, null=True, blank=False)
#     amount_paid = models.FloatField(null=True, blank=True, default=0.0)
#     balance = models.FloatField(null=True, blank=True, default=0.0)
#     creditDebit = (
#         ("Cr", "Cr"),
#         ("Dr", "Dr"),
#     )
#     dr_or_cr = models.CharField(max_length=20, choices=creditDebit, null=True, blank=False)
#     date_of_payment = models.DateTimeField()
#     type_of_invoice = (
#         ("GST Tax", "GST Tax"),
#         ("Bill of Supply", "Bill of Supply"),
#         ("Standard", "Standard"),
#         ("Tax", "Tax"),
#     )
#     type = models.CharField(max_length=30, choices=type_of_invoice, null=True, blank=False)
#     #     invoice_type = models.CharField(max_length=100, null=True, blank=False)
#     private_note = models.TextField(null=True, blank=False)
#     email = (
#         ("Yes", "Yes"),
#         ("No", "No"),
#     )
#     emailed = models.CharField(max_length=50, choices=email, null=True, blank=False)
#     ship_to = models.TextField(null=False, blank=False, max_length=250)
#     place_of_supply = models.CharField(null=False, blank=False, max_length=100)
#     document_number = models.CharField(null=True, blank=False, max_length=100)
#     payment_status = (
#         ("Cash", "Cash"),
#         ("Cash Memo", "Cash Memo"),
#         ("Credit Card", "Credit Card"),
#         ("Check", "Check"),
#         ("Cheque", "Cheque"),
#         ("Bank Transfer", "Bank Transfer"),
#         ("Pay Slip", "Pay Slip"),
#         ("Other", "Other"),
#     )
#     payment_type = models.CharField(max_length=50, choices=payment_status, null=True, blank=False)
#     description = models.TextField(null=True, blank=True)
#     TYPE_UOM = (
#         ('Boxes', 'Boxes'),
#         ('CFT', 'CFT'),
#         ('Centimerets', 'Centimerets'),
#         ('Cubic Meters', 'Cubic Meters'),
#         ('Gram', 'Gram'),
#         ('Hours', 'Hours'),
#         ('Inches', 'Inches'),
#         ('Killowgrams', 'Killowgrams'),
#         ('Piece', 'Piece'),
#     )
#     uom = models.CharField(choices=TYPE_UOM, max_length=20, null=True, blank=False)
#     unit_price = models.FloatField(null=True, blank=False, default=0.0)
#     quantity = models.PositiveIntegerField(default=1, null=True, blank=False)
#     hsn = models.CharField(max_length=100, null=True, blank=True)
#     sac = models.CharField(max_length=100, null=True, blank=True)
#
#
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
