# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-03-22 01:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fashionpointapp', '0018_likepoll'),
    ]

    operations = [
        migrations.AddField(
            model_name='pollcomment',
            name='nod',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='pollcomment',
            name='nol',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
