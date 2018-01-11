# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from users.models import UserProfile
from multiselectfield import MultiSelectField

from django.db import models

# Create your models here.
class SelectedTechniqueOne(models.Model):
    Test_User = models.ForeignKey(UserProfile, verbose_name=u"测试用户")
    chose_Tech1 = models.TextField(max_length=200, verbose_name=u"选择的技术1", default="")
    chose_Tech2 = models.TextField(max_length=200, verbose_name=u"选择的技术2", default="")
    chose_Tech3 = models.TextField(max_length=200, verbose_name=u"选择的技术3", default="")

    def __unicode__(self):
        return self.subject

    class Meta:
        verbose_name = "场景One选择的结果"
        verbose_name_plural = verbose_name


class SelectedTechniqueTwo(models.Model):
    Test_User = models.ForeignKey(UserProfile, verbose_name=u"测试用户")
    chose_Tech1 = models.TextField(max_length=200, verbose_name=u"选择的技术1", default="")
    chose_Tech2 = models.TextField(max_length=200, verbose_name=u"选择的技术2", default="")
    chose_Tech3 = models.TextField(max_length=200, verbose_name=u"选择的技术3", default="")

    class Meta:
        verbose_name = "场景Two的选择结果"
        verbose_name_plural = verbose_name


class SelectedTechniqueThree(models.Model):
    Test_User = models.ForeignKey(UserProfile, verbose_name=u"测试用户")
    chose_Tech1 = models.TextField(max_length=200, verbose_name=u"选择的技术1", default="")
    chose_Tech2 = models.TextField(max_length=200, verbose_name=u"选择的技术2", default="")
    chose_Tech3 = models.TextField(max_length=200, verbose_name=u"选择的技术3", default="")

    class Meta:
        verbose_name = "场景Three的选择结果"
        verbose_name_plural = verbose_name


class PreQuestionResult(models.Model):
    Test_User = models.ForeignKey(UserProfile, verbose_name=u"测试用户")
    Q1_age = models.CharField(max_length=20, choices=((u"<20", u"<20"), (u"21-30", u"21-30"), (u"31-40", u"31-40"), (u"41-50", u"41-50"), (u">51", u">51")), verbose_name=u"年龄",null=True)
    Q2_gender = models.CharField(choices=((u"female", u"女"), (u"male", u"男"), (u"other", u"其他")), max_length=10, verbose_name=u"性别",null=True)
    Q3_nationa = models.CharField(max_length=20, default="", verbose_name=u"国籍",null=True)
    Q4_educationlevel = models.CharField(null=True,max_length=20, choices=(
        (u"UG", u"Undergraduate"), (u"Bachelor", u"Bachelor's degree"), (u"MS", u"Postgraduate (Master)"),
        (u"Master", u"Master's degree"), (u"DS", u"Doctoral student"), (u"Doctorate", u"Doctorate degree")),
        verbose_name=u"教育程度")
    Q41_educationlevel = models.CharField(null=True,max_length=20, default="", verbose_name=u"其他教育程度")
    Q5_expertise = MultiSelectField(null=True,choices=(
        ("CP", u"Computer program"), ("DS", u"Design service"), ("MA", u"Management"), ("TS", u"Technical service"),
        ("SR", u"Scientific research"), ("EDU", u"Education")), verbose_name=u"设计经验", max_choices=3, max_length=50)
    Q51_expertise = models.CharField(null=True,max_length=20, default="", verbose_name=u"其他专业知识")
    Q6_role = MultiSelectField(null=True,choices=(
    ("M", u"Manager"), ("S", u"Student"), ("D", u"Designer"), ("C", u"Consultant"), ("R", u"Researcher"),
    ("P", u"Programmer")), max_choices=3, verbose_name=u"设计角色", max_length=50)
    Q61_role = models.CharField(null=True,max_length=20, default="", verbose_name=u"其他角色")
    Q7_fulltime = models.CharField(null=True,max_length=20,default="", verbose_name=u"工作时长")
    Q8_ProjectCount = models.CharField(null=True,max_length=10,
        choices=((1, u"0个"), (2, u"<3个"), (3, u"3-5个"), (4, u"6-10个"), (5, u"11-15个"), (6, u">15个")), verbose_name=u"设计项目个数")
    Q9_DesigCourse = models.CharField(null=True,max_length=10, choices=((1, u"有参加过"), (2, u"没参加过")), verbose_name=u"是否参加过设计课程或讲座")
    Q10_UsedTechnique = models.CharField(null=True, max_length=10, choices=((1, u"使用过"), (2, u"没使用过")), verbose_name=u"是否使用过设计技术")
    Q11_FamiliarTechnique = MultiSelectField(null=True,max_length=50,
        choices=((1, u"角色模型"), (2, u"场景"), (3, u"出声思考"), (4, u"卡诺分析"), (5, u"角色扮演"), (6, u"行为地图"), (7, u"以上都不是")),
        verbose_name=u"熟悉的技术", max_choices=3)

    degree_choices = (
        (1, u"1"), (2, u"2"), (3, u"3"), (4, u"4"), (5, u"5"), (6, u"6"), (7, u"7")
    )
    Q12_knewpretty = models.IntegerField(null=True,choices=degree_choices,verbose_name=u"精通程度")
    Q13_experts = models.IntegerField(null=True,choices=degree_choices, verbose_name=u"全局")
    Q14_knewless = models.IntegerField(null=True,choices=degree_choices, verbose_name=u"")
    Q15_donotknow = models.IntegerField(null=True,choices=degree_choices, verbose_name=u"")
    Q16_donotfeel = models.IntegerField(null=True,choices=degree_choices, verbose_name=u"")
    Q17_lotofexperiences = models.IntegerField(null=True,choices=degree_choices, verbose_name=u"")
    Q18_familiar = models.IntegerField(null=True,choices=degree_choices, verbose_name=u"")
    Q19_focusobjects = models.IntegerField(null=True,choices=degree_choices, verbose_name=u"")
    Q20_basedcategories = models.IntegerField(null=True,choices=degree_choices, verbose_name=u"")
    Q21_easylearncategories = models.IntegerField(null=True,choices=degree_choices, verbose_name=u"")
    Q22_organizefunctionally = models.IntegerField(null=True,choices=degree_choices, verbose_name=u"")
    Q23_useformallogic = models.IntegerField(null=True,choices=degree_choices, verbose_name=u"")
    Q24_adherelogicalrules = models.IntegerField(null=True,choices=degree_choices, verbose_name=u"")
    Q25_individualbehavior = models.IntegerField(null=True,choices=degree_choices, verbose_name=u"")
    Q26_focussurobj = models.IntegerField(null=True,choices=degree_choices, verbose_name=u"")
    Q27_focussurfeld = models.IntegerField(null=True,choices=degree_choices, verbose_name=u"")
    Q28_difflearncate = models.IntegerField(null=True,choices=degree_choices, verbose_name=u"")
    Q29_organthematically = models.IntegerField(null=True,choices=degree_choices, verbose_name=u"")
    Q30_diareasoning = models.IntegerField(null=True,choices=degree_choices, verbose_name=u"")
    Q31_preflogic = models.IntegerField(null=True,choices=degree_choices, verbose_name=u"")
    Q32_peopbehav = models.IntegerField(choices=degree_choices, verbose_name=u"",null=True)

    class Meta:
        verbose_name = "Pre问卷结果"
        verbose_name_plural = verbose_name


