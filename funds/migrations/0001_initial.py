# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-12-31 03:02
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(max_length=140)),
            ],
        ),
        migrations.CreateModel(
            name='Fund',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.CharField(max_length=10)),
                ('date', models.DateTimeField(auto_now=True)),
                ('contributor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='funds', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
