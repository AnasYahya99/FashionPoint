# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-03-18 19:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fashionpointapp', '0013_category_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='dateOfBirth',
            field=models.DateField(null=True),
        ),
    ]