# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patientinfo', '0004_auto_20150725_2156'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patientinfo',
            name='streetadd',
        ),
        migrations.AddField(
            model_name='patientinfo',
            name='address',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
