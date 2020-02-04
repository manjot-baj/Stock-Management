from django.db import models
from django.utils import timezone
from .models import BaseModel
import random


def random_string():
    return str(random.randint(10000, 99999))


class product_type(BaseModel):
    product_type = models.CharField(max_length=100)

    def __str__(self):
        return self.product_type


class AMC(BaseModel):
    number = models.CharField(default=random_string, max_length=50, null=True)
    client_name = models.CharField(max_length=100, null=True, blank=False)
    product = models.CharField(max_length=100, null=True, blank=False)
    product_types = models.ForeignKey(product_type, on_delete=models.CASCADE, null=True, blank=False)
    description = models.TextField(null=True, blank=False)
    product_type = models.CharField(max_length=100, null=True, blank=False)
    start_date = models.DateTimeField(default=timezone.now, null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.number
