# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-11-29 16:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_remove_product_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='author',
            field=models.CharField(default=b'', max_length=120),
        ),
    ]