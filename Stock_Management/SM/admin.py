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


@admin.register(EnquiryForm)
class EnquiryAdmin(admin.ModelAdmin):
    list_display = ['enquiry_date', 'customer_type', 'first_name', 'last_name', 'enquiry_type', 'product_name',
                    'startPrice', 'endPrice', 'mobile_no', 'whatsapp_no', 'email_Id']
    list_select_related = ['customer_type', 'enquiry_type']
    list_filter = ['customer_type', 'enquiry_date']
    search_fields = ['first_name', 'enquiry_date', 'mobile_no']


admin.site.register(CostumerType)
admin.site.register(EnquiryType)
admin.site.register(CompanyDetail)
admin.site.register(DayBook)
admin.site.register(Vendor)
admin.site.register(Client)
admin.site.register(POData)
admin.site.register(Bill)
admin.site.register(Product)
admin.site.register(Invoice)
admin.site.register(Quotation)
admin.site.register(AMC)
admin.site.register(Product_type)
admin.site.register(Employee)
admin.site.register(Service)
admin.site.register(ServiceType)

