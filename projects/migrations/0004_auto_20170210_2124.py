# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-02-10 21:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_auto_20170210_2117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='status',
            field=models.CharField(blank=True, choices=[('EN REVISIÓN', 'EN REVISIÓN'), ('APROBADO', 'APROBADO'), ('RECHAZADO', 'RECHAZADO')], default='REV', max_length=100, null=True),
        ),
    ]
