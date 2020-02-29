from django.db import models
from django.utils import timezone
from .models import BaseModel
from .company_data import Client
import random


def random_string():
    return str(random.randint(10000, 99999))


class AMC(BaseModel):
    number = models.CharField(default=random_string, max_length=50, null=True, blank=False)
    client_name = models.ForeignKey(Client, on_delete=models.CASCADE, null=True, blank=False)
    description = models.TextField(null=True, blank=True)
    start_date = models.DateTimeField(default=timezone.now, null=True, blank=False)
    end_date = models.DateTimeField(null=True, blank=False)

    def __str__(self):
        return self.number
