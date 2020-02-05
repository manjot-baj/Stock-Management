from django.db import models
from django.utils import timezone
from .models import BaseModel


class CostumerType(BaseModel):
    customerType = models.CharField(max_length=100)

    def __str__(self):
        return self.customerType


class EnquiryType(BaseModel):
    enquiryType = models.CharField(max_length=100, null=True, blank=False)

    def __str__(self):
        return self.enquiryType


class EnquiryForm(BaseModel):
    first_name = models.CharField(max_length=100, null=True, blank=False, )
    last_name = models.CharField(max_length=100, null=True, blank=False, )
    customer_type = models.ForeignKey(CostumerType, on_delete=models.CASCADE, null=True, blank=False)
    address = models.TextField(max_length=200, null=True, blank=False, )
    enquiry_date = models.DateTimeField(default=timezone.now, null=True, blank=True)
    handled_by = models.CharField(max_length=100, null=True, blank=False, )
    enquiry_type = models.ForeignKey(EnquiryType, on_delete=models.CASCADE, null=True, blank=False)

    product_name = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True,blank=False)
    startPrice = models.CharField(max_length=100, null=True, blank=True)
    endPrice = models.CharField(max_length=100, null=True, blank=True)

    mobile_no = models.CharField(max_length=100, null=True, blank=False, )
    whatsapp_no = models.CharField(max_length=100, null=True, blank=True, )
    contact_no = models.CharField(max_length=100, null=True, blank=True, )
    email_Id = models.CharField(max_length=100, null=True, blank=True, )

    def __str__(self):
        return 'Name : {0},  Enquiry_For:{1},  Date : {2}'.format(self.first_name, self.enquiry_type, self.enquiry_date)
