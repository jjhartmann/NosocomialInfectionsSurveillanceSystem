# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patientinfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('firstname', models.CharField(max_length=20)),
                ('lastname', models.CharField(max_length=20)),
                ('dateofbirth', models.DateField(max_length=20)),
                ('gender', models.CharField(max_length=6)),
                ('age', models.FloatField()),
                ('Email', models.EmailField(max_length=50)),
                ('phone', models.CharField(max_length=20)),
                ('streetadd', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=20)),
                ('provice', models.CharField(max_length=20)),
                ('postalcode', models.CharField(max_length=20)),
            ],
        ),
    ]
