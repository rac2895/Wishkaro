# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-11-29 16:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_product_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='slug',
        ),
    ]
