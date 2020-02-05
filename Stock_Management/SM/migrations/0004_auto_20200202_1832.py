<<<<<<< HEAD
# Generated by Django 2.2 on 2020-02-02 13:02
=======
# Generated by Django 2.2.7 on 2020-02-02 13:02
>>>>>>> ba5ba54c4b9a0a8bca9fd8ecc1d659c6e3bf24ec

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('SM', '0003_auto_20200202_1750'),
    ]

    operations = [
        migrations.AddField(
            model_name='costumertype',
            name='create_date',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, editable=False, null=True),
        ),
        migrations.AddField(
            model_name='costumertype',
            name='create_user',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_by_sm_costumertype_related', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='costumertype',
            name='write_date',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, editable=False, null=True),
        ),
        migrations.AddField(
            model_name='costumertype',
            name='write_user',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='written_by_sm_costumertype_related', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='daybook',
            name='create_date',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, editable=False, null=True),
        ),
        migrations.AddField(
            model_name='daybook',
            name='create_user',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_by_sm_daybook_related', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='daybook',
            name='write_date',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, editable=False, null=True),
        ),
        migrations.AddField(
            model_name='daybook',
            name='write_user',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='written_by_sm_daybook_related', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='enquiryform',
            name='create_date',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, editable=False, null=True),
        ),
        migrations.AddField(
            model_name='enquiryform',
            name='create_user',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_by_sm_enquiryform_related', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='enquiryform',
            name='write_date',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, editable=False, null=True),
        ),
        migrations.AddField(
            model_name='enquiryform',
            name='write_user',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='written_by_sm_enquiryform_related', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='enquirytype',
            name='create_date',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, editable=False, null=True),
        ),
        migrations.AddField(
            model_name='enquirytype',
            name='create_user',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_by_sm_enquirytype_related', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='enquirytype',
            name='write_date',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, editable=False, null=True),
        ),
        migrations.AddField(
            model_name='enquirytype',
            name='write_user',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='written_by_sm_enquirytype_related', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='enquiryform',
            name='enquiryDate',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True),
        ),
    ]
