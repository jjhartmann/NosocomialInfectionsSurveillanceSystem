# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patientinfo', '0011_auto_20150806_0233'),
    ]

    operations = [
        migrations.AddField(
            model_name='patientinfo',
            name='patient_data',
            field=models.FileField(upload_to=b'patient_data/', blank=True),
        ),
        migrations.AddField(
            model_name='patientinfo',
            name='patient_picture',
            field=models.FileField(upload_to=b'patient_image/', blank=True),
        ),
    ]
