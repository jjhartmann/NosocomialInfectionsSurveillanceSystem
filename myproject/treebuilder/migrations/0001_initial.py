# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TreebuilderFiles',
            fields=[
                ('user', models.CharField(max_length=100, serialize=False, primary_key=True)),
                ('newick_file', models.TextField(null=True)),
                ('phyloxml_file', models.TextField(null=True)),
            ],
        ),
    ]
