from django.contrib import admin
from .enquiry import *
from .dayBook import *
from .company_data import *
from .purchaseOrder import *
from .invoice import *
from .amc import *
from .employee_data import *

admin.site.site_header = 'Storeck'
admin.site.site_title = 'Storeck'
admin.site.index_title = 'Storeck Administration'

admin.site.register(CostumerType)
admin.site.register(EnquiryType)
admin.site.register(EnquiryForm)
admin.site.register(CompanyDetail)
admin.site.register(DayBook)
admin.site.register(Vendor)
admin.site.register(Client)
admin.site.register(PurchaseOrder)
admin.site.register(Bill)
admin.site.register(Product)
admin.site.register(Invoice)
admin.site.register(Quotation)
admin.site.register(AMC)
admin.site.register(Product_type)
admin.site.register(Employee)
