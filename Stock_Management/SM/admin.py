from django.contrib import admin
from .enquiry import *
from .dayBook import *

admin.site.register(CostumerType)
admin.site.register(EnquiryType)
admin.site.register(EnquiryForm)
admin.site.register(DayBook)