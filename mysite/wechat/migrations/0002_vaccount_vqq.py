# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-03 11:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wechat', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vaccount',
            name='vQQ',
            field=models.CharField(default='', max_length=30),
            preserve_default=False,
        ),
    ]
