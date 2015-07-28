# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patientinfo', '0002_auto_20150725_0832'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patientinfo',
            name='age',
            field=models.PositiveSmallIntegerField(),
        ),
    ]
