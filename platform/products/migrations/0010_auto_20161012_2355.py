# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-10-12 18:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_auto_20161011_2214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coverimage',
            name='image',
            field=models.ImageField(upload_to=b'images/prath'),
        ),
    ]
