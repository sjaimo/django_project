# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-09 02:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='test',
            field=models.TextField(default='anonymous'),
            preserve_default=False,
        ),
    ]
