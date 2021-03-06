# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-02-03 21:53
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('selected', '0006_postquestionresultthree_end_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='PreQuestionResult1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mode_id', models.CharField(default='', max_length=1, verbose_name='\u6a21Id')),
                ('Q12_knewpretty', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7')], null=True, verbose_name='\u7cbe\u901a\u7a0b\u5ea6')),
                ('Q13_experts', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7')], null=True, verbose_name='\u5168\u5c40')),
                ('Q14_knewless', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7')], null=True, verbose_name='')),
                ('Q15_donotknow', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7')], null=True, verbose_name='')),
                ('Q16_donotfeel', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7')], null=True, verbose_name='')),
                ('Q17_lotofexperiences', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7')], null=True, verbose_name='')),
                ('Q18_familiar', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7')], null=True, verbose_name='')),
                ('Test_User', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='\u6d4b\u8bd5\u7528\u6237')),
            ],
            options={
                'verbose_name': 'Pre\u95ee\u5377\u7ed3\u679c1',
                'verbose_name_plural': 'Pre\u95ee\u5377\u7ed3\u679c1',
            },
        ),
        migrations.CreateModel(
            name='PreQuestionResult2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mode_id', models.CharField(default='', max_length=1, verbose_name='\u6a21Id')),
                ('Q19_focusobjects', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7')], null=True, verbose_name='')),
                ('Q20_basedcategories', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7')], null=True, verbose_name='')),
                ('Q21_easylearncategories', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7')], null=True, verbose_name='')),
                ('Q22_organizefunctionally', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7')], null=True, verbose_name='')),
                ('Q23_useformallogic', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7')], null=True, verbose_name='')),
                ('Q24_adherelogicalrules', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7')], null=True, verbose_name='')),
                ('Q25_individualbehavior', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7')], null=True, verbose_name='')),
                ('Q26_focussurobj', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7')], null=True, verbose_name='')),
                ('Q27_focussurfeld', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7')], null=True, verbose_name='')),
                ('Q28_difflearncate', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7')], null=True, verbose_name='')),
                ('Q29_organthematically', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7')], null=True, verbose_name='')),
                ('Q30_diareasoning', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7')], null=True, verbose_name='')),
                ('Q31_preflogic', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7')], null=True, verbose_name='')),
                ('Q32_peopbehav', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7')], null=True, verbose_name='')),
                ('Test_User', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='\u6d4b\u8bd5\u7528\u6237')),
            ],
            options={
                'verbose_name': 'Pre\u95ee\u5377\u7ed3\u679c2',
                'verbose_name_plural': 'Pre\u95ee\u5377\u7ed3\u679c2',
            },
        ),
        migrations.RemoveField(
            model_name='prequestionresult',
            name='Q12_knewpretty',
        ),
        migrations.RemoveField(
            model_name='prequestionresult',
            name='Q13_experts',
        ),
        migrations.RemoveField(
            model_name='prequestionresult',
            name='Q14_knewless',
        ),
        migrations.RemoveField(
            model_name='prequestionresult',
            name='Q15_donotknow',
        ),
        migrations.RemoveField(
            model_name='prequestionresult',
            name='Q16_donotfeel',
        ),
        migrations.RemoveField(
            model_name='prequestionresult',
            name='Q17_lotofexperiences',
        ),
        migrations.RemoveField(
            model_name='prequestionresult',
            name='Q18_familiar',
        ),
        migrations.RemoveField(
            model_name='prequestionresult',
            name='Q19_focusobjects',
        ),
        migrations.RemoveField(
            model_name='prequestionresult',
            name='Q20_basedcategories',
        ),
        migrations.RemoveField(
            model_name='prequestionresult',
            name='Q21_easylearncategories',
        ),
        migrations.RemoveField(
            model_name='prequestionresult',
            name='Q22_organizefunctionally',
        ),
        migrations.RemoveField(
            model_name='prequestionresult',
            name='Q23_useformallogic',
        ),
        migrations.RemoveField(
            model_name='prequestionresult',
            name='Q24_adherelogicalrules',
        ),
        migrations.RemoveField(
            model_name='prequestionresult',
            name='Q25_individualbehavior',
        ),
        migrations.RemoveField(
            model_name='prequestionresult',
            name='Q26_focussurobj',
        ),
        migrations.RemoveField(
            model_name='prequestionresult',
            name='Q27_focussurfeld',
        ),
        migrations.RemoveField(
            model_name='prequestionresult',
            name='Q28_difflearncate',
        ),
        migrations.RemoveField(
            model_name='prequestionresult',
            name='Q29_organthematically',
        ),
        migrations.RemoveField(
            model_name='prequestionresult',
            name='Q30_diareasoning',
        ),
        migrations.RemoveField(
            model_name='prequestionresult',
            name='Q31_preflogic',
        ),
        migrations.RemoveField(
            model_name='prequestionresult',
            name='Q32_peopbehav',
        ),
        migrations.RemoveField(
            model_name='prequestionresult',
            name='Q51_expertise',
        ),
        migrations.RemoveField(
            model_name='prequestionresult',
            name='Q5_expertise',
        ),
    ]
