# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-02-14 19:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_auto_20170214_1952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='status',
            field=models.CharField(blank=True, choices=[('REVISION', 'REVISION'), ('APROBADO', 'APROBADO'), ('RECHAZADO', 'RECHAZADO')], default='REV', max_length=100, null=True),
        ),
    ]