class PostQuestionResultOne(models.Model):
    Test_User = models.ForeignKey(UserProfile, verbose_name=u"测试用户")
    degree_choices = (
        (1, u"1"), (2, u"2"), (3, u"3"), (4, u"4"), (5, u"5"), (6, u"6"), (7, u"7")
    )
    Q1_proficiency = models.IntegerField(choices=degree_choices, verbose_name=u"精通程度",null=True)
    Q2_globalapproach = models.IntegerField(choices=degree_choices, verbose_name=u"全局",null=True)
    Q3_localizedapproach = models.IntegerField(choices=degree_choices, verbose_name=u"",null=True)
    Q4_objects = models.IntegerField(choices=degree_choices, verbose_name=u"",null=True)
    Q5_rulesbased = models.IntegerField(choices=degree_choices, verbose_name=u"",null=True)
    Q6_learncategory = models.IntegerField(choices=degree_choices, verbose_name=u"",null=True)
    Q7_organize = models.IntegerField(choices=degree_choices, verbose_name=u"",null=True)
    Q8_formallogic = models.IntegerField(choices=degree_choices, verbose_name=u"",null=True)
    Q9_logicalrules = models.IntegerField(choices=degree_choices, verbose_name=u"",null=True)
    Q10_individual = models.IntegerField(choices=degree_choices, verbose_name=u"",null=True)
    Q11_surrounding = models.IntegerField(choices=degree_choices, verbose_name=u"",null=True)
    Q12_littelrule = models.IntegerField(choices=degree_choices, verbose_name=u"",null=True)
    Q13_difficultrule = models.IntegerField(choices=degree_choices, verbose_name=u"",null=True)
    Q14_thematically = models.IntegerField(choices=degree_choices, verbose_name=u"",null=True)
    Q15_dialectical = models.IntegerField(choices=degree_choices, verbose_name=u"",null=True)
    Q16_contradiction = models.IntegerField(choices=degree_choices, verbose_name=u"",null=True)
    Q17_pressures = models.IntegerField(choices=degree_choices, verbose_name=u"",null=True)
    Q18_thematically = models.IntegerField(choices=degree_choices, verbose_name=u"",null=True)

    class Meta:
        verbose_name = "Post问卷结果One"
        verbose_name_plural = verbose_name


