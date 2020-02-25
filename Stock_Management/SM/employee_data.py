from django.contrib.auth.models import User
from django.db import models
from .models import BaseModel


class Employee(BaseModel):
    id = models.AutoField(primary_key=True)
    photo = models.ImageField(null=True, blank=True)
    join_date = models.DateField(null=True, blank=False)
    name = models.CharField(max_length=100, null=True, blank=False)
    address = models.TextField(max_length=200, null=True, blank=False)
    city = models.CharField(max_length=100, null=True, blank=False)
    state = models.CharField(max_length=100, null=True, blank=False)
    pin_code = models.CharField(max_length=100, null=True, blank=False)
    country = models.CharField(max_length=100, null=True, blank=False)
    mobile_no = models.CharField(max_length=100, null=True, blank=False)
    email_id = models.CharField(max_length=100, null=True, blank=False)
    user = models.ForeignKey(User, related_name='employee_user', on_delete=models.SET_NULL, null=True, blank=True)
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

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        from .utils import encode
        # post_str = encode()
        if self.pk is None:
            usr_name = self.name.replace(" ", "")
            res = super(Employee, self).save(force_insert=False, force_update=False, using=None, update_fields=None)
            user_obj = User.objects.create_user(
                username='USR_' + usr_name, password=None, is_staff=True, email=self.email_id,
                first_name=self.name
            )
            user_data = list(User.objects.filter(username=user_obj).values('pk'))
            user_data[0].get('pk')
            print(user_data[0].get('pk'))
            self.user_id = user_data[0].get('pk')
        else:
            res = super(Employee, self).save(force_insert=False, force_update=False, using=None, update_fields=None)
        return res
