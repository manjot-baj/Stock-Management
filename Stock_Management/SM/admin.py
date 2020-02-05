from django.contrib import admin
from .enquiry import *
from .dayBook import *
from .invoice import *
from .amc import *

admin.site.site_header = 'Storeck'
admin.site.site_title = 'Storeck'
admin.site.index_title = 'Storeck Administration'

admin.site.register(CostumerType)
admin.site.register(EnquiryType)
admin.site.register(EnquiryForm)
admin.site.register(DayBook)
admin.site.register(Product)
admin.site.register(invoice)
admin.site.register(quotation)
admin.site.register(AMC)