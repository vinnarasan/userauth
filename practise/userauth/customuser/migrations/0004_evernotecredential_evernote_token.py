# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-23 20:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customuser', '0003_auto_20160622_1843'),
    ]

    operations = [
        migrations.AddField(
            model_name='evernotecredential',
            name='evernote_token',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
