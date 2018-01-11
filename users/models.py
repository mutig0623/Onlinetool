# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser,Permission
from classification.models import *
from datetime import datetime
from multiselectfield import MultiSelectField
from django.db import models

# Create your models here.


class UserProfile(AbstractUser):
    start_time = models.DateTimeField(default=datetime.now)
    end_time = models.DateTimeField(default=datetime.now)
    Mode_id = models.CharField(max_length=1, default="")

    def __unicode__(self):
        return self.username

    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name


class TechinforCH(models.Model):
    Tech_Name = models.CharField(max_length=50, default="", verbose_name=u"中文设计技术名称")
    Short_Description = models.TextField(max_length=500, default="", verbose_name=u"中文技术简短描述")
    Long_Description = models.TextField(max_length=1000, default="", verbose_name=u"中文技术详细描述")
    TDDesign = models.ForeignKey(TDDesignCH, verbose_name=u"TopDown设计阶段属性", null=True,blank=True)
    TDDependency = models.ForeignKey(TDDependencyCH, verbose_name=u"TopDown时间依赖", null=True,blank=True)
    TDDuration = models.ForeignKey(TDDurationCH, verbose_name=u"TopDown持续时间", null=True,blank=True)
    TDParticipation = models.ForeignKey(TDParticipationCH, verbose_name=u"TopDown用户参与", null=True,blank=True)
    TDEvaluation = models.ForeignKey(TDEvaluationCH, verbose_name=u"TopDown评估类型", null=True,blank=True)
    BUDesign = models.ForeignKey(BUDesignCH,verbose_name=u"BottomUp设计阶段", null=True,blank=True)
    BUCollection = models.ForeignKey(BUCollectionCH, verbose_name=u"BottomUp收集设计数据", null=True,blank=True)
    BUDuration = models.ForeignKey(BUDurationCH,verbose_name=u"Bottomup持续时间", null=True,blank=True)
    BUParticipant = models.ForeignKey(BUParticipantCH,verbose_name=u"Bottomup参与者", null=True,blank=True)
    UserParticipationgroup = models.CharField(max_length=5, default="", verbose_name=u"TagCloud分类名称1")
    MidDuration = models.CharField(max_length=5, default="", verbose_name=u"TagCloud分类名称2")
    Observation = models.CharField(max_length=5, default="", verbose_name=u"TagCloud分类名称3")
    IdeaGeneration = models.CharField(max_length=5, default="", verbose_name=u"TagCloud分类名称4")
    CollaborationStakeholders = models.CharField(max_length=5, default="", verbose_name=u"TagCloud分类名称5")
    FeedbackOnline = models.CharField(max_length=5, default="", verbose_name=u"TagCloud分类名称6")
    PrototypeEvaluation = models.CharField(max_length=5, default="", verbose_name=u"TagCloud分类名称7")
    DataCollection = models.CharField(max_length=5, default="", verbose_name=u"TagCloud分类名称8")
    Prototyping = models.CharField(max_length=5, default="", verbose_name=u"TagCloud分类名称9")
    ShortDuration = models.CharField(max_length=5, default="", verbose_name=u"TagCloud分类名称10")
    Evaluation = models.CharField(max_length=5, default="", verbose_name=u"TagCloud分类名称11")
    ProductEvaluation = models.CharField(max_length=5, default="", verbose_name=u"TagCloud分类名称12")
    ProjectOrganization = models.CharField(max_length=5, default="", verbose_name=u"TagCloud分类名称13")
    FlexibleLength = models.CharField(max_length=5, default="", verbose_name=u"TagCloud分类名称14")
    UserParticipation = models.CharField(max_length=5, default="", verbose_name=u"TagCloud分类名称15")
    InformationOrganization = models.CharField(max_length=5, default="", verbose_name=u"TagCloud分类名称16")
    FeedbackOffline = models.CharField(max_length=5, default="", verbose_name=u"TagCloud分类名称17")
    LongDuration = models.CharField(max_length=5, default="", verbose_name=u"TagCloud分类名称18")
    UserResearch = models.CharField(max_length=5, default="", verbose_name=u"TagCloud分类名称19")
    RelationshipDependency = models.CharField(max_length=5, default="", verbose_name=u"TagCloud分类名称20")
    UserSimulation = models.CharField(max_length=5, default="", verbose_name=u"TagCloud分类名称21")
    ExpertParticipation = models.CharField(max_length=5, default="", verbose_name=u"TagCloud分类名称22")
    UXEvaluation = models.CharField(max_length=5, default="", verbose_name=u"TagCloud分类名称23")
    FeedbackCollection = models.CharField(max_length=5, default="", verbose_name=u"TagCloud分类名称24")

    class Meta:
        verbose_name="中文设计技术信息"
        verbose_name_plural = verbose_name


