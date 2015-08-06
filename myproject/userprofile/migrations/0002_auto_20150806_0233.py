# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='address',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='gender',
            field=models.CharField(max_length=1, null=True, choices=[(b'M', b'Male'), (b'F', b'Female')]),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='phone',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='profile_picture',
            field=models.ImageField(upload_to=b'static/profile_image', blank=True),
        ),
    ]
