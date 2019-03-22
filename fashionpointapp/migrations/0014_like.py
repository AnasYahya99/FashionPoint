# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-03-17 13:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fashionpointapp', '0013_category_picture'),
    ]

    operations = [
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.PositiveIntegerField(default=0)),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fashionpointapp.PostComment')),
                ('userPofile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fashionpointapp.UserProfile')),
            ],
            options={
                'verbose_name_plural': 'likes',
            },
        ),
    ]