class TechinforEN(models.Model):
    Tech_Name = models.CharField(max_length=50, default="", verbose_name=u"英文设计技术名称")
    Short_Description = models.TextField(max_length=500, default="", verbose_name=u"英文技术简短描述")
    Long_Description = models.TextField(max_length=1000, default="", verbose_name=u"英文技术详细描述")
    TDDesign = models.ForeignKey(TDDesignEN, verbose_name=u"TopDown设计阶段属性", null=True,blank=True)
    TDDependency = models.ForeignKey(TDDependencyEN, verbose_name=u"TopDown时间依赖", null=True,blank=True)
    TDDuration = models.ForeignKey(TDDurationEN, verbose_name=u"TopDown持续时间", null=True,blank=True)
    TDParticipation = models.ForeignKey(TDParticipationEN, verbose_name=u"TopDown用户参与", null=True,blank=True)
    TDEvaluation = models.ForeignKey(TDEvaluationEN, verbose_name=u"TopDown评估类型", null=True,blank=True)
    BUDesign = models.ForeignKey(BUDesignEN, verbose_name=u"BottomUp设计阶段", null=True,blank=True)
    BUCollection = models.ForeignKey(BUCollectionEN, verbose_name=u"BottomUp收集设计数据", null=True,blank=True)
    BUDuration = models.ForeignKey(BUDurationEN, verbose_name=u"Bottomup持续时间", null=True,blank=True)
    BUParticipant = models.ForeignKey(BUParticipantEN, verbose_name=u"Bottomup参与者", null=True,blank=True)
    UserParticipationgroup = models.CharField(max_length=5, default="", verbose_name=u"TagCloud分类名称1")
    MidDuration = models.CharField(max_length=5, default="", verbose_name=u"TagCloud分类名称2")
    Observation = models.CharField(max_length=5, default="", verbose_name=u"TagCloud分类名称3")
    IdeaGeneration = models.CharField(max_length=5, default="", verbose_name=u"TagCloud分类名称4")
    CollaborationStakeholders = models.CharField(max_length=5, default="", verbose_name=u"TagCloud分类名称5")
    FeedbackOnline = models.CharField(max_length=5, default="", verbose_name=u"TagCloud分类名称6")
    PrototypeEvaluation = models.CharField(max_length=5, default="", verbose_name=u"TagCloud分类名称7")
    DataCollection = models.CharField(max_length=5, default="", verbose_name=u"TagCloud分类名称8")
    Prototyping = models.CharField(max_length=5, default="", verbose_name=u"TagCloud分类名称9")
    ShortDuration = models.CharField(max_length=5, default="", verbose_name=u"TagCloud分类名称10")
    Evaluation = models.CharField(max_length=5, default="", verbose_name=u"TagCloud分类名称11")
    ProductEvaluation = models.CharField(max_length=5, default="", verbose_name=u"TagCloud分类名称12")
    ProjectOrganization = models.CharField(max_length=5, default="", verbose_name=u"TagCloud分类名称13")
    FlexibleLength = models.CharField(max_length=5, default="", verbose_name=u"TagCloud分类名称14")
    UserParticipation = models.CharField(max_length=5, default="", verbose_name=u"TagCloud分类名称15")
    InformationOrganization = models.CharField(max_length=5, default="", verbose_name=u"TagCloud分类名称16")
    FeedbackOffline = models.CharField(max_length=5, default="", verbose_name=u"TagCloud分类名称17")
    LongDuration = models.CharField(max_length=5, default="", verbose_name=u"TagCloud分类名称18")
    UserResearch = models.CharField(max_length=5, default="", verbose_name=u"TagCloud分类名称19")
    RelationshipDependency = models.CharField(max_length=5, default="", verbose_name=u"TagCloud分类名称20")
    UserSimulation = models.CharField(max_length=5, default="", verbose_name=u"TagCloud分类名称21")
    ExpertParticipation = models.CharField(max_length=5, default="", verbose_name=u"TagCloud分类名称22")
    UXEvaluation = models.CharField(max_length=5, default="", verbose_name=u"TagCloud分类名称23")
    FeedbackCollection = models.CharField(max_length=5, default="", verbose_name=u"TagCloud分类名称24")

    class Meta:
        verbose_name="英文设计技术信息"
        verbose_name_plural = verbose_name


