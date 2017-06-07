# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_remove_product_sku'),
    ]

    operations = [
        migrations.CreateModel(
            name='CoverImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(upload_to=b'images/ritu')),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='meta_keywords',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(unique=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='variation',
            name='category',
            field=models.CharField(default=b'size', max_length=120, choices=[(b'size', b'size'), (b'color', b'color')]),
        ),
    ]
