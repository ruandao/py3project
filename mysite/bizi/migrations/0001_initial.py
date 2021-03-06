# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-28 07:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Img',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('model_pic', models.ImageField(upload_to='pic_folder/')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bizi.Category')),
            ],
        ),
    ]
