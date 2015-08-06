# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patientinfo', '0010_auto_20150728_0248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patientinfo',
            name='gender',
            field=models.CharField(max_length=1, null=True, choices=[(b'M', b'Male'), (b'F', b'Female')]),
        ),
    ]
