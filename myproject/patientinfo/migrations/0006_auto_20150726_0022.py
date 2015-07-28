# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patientinfo', '0005_auto_20150726_0019'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patientinfo',
            old_name='address',
            new_name='streetadd',
        ),
    ]
