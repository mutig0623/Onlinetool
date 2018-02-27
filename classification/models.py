# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class TDDesignCH(models.Model):
    Design_Name = models.CharField(max_length=20, default="", verbose_name=unicode("中文TopDown设计阶段属性"))

    class Meta:
        verbose_name=unicode("中文TopDown设计阶段")
        verbose_name_plural = verbose_name


class TDDependencyCH(models.Model):
    Dependency_Name = models.CharField(max_length=20, default="", verbose_name=unicode("中文TopDown时间依赖"))

    class Meta:
        verbose_name=unicode("中文TopDown时间依赖性")
        verbose_name_plural = verbose_name


class TDDurationCH(models.Model):
    Duration_Name = models.CharField(max_length=20, default="", verbose_name=unicode("中文TopDown持续时间"))

    class Meta:
        verbose_name=unicode("中文TopDown持续时间")
        verbose_name_plural = verbose_name


class TDParticipationCH(models.Model):
    Participation_Name = models.CharField(max_length=20, default="", verbose_name=unicode("中文TopDown用户参与"))

    class Meta:
        verbose_name=unicode("中文TopDown用户参与")
        verbose_name_plural = verbose_name


class TDEvaluationCH(models.Model):
    Evaluation_Name = models.CharField(max_length=20, default="", verbose_name=u"中文TopDown评估类型")

    class Meta:
        verbose_name=u"中文TopDown评估类型"
        verbose_name_plural = verbose_name


class TDDesignEN(models.Model):
    Design_Name = models.CharField(max_length=50, default="", verbose_name=u"英文TopDown设计阶段属性")

    class Meta:
        verbose_name=u"英文TopDown设计阶段"
        verbose_name_plural = verbose_name


class TDDependencyEN(models.Model):
    Dependency_Name = models.CharField(max_length=20, default="", verbose_name=u"英文TopDown时间依赖")

    class Meta:
        verbose_name=u"英文TopDown时间依赖性"
        verbose_name_plural = verbose_name


class TDDurationEN(models.Model):
    Duration_Name = models.CharField(max_length=20, default="", verbose_name=u"英文TopDown持续时间")

    class Meta:
        verbose_name=u"英文TopDown持续时间"
        verbose_name_plural = verbose_name


class TDParticipationEN(models.Model):
    Participation_Name = models.CharField(max_length=20, default="", verbose_name=u"英文TopDown用户参与")

    class Meta:
        verbose_name=u"英文TopDown用户参与"
        verbose_name_plural = verbose_name


class TDEvaluationEN(models.Model):
    Evaluation_Name = models.CharField(max_length=20, default="", verbose_name=u"英文TopDown评估类型")

    class Meta:
        verbose_name=u"英文TopDown评估类型"
        verbose_name_plural = verbose_name


class TDDesignDE(models.Model):
    Design_Name = models.CharField(max_length=20, default="", verbose_name=u"德语TopDown设计阶段属性")

    class Meta:
        verbose_name=u"德语TopDown设计阶段"
        verbose_name_plural = verbose_name


class TDDependencyDE(models.Model):
    Dependency_Name = models.CharField(max_length=20, default="", verbose_name=u"德语TopDown时间依赖")

    class Meta:
        verbose_name=u"德语TopDown时间依赖性"
        verbose_name_plural = verbose_name


class TDDurationDE(models.Model):
    Duration_Name = models.CharField(max_length=20, default="", verbose_name=u"德语TopDown持续时间")

    class Meta:
        verbose_name=u"德语TopDown持续时间"
        verbose_name_plural = verbose_name


class TDParticipationDE(models.Model):
    Participation_Name = models.CharField(max_length=20, default="", verbose_name=u"德语TopDown用户参与")

    class Meta:
        verbose_name=u"德语TopDown用户参与"
        verbose_name_plural = verbose_name


class TDEvaluationDE(models.Model):
    Evaluation_Name = models.CharField(max_length=20, default="", verbose_name=u"德语TopDown评估类型")

    class Meta:
        verbose_name=u"德语TopDown评估类型"
        verbose_name_plural = verbose_name


class BUDesignCH(models.Model):
    Design_Name = models.CharField(max_length=20, default="", verbose_name=u"中文BottomUp设计阶段")

    class Meta:
        verbose_name=u"中文Bottomup设计阶段"
        verbose_name_plural = verbose_name


class BUCollectionCH(models.Model):
    Collection_Name = models.CharField(max_length=20, default="", verbose_name=u"中文BottomUp收集设计数据")

    class Meta:
        verbose_name=u"中文Bottomup收集设计数据"
        verbose_name_plural = verbose_name


class BUDurationCH(models.Model):
    Duration_Name = models.CharField(max_length=20, default="", verbose_name=u"中文Bottomup持续时间")

    class Meta:
        verbose_name=u"中文Bottomup持续时间"
        verbose_name_plural = verbose_name


class BUParticipantCH(models.Model):
    Participant_Name = models.CharField(max_length=20, default="", verbose_name=u"中文Bottomup参与者")

    class Meta:
        verbose_name=u"中文Bottomup参与者"
        verbose_name_plural = verbose_name


class BUDesignEN(models.Model):
    Design_Name = models.CharField(max_length=20, default="", verbose_name=u"英文BottomUp设计阶段")

    class Meta:
        verbose_name=u"英文Bottomup设计阶段"
        verbose_name_plural = verbose_name


class BUCollectionEN(models.Model):
    Collection_Name = models.CharField(max_length=30, default="", verbose_name=u"英文BottomUp收集设计数据")

    class Meta:
        verbose_name=u"英文Bottomup收集设计数据"
        verbose_name_plural = verbose_name


