# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-15 23:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_project_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='video',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]