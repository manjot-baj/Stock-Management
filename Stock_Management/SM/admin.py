from django.contrib import admin
from .enquiry import *
from .dayBook import *
from .company_data import *
from .PO import *
from .invoice import *
from .amc import *
from .employee_data import *
from .service import *

admin.site.site_header = 'Storeck'
admin.site.site_title = 'Storeck'
admin.site.index_title = 'Storeck Administration'


@admin.register(CompanyDetail)
class CompanyDetailAdmin(admin.ModelAdmin):
    list_display = ['name', 'country', 'name', 'address', 'city', 'state', 'pin_code', 'phone',
                    'email_id', 'website', 'GSTIN', 'taxation_type', 'tax_inclusive', 'TIN', 'VAT', 'service_tax_no',
                    'CST_tin_no', 'PAN', 'additional_details', 'currency']
    list_filter = ['name']
    search_fields = ['name']


@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
    list_display = ['name', 'contact_Name', 'TIN', 'email', 'phone', 'billing_address',
                    'billing_zip', 'billing_city', 'billing_state', 'billing_country', 'shipping_address',
                    'shipping_zip', 'shipping_city', 'shipping_state', 'shipping_country', 'details', 'GSTIN']
    list_filter = ['name', 'phone', 'contact_Name']
    search_fields = ['name', 'phone', 'contact_Name']


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['name', 'contact_Name', 'TIN', 'email', 'phone', 'billing_address',
                    'billing_zip', 'billing_city', 'billing_state', 'billing_country', 'shipping_address',
                    'shipping_zip', 'shipping_city', 'shipping_state', 'shipping_country', 'details',
                    'GSTIN', 'PAN', 'balance']
    list_filter = ['name', 'phone', 'contact_Name']
    search_fields = ['name', 'phone', 'contact_Name']


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['join_date', 'name', 'type', 'job_profile', 'qualification', 'address', 'city', 'state',
                    'pin_code', 'country', 'mobile_no', 'email_id']
    list_filter = ['type', 'join_date', 'city', 'state']
    search_fields = ['name', 'type', 'join_date', 'mobile_no', 'email_id']


@admin.register(Enquiry)
class EnquiryAdmin(admin.ModelAdmin):
    list_display = ['enquiry_date', 'customer_type', 'first_name', 'last_name', 'enquiry_type', 'handled_by',
                    'product_name', 'startPrice', 'endPrice', 'mobile_no', 'whatsapp_no', 'email_id']
    list_select_related = ['customer_type', 'enquiry_type', 'handled_by']
    list_filter = ['customer_type', 'enquiry_date', 'handled_by']
    search_fields = ['first_name', 'enquiry_date', 'mobile_no']

@admin.register(EnquiryRecord)
class EnquiryRecordAdmin(admin.ModelAdmin):
     list_display = ['enquiryDetails', 'date', 'status', 'comments']
#     list_select_related = ['enquiryDetails','status', ]
#     list_filter = ['enquiryDetails', 'date', 'status', 'comments']
#     search_fields = ['enquiryDetails', 'date', 'status', 'comments']


@admin.register(DayBook)
class DayBookAdmin(admin.ModelAdmin):
    list_display = ['date', 'number', 'name', 'customer_type', 'customer_name', 'employee_name', 'vendor_name',
                    'status', 'credit_amount', 'debit_amount']
    list_select_related = ['customer_name', 'employee_name', 'vendor_name']
    list_filter = ['customer_type', 'status', 'date']
    search_fields = ['customer_type', 'status', 'date', 'number']


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['date', 'service_number', 'client', 'service_type', 'status']
    list_select_related = ['client', 'service_type']
    list_filter = ['service_number', 'status', 'date']
    search_fields = ['service_number', 'status', 'date', 'client']


@admin.register(AMC)
class AMCAdmin(admin.ModelAdmin):
    list_display = ['start_date', 'number', 'client_name', 'product_types', 'end_date']
    list_select_related = ['client_name', 'product_types']
    list_filter = ['start_date', 'number', 'client_name', 'product_types', 'end_date']
    search_fields = ['start_date', 'number', 'client_name', 'product_types']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'unit_price', 'u_o_m', 'quantity', 'product_type', 'purchase_rate',
                    'purchase_rate_currency', 'h_s_n_or_s_a_c', 's_k_u', 'tax', 'c_e_s_s_percent', 'c_e_s_s']
    list_filter = ['name', 'product_type']
    search_fields = ['name', 'product_type']


# @admin.register(Invoice)
# class InvoiceAdmin(admin.ModelAdmin):
#     list_display = ['client_name', 'invoice_no', 'v_a_t_no', 'p_o_no', 'issue_date', 'due_date', 'amount_before_tax',
#                     'discount', 'tax', 'total', 'status', 'amount_paid', 'balance', 'dr_or_cr', 'date_of_payment',
#                     'invoice_type']
#     list_select_related = ['client_name', 'p_o_no']
#     list_filter = ['client_name', 'invoice_no', 'issue_date', 'due_date', 'status', 'invoice_type']
#     search_fields = ['client_name', 'invoice_no', 'issue_date', 'due_date', 'status', 'invoice_type']
#
#
# @admin.register(Quotation)
# class QuotationAdmin(admin.ModelAdmin):
#     list_display = ['client_name', 'estimate_no', 'p_o_no', 'issue_date', 'valid_until', 'amount',
#                     'tax', 'discount', 'total', 'invoiced', 'quotation_type']
#     list_select_related = ['client_name', 'p_o_no']
#     list_filter = ['client_name', 'issue_date', 'valid_until', 'invoiced']
#     search_fields = ['client_name', 'issue_date', 'valid_until', 'invoiced']
#
#
# @admin.register(POData)
# class PODataAdmin(admin.ModelAdmin):
#     list_display = ['purchase_order_no', 'vendor_name', 'GSTIN', 'issue_date', 'valid_until', 'amount',
#                     'tax', 'CGST', 'SGST', 'IGST', 'CESS', 'total', 'billed']
#     list_select_related = ['vendor_name']
#     list_filter = ['purchase_order_no', 'vendor_name', 'issue_date', 'valid_until', 'billed']
#     search_fields = ['purchase_order_no', 'vendor_name']
#
#
# @admin.register(Bill)
# class BillAdmin(admin.ModelAdmin):
#     list_display = ['bill_no', 'vendor_name', 'GSTIN', 'invoice_no', 'po_no', 'issue_date', 'due_date',
#                     'shipping_charges', 'amount_before_tax', 'discount', 'amount_before_tax_after_discount',
#                     'tax', 'CGST', 'SGST', 'IGST', 'CESS', 'total',
#                     'status', 'amount_paid', 'balance',
#                     'Dr_Cr', 'date_of_payment']
#     list_select_related = ['vendor_name', 'invoice_no', 'po_no']
#     list_filter = ['vendor_name', 'issue_date', 'due_date', 'status']
#     search_fields = ['bill_no', 'vendor_name', 'invoice_no', 'po_no']


admin.site.register(CostumerType)
admin.site.register(EnquiryType)
admin.site.register(Product_type)
admin.site.register(ServiceType)
