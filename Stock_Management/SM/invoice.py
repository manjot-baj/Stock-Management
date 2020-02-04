from django.db import models
from django.utils import timezone
from .models import BaseModel


class Product(BaseModel):
    name = models.CharField(max_length=100, null=True, blank=False)
    unit_price = models.CharField(max_length=100, null=True, blank=False)
    u_o_m = models.CharField(max_length=100, null=True, blank=False)
    quantity = models.CharField(max_length=100, null=True, blank=False)
    description = models.TextField(null=True, blank=False)
    product_type = models.CharField(max_length=100, null=True, blank=False)
    purchase_rate = models.CharField(max_length=100, null=True, blank=False)
    purchase_rate_currency = models.CharField(max_length=100, null=True, blank=False)
    h_s_n_or_s_a_c = models.CharField(max_length=100, null=True, blank=False)
    s_k_u = models.CharField(max_length=100, null=True, blank=False)
    tax = models.CharField(max_length=100, null=True, blank=False)
    c_e_s_s_percent = models.CharField(max_length=100, null=True, blank=False)
    c_e_s_s = models.CharField(max_length=100, null=True, blank=False)

    def __str__(self):
        return self.name


class invoice(BaseModel):
    name = models.CharField(max_length=100, null=True, blank=False)
    v_a_t_no = models.CharField(max_length=100, null=True, blank=False)
    invoice_no = models.CharField(max_length=100, null=True, blank=False)
    p_o_number = models.CharField(max_length=100, null=True, blank=False)
    p_o_date = models.CharField(max_length=100, null=True, blank=False)
    issue_date = models.CharField(max_length=100, null=True, blank=False)
    due_date = models.CharField(max_length=100, null=True, blank=False)
    amount_before_tax = models.CharField(max_length=100, null=True, blank=False)
    discount = models.CharField(max_length=100, null=True, blank=False)
    tax = models.CharField(max_length=100, null=True, blank=False)
    total = models.CharField(max_length=100, null=True, blank=False)
    status = models.CharField(max_length=100, null=True, blank=False)
    amount_paid = models.CharField(max_length=100, null=True, blank=False)
    balance = models.CharField(max_length=100, null=True, blank=False)
    dr_or_cr = models.CharField(max_length=100, null=True, blank=False)
    date_of_payment = models.CharField(max_length=100, null=True, blank=False)
    invoice_type = models.CharField(max_length=100, null=True, blank=False)
    private_note = models.TextField(null=True, blank=False)
    payments = models.TextField(null=True, blank=False)

    def __str__(self):
        return self.name


class quotation(BaseModel):
    client_name = models.CharField(max_length=100, null=True, blank=False)
    estimate_no = models.CharField(max_length=100, null=True, blank=False)
    p_o_no = models.CharField(max_length=100, null=True, blank=False)
    issue_date = models.CharField(max_length=100, null=True, blank=False)
    valid_until = models.CharField(max_length=100, null=True, blank=False)
    amount = models.CharField(max_length=100, null=True, blank=False)
    tax = models.CharField(max_length=100, null=True, blank=False)
    discount = models.CharField(max_length=100, null=True, blank=False)
    total = models.CharField(max_length=100, null=True, blank=False)
    invoiced = models.CharField(max_length=100, null=True, blank=False)
    quotation_type = models.CharField(max_length=100, null=True, blank=False)

    def __str__(self):
        return self.client_name