class BUDurationEN(models.Model):
    Duration_Name = models.CharField(max_length=20, default="", verbose_name=u"英文Bottomup持续时间")

    class Meta:
        verbose_name=u"英文Bottomup持续时间"
        verbose_name_plural = verbose_name


class BUParticipantEN(models.Model):
    Participant_Name = models.CharField(max_length=20, default="", verbose_name=u"英文Bottomup参与者")

    class Meta:
        verbose_name=u"英文Bottomup参与者"
        verbose_name_plural = verbose_name


class BUDesignDE(models.Model):
    Design_Name = models.CharField(max_length=20, default="", verbose_name=u"德语BottomUp设计阶段")

    class Meta:
        verbose_name=u"德语Bottomup设计阶段"
        verbose_name_plural = verbose_name


class BUCollectionDE(models.Model):
    Collection_Name = models.CharField(max_length=50, default="", verbose_name=u"德语BottomUp收集设计数据")

    class Meta:
        verbose_name=u"德语Bottomup收集设计数据"
        verbose_name_plural = verbose_name


class BUDurationDE(models.Model):
    Duration_Name = models.CharField(max_length=20, default="", verbose_name=u"德语Bottomup持续时间")

    class Meta:
        verbose_name=u"德语Bottomup持续时间"
        verbose_name_plural = verbose_name


class BUParticipantDE(models.Model):
    Participant_Name = models.CharField(max_length=20, default="", verbose_name=u"德语Bottomup参与者")

    class Meta:
        verbose_name=u"德语Bottomup参与者"
        verbose_name_plural = verbose_name


class TagCloudCH(models.Model):
    TagCloud_Name = models.CharField(max_length=20, default="", verbose_name=u"中文TagCloud分类名称")
    frequency = models.IntegerField(verbose_name=u"频率")

    class Meta:
        verbose_name=u"中文TagCloud分类信息"
        verbose_name_plural = verbose_name


class TagCloudEN(models.Model):
    TagCloud_Name = models.CharField(max_length=50, default="", verbose_name=u"英文TagCloud分类名称")
    frequency = models.CharField(default="", max_length=2, verbose_name=u"频率")

    class Meta:
        verbose_name=u"英文TagCloud分类信息"
        verbose_name_plural = verbose_name


class TagCloudDE(models.Model):
    TagCloud_Name = models.CharField(max_length=20, default="", verbose_name=u"德语TagCloud分类名称")
    frequency = models.CharField(default="", max_length=2, verbose_name=u"频率")

    class Meta:
        verbose_name=u"德语TagCloud分类信息"
        verbose_name_plural = verbose_name


class PreQuestionCH(models.Model):
    PreQues_Description = models.TextField(max_length=200, default="", verbose_name=u"中文Pre问题")

    class Meta:
        verbose_name = u"中文PreQuestion的信息"
        verbose_name_plural = verbose_name


class PreQuestionEN(models.Model):
    PreQues_Description = models.TextField(max_length=200, default="", verbose_name=u"英文Pre问题")

    class Meta:
        verbose_name = u"英文PreQuestion的信息"
        verbose_name_plural = verbose_name


class PreQuestionDE(models.Model):
    PreQues_Description = models.TextField(max_length=200, default="", verbose_name=u"德语Pre问题")

    class Meta:
        verbose_name = u"德语PreQuestion的信息"
        verbose_name_plural = verbose_name


class PostQuestionCH(models.Model):
    PostQues_Description = models.TextField(max_length=200, default="", verbose_name=u"中文前两个的Post问题")

    class Meta:
        verbose_name = u"中文前两个Post问题"
        verbose_name_plural = verbose_name


class PostQuestionEN(models.Model):
    PostQues_Description = models.TextField(max_length=200, default="", verbose_name=u"英文前两个的Post问题")

    class Meta:
        verbose_name = u"英文前两个Post问题"
        verbose_name_plural = verbose_name


class PostQuestionDE(models.Model):
    PostQues_Description = models.TextField(max_length=200, default="", verbose_name=u"德语前两个的Post问题")

    class Meta:
        verbose_name = u"德语前两个Post问题"
        verbose_name_plural = verbose_name

class PostQuestionPlusCH(models.Model):
    PostQues_Description = models.TextField(max_length=200, default="", verbose_name=u"中文最后一个附加问题")

    class Meta:
        verbose_name = u"中文最后一个Post问题"
        verbose_name_plural = verbose_name


class PostQuestionPlusEN(models.Model):
    PostQues_Description = models.TextField(max_length=200, default="", verbose_name=u"英文最后一个附加问题")

    class Meta:
        verbose_name = u"中英文最后一个Post问题"
        verbose_name_plural = verbose_name


class PostQuestionPlusDE(models.Model):
    PostQues_Description = models.TextField(max_length=200, default="", verbose_name=u"德语最后一个附加问题")

    class Meta:
        verbose_name = u"德语最后一个Post问题"
        verbose_name_plural = verbose_name


class TaskDescriptionCH(models.Model):
    Description = models.TextField(max_length=1000, default="", verbose_name=u"中文场景描述")

    class Meta:
        verbose_name = u"中文Task场景描述"
        verbose_name_plural = verbose_name


class TaskDescriptionEN(models.Model):
    Description = models.TextField(max_length=1000, default="", verbose_name=u"英文场景描述")

    class Meta:
        verbose_name = u"英文Task场景描述"
        verbose_name_plural = verbose_name


class TaskDescriptionDE(models.Model):
    Description = models.TextField(max_length=1000, default="", verbose_name=u"中文场景描述")

    class Meta:
        verbose_name = u"德语Task场景描述"
        verbose_name_plural = verbose_name
