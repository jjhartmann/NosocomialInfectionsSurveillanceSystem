# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patientinfo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patientinfo',
            name='age',
            field=models.PositiveSmallIntegerField(max_length=3),
        ),
    ]
