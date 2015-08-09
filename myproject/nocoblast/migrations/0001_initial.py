# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FASTATable',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('desc', models.TextField(null=True)),
                ('fasta', models.TextField(null=True)),
            ],
        ),
    ]
