# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-28 07:04
from __future__ import unicode_literals

from django.db import migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
        ('projects', '0004_reward'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='reward',
            options={'ordering': ['price']},
        ),
        migrations.AddField(
            model_name='project',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]
