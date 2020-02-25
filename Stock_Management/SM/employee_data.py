from django.db import models
from .models import BaseModel


class Employee(BaseModel):
    photo = models.ImageField(null=True, blank=False)  # True
    join_date = models.DateField(null=True, blank=False)
    name = models.CharField(max_length=100, null=True, blank=False)
    address = models.TextField(max_length=200, null=True, blank=False)
    city = models.CharField(max_length=100, null=True, blank=False)
    state = models.CharField(max_length=100, null=True, blank=False)
    pin_code = models.CharField(max_length=100, null=True, blank=False)
    country = models.CharField(max_length=100, null=True, blank=False)
    mobile_no = models.CharField(max_length=100, null=True, blank=False)
    email_id = models.CharField(max_length=100, null=True, blank=False)
    qualification = models.TextField(null=True, blank=False)
    JobType = (
        ("Part Time", "Part Time"),
        ("Full Time", "Full Time"),
        ("Internship", "Internship"),
    )
    type = models.CharField(max_length=50, choices=JobType, null=True, blank=False)
    job_profile = models.CharField(max_length=100, null=True, blank=False)
    job_description = models.TextField(null=True, blank=False)

    def __str__(self):
        return self.name
