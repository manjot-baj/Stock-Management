from django.db import models
from django.utils import timezone


class CostumerType(models.Model):
    customerType = models.CharField(max_length=100)

    def __str__(self):
        return self.customerType

class EnquiryType(models.Model):
    enquiryType = models.CharField(max_length=100, null=True, blank=False)

    def __str__(self):
        return self.enquiryType

class EnquiryForm(models.Model):
    firstName = models.CharField(max_length=100, null=True, blank=False,)
    lastName = models.CharField(max_length=100, null=True, blank=False,)
    customerType = models.ForeignKey(CostumerType, on_delete=models.CASCADE, null=True, blank=False)
    address = models.TextField(max_length=200, null=True, blank=False,)
    enquiryDate = models.DateTimeField(default=timezone.now, null=True, blank=True, editable=False)
    handledBy = models.CharField(max_length=100, null=True, blank=False,)
    enquiryType = models.ForeignKey(EnquiryType, on_delete=models.CASCADE, null=True, blank=False)

    enquiry_Name = models.CharField(max_length=100, null=True, blank=True)
    startPrice = models.CharField(max_length=100, null=True, blank=True)
    endPrice = models.CharField(max_length=100, null=True, blank=True)

    mobile_No = models.CharField(max_length=100, null=True, blank=False,)
    whatsUP_No = models.CharField(max_length=100, null=True, blank=True, )
    contact_No = models.CharField(max_length=100, null=True, blank=True, )
    email_Id = models.CharField(max_length=100, null=True, blank=True, )

    def __str__(self):
        return 'Name : {0},  Enquiry_For:{1},  Date : {2}'.format(self.firstName, self.enquiryType, self.enquiryDate)

