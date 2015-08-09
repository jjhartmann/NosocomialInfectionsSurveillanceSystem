# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patientinfo', '0012_auto_20150806_0347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patientinfo',
            name='patient_picture',
            field=models.FileField(upload_to=b'patient_picture/', blank=True),
        ),
    ]
