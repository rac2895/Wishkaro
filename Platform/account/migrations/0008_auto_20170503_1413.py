# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2017-05-03 08:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_misc_misccoverimage'),
    ]

    operations = [
        migrations.RenameField(
            model_name='misc',
            old_name='image',
            new_name='image1',
        ),
        migrations.RenameField(
            model_name='misc',
            old_name='name',
            new_name='name1',
        ),
        migrations.RenameField(
            model_name='misc',
            old_name='title',
            new_name='price1',
        ),
        migrations.RenameField(
            model_name='misccoverimage',
            old_name='image',
            new_name='image1',
        ),
        migrations.AddField(
            model_name='misc',
            name='title1',
            field=models.CharField(default=b'', max_length=120),
        ),
    ]
