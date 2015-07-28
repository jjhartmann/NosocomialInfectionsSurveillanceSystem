# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patientinfo', '0009_auto_20150726_0520'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patientinfo',
            old_name='Email',
            new_name='email',
        ),
    ]
