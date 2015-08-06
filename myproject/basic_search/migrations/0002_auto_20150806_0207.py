# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basic_search', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='influenza_faa',
            name='fasta_protein_description',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='influenza_fna',
            name='fasta_nucleotide_description',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
