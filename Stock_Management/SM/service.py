from django.utils import timezone

from django.db import models
from django.utils.crypto import random
from .company_data import *

from .models import BaseModel


def random_string():
    return str(random.randint(10000, 99999))


class ServiceType(BaseModel):
    name = models.CharField(max_length=100, null=True, blank=True)
    def __str__(self):
        return self.name


class Service(BaseModel):
    service_number = models.CharField(max_length=50, default=random_string, null=True, blank=True)
    date = models.DateTimeField(default=timezone.now, null=True, blank=False)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, null=True, blank=False)
    service_type = models.ForeignKey(ServiceType, on_delete=models.CASCADE, null=True, blank=False)
    description = models.TextField(max_length=200, null=True, blank=True)
    photo = models.ImageField(upload_to='uploads/', null=True, blank=True)
    status_type = (
        ("Start", "start"),
        ("Pending", "pending"),
        ("On progress", "on progress"),
        ("Completed", "completed")
    )

    status = models.CharField(max_length=100, choices=status_type, default='Start')

    def __str__(self):
        return self.service_number
