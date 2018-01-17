# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-17 00:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_post_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('d', 'Draft'), ('p', 'Published'), ('w', 'Withdrawn')], default='draft', max_length=1),
            preserve_default=False,
        ),
    ]