class PostQuestionResultTwo(models.Model):
    Test_User = models.ForeignKey(UserProfile, verbose_name=u"测试用户")
    degree_choices = (
        (1, u"1"), (2, u"2"), (3, u"3"), (4, u"4"), (5, u"5"), (6, u"6"), (7, u"7")
    )
    Q1_proficiency = models.IntegerField(choices=degree_choices, verbose_name=u"精通程度",null=True)
    Q2_globalapproach = models.IntegerField(choices=degree_choices, verbose_name=u"全局",null=True)
    Q3_localizedapproach = models.IntegerField(choices=degree_choices, verbose_name=u"",null=True)
    Q4_objects = models.IntegerField(choices=degree_choices, verbose_name=u"",null=True)
    Q5_rulesbased = models.IntegerField(choices=degree_choices, verbose_name=u"",null=True)
    Q6_learncategory = models.IntegerField(choices=degree_choices, verbose_name=u"",null=True)
    Q7_organize = models.IntegerField(choices=degree_choices, verbose_name=u"",null=True)
    Q8_formallogic = models.IntegerField(choices=degree_choices, verbose_name=u"",null=True)
    Q9_logicalrules = models.IntegerField(choices=degree_choices, verbose_name=u"",null=True)
    Q10_individual = models.IntegerField(choices=degree_choices, verbose_name=u"",null=True)
    Q11_surrounding = models.IntegerField(choices=degree_choices, verbose_name=u"",null=True)
    Q12_littelrule = models.IntegerField(choices=degree_choices, verbose_name=u"",null=True)
    Q13_difficultrule = models.IntegerField(choices=degree_choices, verbose_name=u"",null=True)
    Q14_thematically = models.IntegerField(choices=degree_choices, verbose_name=u"",null=True)
    Q15_dialectical = models.IntegerField(choices=degree_choices, verbose_name=u"",null=True)
    Q16_contradiction = models.IntegerField(choices=degree_choices, verbose_name=u"",null=True)
    Q17_pressures = models.IntegerField(choices=degree_choices, verbose_name=u"",null=True)
    Q18_thematically = models.IntegerField(choices=degree_choices, verbose_name=u"",null=True)

    class Meta:
        verbose_name = "Post问卷结果Two"
        verbose_name_plural = verbose_name


class PostQuestionResultThree(models.Model):
    Test_User = models.ForeignKey(UserProfile, verbose_name=u"测试用户")
    degree_choices = (
        (1, u"1"), (2, u"2"), (3, u"3"), (4, u"4"), (5, u"5"), (6, u"6"), (7, u"7")
    )
    Q1_proficiency = models.IntegerField(choices=degree_choices, verbose_name=u"精通程度",null=True)
    Q2_globalapproach = models.IntegerField(choices=degree_choices, verbose_name=u"全局",null=True)
    Q3_localizedapproach = models.IntegerField(choices=degree_choices, verbose_name=u"",null=True)
    Q4_objects = models.IntegerField(choices=degree_choices, verbose_name=u"",null=True)
    Q5_rulesbased = models.IntegerField(choices=degree_choices, verbose_name=u"",null=True)
    Q6_learncategory = models.IntegerField(choices=degree_choices, verbose_name=u"",null=True)
    Q7_organize = models.IntegerField(choices=degree_choices, verbose_name=u"",null=True)
    Q8_formallogic = models.IntegerField(choices=degree_choices, verbose_name=u"",null=True)
    Q9_logicalrules = models.IntegerField(choices=degree_choices, verbose_name=u"",null=True)
    Q10_individual = models.IntegerField(choices=degree_choices, verbose_name=u"",null=True)
    Q11_surrounding = models.IntegerField(choices=degree_choices, verbose_name=u"",null=True)
    Q12_littelrule = models.IntegerField(choices=degree_choices, verbose_name=u"",null=True)
    Q13_difficultrule = models.IntegerField(choices=degree_choices, verbose_name=u"",null=True)
    Q14_thematically = models.IntegerField(choices=degree_choices, verbose_name=u"",null=True)
    Q15_dialectical = models.IntegerField(choices=degree_choices, verbose_name=u"",null=True)
    Q16_contradiction = models.IntegerField(choices=degree_choices, verbose_name=u"",null=True)
    Q17_pressures = models.IntegerField(choices=degree_choices, verbose_name=u"",null=True)
    Q18_thematically = models.IntegerField(choices=degree_choices, verbose_name=u"",null=True)
    Q19_littelrule = models.IntegerField(choices=degree_choices, verbose_name=u"",null=True)
    Q20_difficultrule = models.IntegerField(choices=degree_choices, verbose_name=u"",null=True)
    Q21_thematically = models.IntegerField(choices=degree_choices, verbose_name=u"",null=True)
    Q22_dialectical = models.IntegerField(choices=degree_choices, verbose_name=u"",null=True)
    Q23_contradiction = models.IntegerField(choices=degree_choices, verbose_name=u"",null=True)
    Q24_pressures = models.IntegerField(choices=degree_choices, verbose_name=u"",null=True)
    Q25_thematically = models.IntegerField(choices=degree_choices, verbose_name=u"",null=True)

    class Meta:
        verbose_name = "Post问卷结果Three"
        verbose_name_plural = verbose_name


class Testing(models.Model):
    age = models.CharField(choices=((u"female", u"女"), (u"male", u"男"), (u"other", u"其他")),max_length=10, verbose_name=u"性别")

    class Meta:
        verbose_name = "测试"
        verbose_name_plural = verbose_name

