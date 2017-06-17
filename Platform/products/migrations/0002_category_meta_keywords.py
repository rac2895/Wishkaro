# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='meta_keywords',
            field=models.CharField(help_text=b'Comma-delimited set of SEO keywords for meta tag', max_length=255, null=True),
        ),
    ]
