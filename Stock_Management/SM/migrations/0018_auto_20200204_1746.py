# Generated by Django 2.2 on 2020-02-04 12:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SM', '0017_auto_20200204_1744'),
    ]

    operations = [
        migrations.RenameField(
            model_name='enquiryform',
            old_name='enquiry_ype',
            new_name='enquiry_type',
        ),
    ]
