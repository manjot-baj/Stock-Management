from django.contrib import admin
from .enquiry import *
from .dayBook import *
from .invoice import *
admin.site.register(CostumerType)
admin.site.register(EnquiryType)
admin.site.register(EnquiryForm)
admin.site.register(DayBook)
admin.site.register(Product)
admin.site.register(invoice)
admin.site.register(quotation)