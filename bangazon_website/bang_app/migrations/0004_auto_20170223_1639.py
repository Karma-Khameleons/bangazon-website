# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-23 16:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bang_app', '0003_auto_20170222_2334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=20),
        ),
    ]
