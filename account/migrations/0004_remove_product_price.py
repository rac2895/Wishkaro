# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-11-29 12:57
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_coverimage_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='price',
        ),
    ]