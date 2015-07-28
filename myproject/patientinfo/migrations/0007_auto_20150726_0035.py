# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patientinfo', '0006_auto_20150726_0022'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patientinfo',
            old_name='dateofbirth',
            new_name='date_of_birth',
        ),
        migrations.RenameField(
            model_name='patientinfo',
            old_name='postalcode',
            new_name='postal_code',
        ),
        migrations.RenameField(
            model_name='patientinfo',
            old_name='streetadd',
            new_name='street_address',
        ),
    ]
