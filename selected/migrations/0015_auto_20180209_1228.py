# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-02-09 11:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('selected', '0014_auto_20180206_2114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prequestionresult',
            name='CountryYears',
            field=models.CharField(max_length=10, null=True, verbose_name='\u5e74\u957f'),
        ),
    ]