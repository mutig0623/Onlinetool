# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-02-09 14:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('selected', '0015_auto_20180209_1228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prequestionresult',
            name='CountryName',
            field=models.CharField(default='', max_length=100, null=True, verbose_name='\u56fd\u5bb6\u540d\u79f0'),
        ),
        migrations.AlterField(
            model_name='prequestionresult',
            name='CountryYears',
            field=models.CharField(default='', max_length=10, null=True, verbose_name='\u5e74\u957f'),
        ),
    ]
