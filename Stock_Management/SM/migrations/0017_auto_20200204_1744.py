# Generated by Django 2.2 on 2020-02-04 12:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SM', '0016_auto_20200204_1716'),
    ]

    operations = [
        migrations.RenameField(
            model_name='enquiryform',
            old_name='contact_No',
            new_name='contact_no',
        ),
        migrations.RenameField(
            model_name='enquiryform',
            old_name='customerType',
            new_name='customer_type',
        ),
        migrations.RenameField(
            model_name='enquiryform',
            old_name='enquiryDate',
            new_name='enquiry_date',
        ),
        migrations.RenameField(
            model_name='enquiryform',
            old_name='enquiryType',
            new_name='enquiry_ype',
        ),
        migrations.RenameField(
            model_name='enquiryform',
            old_name='firstName',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='enquiryform',
            old_name='handledBy',
            new_name='handled_by',
        ),
        migrations.RenameField(
            model_name='enquiryform',
            old_name='lastName',
            new_name='last_name',
        ),
        migrations.RenameField(
            model_name='enquiryform',
            old_name='mobile_No',
            new_name='mobile_no',
        ),
        migrations.RenameField(
            model_name='enquiryform',
            old_name='whatsUP_No',
            new_name='product_name',
        ),
        migrations.RenameField(
            model_name='enquiryform',
            old_name='enquiry_Name',
            new_name='whatsapp_no',
        ),
    ]
