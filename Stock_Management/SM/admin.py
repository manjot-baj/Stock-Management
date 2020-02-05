from django.contrib import admin
from .enquiry import *
from .dayBook import *
from .company_data import *
from .purchaseOrder import *

admin.site.register(CostumerType)
admin.site.register(EnquiryType)
admin.site.register(EnquiryForm)
admin.site.register(CompanyDetail)
admin.site.register(DayBook)
admin.site.register(Vendor)
admin.site.register(Client)
admin.site.register(PurchaseOrder)
admin.site.register(Bill)


