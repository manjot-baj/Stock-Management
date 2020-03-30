from django.contrib import admin
from .enquiry import *
from .dayBook import *
from .company_data import *
from .PO import *
from .invoice import *
from .amc import *
from .employee_data import *
from .service import *
from django.urls import path, reverse
from django.utils.html import format_html
from SMdashboard import reports

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


admin.site.register(CostumerType)
admin.site.register(EnquiryType)
admin.site.register(ServiceType)
admin.site.register(AMCRecord)
admin.site.register(Product)
admin.site.register(ServiceStoreData)
