# Generated by Django 2.2 on 2020-02-04 13:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('SM', '0020_purchaseorder'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(blank=True, default=django.utils.timezone.now, editable=False, null=True)),
                ('write_date', models.DateTimeField(blank=True, default=django.utils.timezone.now, editable=False, null=True)),
                ('name', models.CharField(max_length=100, null=True)),
                ('GSTIN', models.CharField(max_length=100, null=True)),
                ('bill_number', models.CharField(max_length=100, null=True)),
                ('invoice_number', models.CharField(max_length=100, null=True)),
                ('PO_number', models.CharField(max_length=100, null=True)),
                ('issue_date', models.CharField(max_length=100, null=True)),
                ('due_date', models.CharField(max_length=100, null=True)),
                ('shipping_charges', models.CharField(max_length=100, null=True)),
                ('amount_before_tax', models.CharField(max_length=100, null=True)),
                ('discount', models.CharField(max_length=100, null=True)),
                ('amount_before_tax_after_discount', models.CharField(max_length=100, null=True)),
                ('tax', models.CharField(max_length=100, null=True)),
                ('CGST', models.CharField(max_length=100, null=True)),
                ('SGST', models.CharField(max_length=100, null=True)),
                ('IGST', models.CharField(max_length=100, null=True)),
                ('CESS', models.CharField(max_length=100, null=True)),
                ('total', models.CharField(max_length=100, null=True)),
                ('status', models.CharField(max_length=100, null=True)),
                ('amount_paid', models.CharField(max_length=100, null=True)),
                ('balance', models.CharField(max_length=100, null=True)),
                ('Dr_Cr', models.CharField(max_length=100, null=True)),
                ('date_of_payment', models.CharField(max_length=100, null=True)),
                ('private_notes', models.CharField(max_length=100, null=True)),
                ('payments', models.CharField(max_length=100, null=True)),
                ('create_user', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_by_sm_bill_related', to=settings.AUTH_USER_MODEL)),
                ('write_user', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='written_by_sm_bill_related', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
