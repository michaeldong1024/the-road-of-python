# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2019-08-07 06:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='addr',
            field=models.CharField(default='China', max_length=32),
            preserve_default=False,
        ),
    ]
