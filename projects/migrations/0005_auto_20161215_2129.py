# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-15 21:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_auto_20161215_1853'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='goal',
            field=models.CharField(default=1, max_length=140),
        ),
    ]