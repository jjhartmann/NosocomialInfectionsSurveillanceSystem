# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Patientinfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('firstname', models.CharField(max_length=20)),
                ('lastname', models.CharField(max_length=20)),
                ('date_of_birth', models.DateField(max_length=20, null=True, blank=True)),
                ('gender', models.CharField(blank=True, max_length=1, null=True, choices=[(b'M', b'Male'), (b'F', b'Female')])),
                ('age', models.PositiveSmallIntegerField(null=True, blank=True)),
                ('email', models.EmailField(max_length=50, null=True, blank=True)),
                ('phone', models.CharField(max_length=20, null=True, blank=True)),
                ('street_address', models.CharField(max_length=20, null=True, blank=True)),
                ('city', models.CharField(max_length=20, null=True, blank=True)),
                ('provice', models.CharField(max_length=20, null=True, blank=True)),
                ('postal_code', models.CharField(max_length=20, null=True, blank=True)),
                ('patient_picture', models.FileField(upload_to=b'patient_picture/', blank=True)),
                ('patient_data', models.FileField(upload_to=b'patient_data/', blank=True)),
                ('doctor', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
