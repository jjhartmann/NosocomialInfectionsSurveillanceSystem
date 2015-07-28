# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patientinfo', '0007_auto_20150726_0035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patientinfo',
            name='gender',
            field=models.CharField(max_length=3, null=True, choices=[(b'MALE', b'Male'), (b'FEMALE', b'Female'), (b'OTHER', b'Other')]),
        ),
    ]