# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-02-13 15:57
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_userprofile_endtime'),
    ]

    operations = [
        migrations.RenameField(
            model_name='techinforen',
            old_name='MidDuration',
            new_name='MidtermDuration',
        ),
    ]
