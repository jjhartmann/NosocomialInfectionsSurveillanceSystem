# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patientinfo', '0003_auto_20150725_2039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patientinfo',
            name='Email',
            field=models.EmailField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='patientinfo',
            name='age',
            field=models.PositiveSmallIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='patientinfo',
            name='city',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='patientinfo',
            name='dateofbirth',
            field=models.DateField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='patientinfo',
            name='gender',
            field=models.CharField(max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='patientinfo',
            name='phone',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='patientinfo',
            name='postalcode',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='patientinfo',
            name='provice',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='patientinfo',
            name='streetadd',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
