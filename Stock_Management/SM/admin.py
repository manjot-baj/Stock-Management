from django.contrib import admin
from .enquiry import *
from .dayBook import *
from .company_data import *
from .PO import *
from .product import *
from .amc import *
from .employee_data import *
from .service import *
from django.urls import path, reverse
from django.utils.html import format_html
from SMdashboard import reports
from .quotation import Quotation, Quotation_lines
from .invoice import Invoice, InvoiceLines
from .bill_of_supply import Bill_of_supply, Bill_of_supply_Lines
from .payment_document import Payment_document

admin.site.site_header = 'Storeck'
admin.site.site_title = 'Storeck'
admin.site.index_title = 'Storeck Administration'


@admin.register(CompanyDetail)
class CompanyDetailAdmin(admin.ModelAdmin):
    list_display = ['name', 'country', 'address', 'city', 'state', 'pin_code', 'phone',
                    'email_id', 'website', 'GSTIN', 'taxation_type', 'tax_inclusive', 'TIN', 'VAT', 'service_tax_no',
                    'CST_tin_no', 'PAN', 'additional_details', 'currency']
    list_filter = ['name']
    search_fields = ['name']


@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
    list_display = ['name', 'contact_Name', 'TIN', 'email', 'phone', 'billing_address',
                    'billing_zip', 'billing_city', 'billing_state', 'billing_country', 'shipping_address',
                    'shipping_zip', 'shipping_city', 'shipping_state', 'shipping_country', 'details', 'GSTIN',
                    'company']
    list_filter = ['name', 'phone', 'contact_Name', 'company']
    search_fields = ['name', 'phone', 'contact_Name', 'company']


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['name', 'contact_Name', 'TIN', 'email', 'phone', 'billing_address',
                    'billing_zip', 'billing_city', 'billing_state', 'billing_country', 'shipping_address',
                    'shipping_zip', 'shipping_city', 'shipping_state', 'shipping_country', 'details',
                    'GSTIN', 'PAN', 'balance', 'company']
    list_filter = ['name', 'phone', 'contact_Name', 'company']
    search_fields = ['name', 'phone', 'contact_Name', 'company']


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['join_date', 'name', 'type', 'job_profile', 'qualification', 'address', 'city', 'state',
                    'pin_code', 'country', 'mobile_no', 'email_id', 'company']
    list_filter = ['type', 'join_date', 'city', 'state', 'company']
    search_fields = ['name', 'type', 'join_date', 'mobile_no', 'email_id', 'company']


@admin.register(Enquiry)
class EnquiryAdmin(admin.ModelAdmin):
    list_display = ['enquiry_date', 'customer_type', 'first_name', 'last_name', 'enquiry_type', 'create_user',
                    'write_user',
                    'product_name', 'price', 'mobile_no', 'email_id', 'create_user',
                    'write_user', 'company']
    list_select_related = ['customer_type', 'enquiry_type']
    list_filter = ['customer_type', 'enquiry_date', 'create_user',
                   'write_user', 'company']
    search_fields = ['first_name', 'enquiry_date', 'mobile_no', 'company']


@admin.register(EnquiryRecord)
class EnquiryRecordAdmin(admin.ModelAdmin):
    list_display = ['enquiryDetails', 'date', 'status', 'comments']
    list_select_related = ['enquiryDetails']
    list_filter = ['enquiryDetails', 'date', 'status']
    search_fields = ['date', 'status']


@admin.register(ServiceRecord)
class ServiceRecordAdmin(admin.ModelAdmin):
    list_display = ['service_number', 'date', 'status', 'comment']
    list_select_related = ['service_number']
    list_filter = ['service_number', 'date', 'status']
    search_fields = ['date', 'status']


@admin.register(DayBook)
class DayBookAdmin(admin.ModelAdmin):
    list_display = ['date', 'number', 'name', 'customer_type', 'customer_name', 'employee_name', 'vendor_name',
                    'status', 'credit_amount', 'debit_amount', 'company']
    list_select_related = ['customer_name', 'employee_name', 'vendor_name']
    list_filter = ['customer_type', 'status', 'date', 'company']
    search_fields = ['customer_type', 'status', 'date', 'number', 'company']


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['date', 'service_number', 'client', 'service_type', 'company']
    list_select_related = ['client', 'service_type']
    list_filter = ['service_number', 'date', 'company']
    search_fields = ['service_number', 'date', 'client', 'company']


@admin.register(AMC)
class AMCAdmin(admin.ModelAdmin):
    list_display = ['start_date', 'number', 'client_name', 'end_date', 'company']
    list_filter = ['start_date', 'number', 'client_name', 'end_date', 'company']
    search_fields = ['start_date', 'number', 'client_name', 'company']


class QuotationAdminInline(admin.TabularInline):
    model = Quotation_lines
    fieldsets = [
        ('Quotation Lines', {'fields': (
            ('product', 'uom', 'quantity', 'unit_price', 'tax'),
        )}),
    ]
    extra = 1


@admin.register(Quotation)
class QuotationAdmin(admin.ModelAdmin):
    list_display = ['issue_date', 'number', 'client_name', 'due_date']
    search_fields = ['number']
    inlines = [QuotationAdminInline]

    fieldsets = [
        ('Quotation Details', {'fields': (
            ('issue_date', 'due_date', 'number'),
            ('client_name', 'ship_to'),
            ('grand_total'),
            ('company'),
        ), }),
    ]


class InvoiceAdminInline(admin.TabularInline):
    model = InvoiceLines
    fieldsets = [
        ('InvoiceLines', {'fields': (
            ('product', 'description', 'uom', 'quantity', 'unit_price', 'discount', 'tax'),
        )}),
    ]
    extra = 1


@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ['client_name', 'ship_to', 'number', 'issue_date', 'grand_total']
    search_fields = ['number', 'client_name']
    inlines = [InvoiceAdminInline]

    fieldsets = [
        ('Invoice Order Details', {'fields': (
            ('client_name', 'ship_to'),
            ('number', 'issue_date'),
            ('grand_total'),
        ), }),
    ]


class Bill_of_supplyAdminInline(admin.TabularInline):
    model = Bill_of_supply_Lines
    fieldsets = [
        ('BillLines', {'fields': (
            ('product', 'description', 'uom', 'quantity', 'unit_price', 'discount'),
        )}),
    ]
    extra = 1


@admin.register(Bill_of_supply)
class Bill_of_supplyAdmin(admin.ModelAdmin):
    list_display = ['client_name', 'ship_to', 'number', 'issue_date', 'grand_total']
    search_fields = ['number', 'client_name']
    inlines = [Bill_of_supplyAdminInline]

    fieldsets = [
        ('Bill_of_supply Order Details', {'fields': (
            ('client_name', 'ship_to'),
            ('number', 'issue_date'),
            ('grand_total'),
        ), }),
    ]


admin.site.register(CostumerType)
admin.site.register(EnquiryType)
admin.site.register(ServiceType)
admin.site.register(AMCRecord)
admin.site.register(Product)
admin.site.register(ServiceStoreData)
admin.site.register(Payment_document)