class TechinforDE(models.Model):
    Tech_Name = models.CharField(max_length=50, default="", verbose_name=u"德语设计技术名称")
    Short_Description = models.TextField(max_length=500, default="", verbose_name=u"德语技术简短描述")
    Long_Description = models.TextField(max_length=1000, default="", verbose_name=u"德语技术详细描述")
    TDDesign = models.ForeignKey(TDDesignDE, verbose_name=u"TopDown设计阶段属性", null=True,blank=True)
    TDDependency = models.ForeignKey(TDDependencyDE, verbose_name=u"TopDown时间依赖", null=True,blank=True)
    TDDuration = models.ForeignKey(TDDurationDE, verbose_name=u"TopDown持续时间", null=True,blank=True)
    TDParticipation = models.ForeignKey(TDParticipationDE, verbose_name=u"TopDown用户参与", null=True,blank=True)
    TDEvaluation = models.ForeignKey(TDEvaluationDE, verbose_name=u"TopDown评估类型", null=True,blank=True)
    BUDesign = models.ForeignKey(BUDesignDE, verbose_name=u"BottomUp设计阶段", null=True,blank=True)
    BUCollection = models.ForeignKey(BUCollectionDE, verbose_name=u"BottomUp收集设计数据", null=True,blank=True)
    BUDuration = models.ForeignKey(BUDurationDE, verbose_name=u"Bottomup持续时间", null=True,blank=True)
    BUParticipant = models.ForeignKey(BUParticipantDE, verbose_name=u"Bottomup参与者", null=True,blank=True)
    UserParticipationgroup = models.CharField(max_length=5, default="", verbose_name=u"TagCloud分类名称1")
    MidDuration = models.CharField(max_length=5, default="", verbose_name=u"TagCloud分类名称2")
    Observation = models.CharField(max_length=5, default="", verbose_name=u"TagCloud分类名称3")
    IdeaGeneration = models.CharField(max_length=5, default="", verbose_name=u"TagCloud分类名称4")
    CollaborationStakeholders = models.CharField(max_length=5, default="", verbose_name=u"TagCloud分类名称5")
    FeedbackOnline = models.CharField(max_length=5, default="", verbose_name=u"TagCloud分类名称6")
    PrototypeEvaluation = models.CharField(max_length=5, default="", verbose_name=u"TagCloud分类名称7")
    DataCollection = models.CharField(max_length=5, default="", verbose_name=u"TagCloud分类名称8")
    Prototyping = models.CharField(max_length=5, default="", verbose_name=u"TagCloud分类名称9")
    ShortDuration = models.CharField(max_length=5, default="", verbose_name=u"TagCloud分类名称10")
    Evaluation = models.CharField(max_length=5, default="", verbose_name=u"TagCloud分类名称11")
    ProductEvaluation = models.CharField(max_length=5, default="", verbose_name=u"TagCloud分类名称12")
    ProjectOrganization = models.CharField(max_length=5, default="", verbose_name=u"TagCloud分类名称13")
    FlexibleLength = models.CharField(max_length=5, default="", verbose_name=u"TagCloud分类名称14")
    UserParticipation = models.CharField(max_length=5, default="", verbose_name=u"TagCloud分类名称15")
    InformationOrganization = models.CharField(max_length=5, default="", verbose_name=u"TagCloud分类名称16")
    FeedbackOffline = models.CharField(max_length=5, default="", verbose_name=u"TagCloud分类名称17")
    LongDuration = models.CharField(max_length=5, default="", verbose_name=u"TagCloud分类名称18")
    UserResearch = models.CharField(max_length=5, default="", verbose_name=u"TagCloud分类名称19")
    RelationshipDependency = models.CharField(max_length=5, default="", verbose_name=u"TagCloud分类名称20")
    UserSimulation = models.CharField(max_length=5, default="", verbose_name=u"TagCloud分类名称21")
    ExpertParticipation = models.CharField(max_length=5, default="", verbose_name=u"TagCloud分类名称22")
    UXEvaluation = models.CharField(max_length=5, default="", verbose_name=u"TagCloud分类名称23")
    FeedbackCollection = models.CharField(max_length=5, default="", verbose_name=u"TagCloud分类名称24")

    class Meta:
        verbose_name="德语设计技术信息"
        verbose_name_plural = verbose_name


class PreResultTasks(models.Model):
    Task_Description = models.TextField(max_length=500, default="", verbose_name=u"测试题目描述")
    Re_Result1 = models.CharField(max_length=50, default="", verbose_name=u"预先设定答案1")
    Re_Result2 = models.CharField(max_length=50, default="", verbose_name=u"预先设定答案2")
    Re_Result3 = models.CharField(max_length=50, default="", verbose_name=u"预先设定答案3")
    Re_Result4 = models.CharField(max_length=50, default="", verbose_name=u"预先设定答案4")
    Re_Result5 = models.CharField(max_length=50, default="", verbose_name=u"预先设定答案5")
    Re_Result6 = models.CharField(max_length=50, default="", verbose_name=u"预先设定答案6")
    Re_Result7 = models.CharField(max_length=50, default="", verbose_name=u"预先设定答案7")
    Re_Result8 = models.CharField(max_length=50, default="", verbose_name=u"预先设定答案8")
    Re_Result9 = models.CharField(max_length=50, default="", verbose_name=u"预先设定答案9")
    Re_Result10 = models.CharField(max_length=50, default="", verbose_name=u"预先设定答案10")

    class Meta:
        verbose_name="场景的预设答案"
        verbose_name_plural = verbose_name