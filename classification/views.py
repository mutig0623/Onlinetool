# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
import json
import MySQLdb
from django.db import models
from django.contrib.auth.backends import ModelBackend
from users.models import *
from selected.models import *
from  classification.models import *
from  django.contrib.auth import authenticate,login
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers

import json



def home(request):
    return render(request, 'index.html', {})

def home1(request):
    return render(request,'HTML/CH/end.html',{})

def home2(request):
    return render(request, 'HTML/EN/end.html', {})

def home3(request):
    return render(request, 'HTML/DE/end.html', {})

def home4(request):
    return render(request, 'HTML/EN/Blank/introduction.html', {})


#跳转到中文介绍页面
def Chlink(request):
    return render(request, 'HTML/CH/indexCH.html', {})


# 跳转到中文instruction页面
def Chintro(request):
    return render(request,'HTML/CH/Instruction.html',{})


# 跳转到注册页面
def LogCh(request):
    return  render(request,'HTML/CH/login.html',{})


#  注册和登录操作，并跳转到pre-test.html
class LoginChView(View):
    def post(self,request):
        user_name = request.POST.get("username","")
        user_password = 0
        if UserProfile.objects.filter(username=user_name):
           return render(request, 'HTML/CH/login.html',{
                "msg":"信息已被注册，请用其他信息注册！"
            })
        userinfor = UserProfile()
        userinfor.username = user_name
        userinfor.password = user_password
        userinfor.start_time = datetime.now()
        userinfor.save()
        user = authenticate(username=user_name,password=user_password)
        if user is not None:
            login(request,user)
            return render(request,'HTML/CH/pre-test.html')


# 添加pre question到数据库，跳转到pre-test A.html
def PreAdd(request):
    if request.method == "POST":
        age = request.POST.get('age')
        sex = request.POST.get('sex')
        national = request.POST.get('national', "")
        livecountry = request.POST.get('othercontry',"")
        user_id = request.user.id
        mode = request.user.id % 4
        PreQuestionResult.objects.create(mode_id=mode, Q1_age=age, Q2_gender=sex, Q3_nationa=national, livecountry=livecountry,Test_User_id=user_id,)
        if livecountry == "YES":
           return render(request, 'HTML/CH/pre-testA.html', {})
        else:
           return render(request,'HTML/CH/pre-testB.html',{})


# 添加pre questionA 到数据库，跳转到pre-test B.html
def PreAddA(request):
    if request.method == "POST":
        country = request.POST.get('countryname', "")
        longst = request.POST.get('yearslong', "")
        F1 = request.POST.get('F1', )
        F2 = request.POST.get('F2', )
        F3 = request.POST.get('F3', )
        F4 = request.POST.get('F4', )
        F5 = request.POST.get('F5', )
        F6 = request.POST.get('F6', )
        user_id = request.user.id
        mode = request.user.id % 4
        PreQuestionResult.objects.filter(Test_User_id=user_id).update(CountryName=country, CountryYears=longst, FC_1=F1,FC_2=F2, FC_3=F3, FC_4=F4, FC_5=F5, FC_6=F6, )
        return render(request,'HTML/CH/pre-testB.html',{})


# 添加pre questionA 到数据库，跳转到pre-test B.html
def PreAddB(request):
    if request.method == "POST":
        edu = request.POST.get('edu')
        eduother = request.POST.get('eduother')
        role = request.POST.getlist('role')
        roleother = request.POST.get('roleother', "")
        years = request.POST.get('years', "0")
        pronu = request.POST.get('pronu')
        cours = request.POST.get('cours')
        tech = request.POST.get('tech')
        samtech = request.POST.getlist('samtech')
        user_id = request.user.id
        mode = request.user.id % 4
        PreQuestionResult.objects.filter(Test_User_id=user_id).update(mode_id=mode,
                                         Q4_educationlevel=edu, Q41_educationlevel=eduother, Q6_role=role,
                                         Q61_role=roleother, Q7_fulltime=years, Q8_ProjectCount=pronu,
                                         Q9_DesigCourse=cours, Q10_UsedTechnique=tech,
                                         Q11_FamiliarTechnique=samtech, )
    return render(request, 'HTML/CH/pre-test 1.html', {})


# 存数据到Pre-testB表中,跳转到pre-test 2.html
def PreAdd1(request):
    if request.method == "POST":
        que1 = request.POST.get('que11')
        que2 = request.POST.get('que12')
        que3 = request.POST.get('que13')
        que4 = request.POST.get('que14')
        que5 = request.POST.get('que15')
        que6 = request.POST.get('que16')
        que7 = request.POST.get('que17')
        user_id = request.user.id
        mode = request.user.id % 4
        PreQuestionResult.objects.filter(Test_User_id=user_id).update( Q12_knewpretty=que1, Q13_experts=que2, Q14_knewless=que3, Q15_donotknow=que4,
                                         Q16_donotfeel=que5, Q17_lotofexperiences=que6, Q18_familiar=que7,)

        return render(request,'HTML/CH/pre-test 2.html',{})


 # 存数据到pre-test2表中，判断跳转到哪个introduction页面中

def PreAdd2(request):
    if request.method == "POST":
        que8 = request.POST.get('que18')
        que9 = request.POST.get('que19')
        que10 = request.POST.get('que20')
        que11 = request.POST.get('que21')
        que12 = request.POST.get('que22')
        que13 = request.POST.get('que23')
        que14 = request.POST.get('que24')
        que15 = request.POST.get('que25')
        que16 = request.POST.get('que26')
        que17 = request.POST.get('que27')
        que18 = request.POST.get('que28')
        que19 = request.POST.get('que29')
        que20 = request.POST.get('que30')
        que21 = request.POST.get('que31')
        user_id = request.user.id
        mode = request.user.id % 4
        PreQuestionResult.objects.filter(Test_User_id=user_id).update(Q19_focusobjects=que8, Q20_basedcategories=que9, Q21_easylearncategories=que10,
                                         Q22_organizefunctionally=que11, Q23_useformallogic=que12,
                                         Q24_adherelogicalrules=que13, Q25_individualbehavior=que14,
                                         Q26_focussurobj=que15, Q27_focussurfeld=que16, Q28_difflearncate=que17,
                                         Q29_organthematically=que18, Q30_diareasoning=que19, Q31_preflogic=que20,
                                         Q32_peopbehav=que21,)
        if mode == 0:
            return render(request, 'HTML/CH/Top-down/introduction.html', {})
        elif mode == 1:
            return render(request, 'HTML/CH/Bottom-up/introduction.html', {})
        elif mode == 2:
            return render(request, 'HTML/CH/Tag-Cloud/introduction.html', {})
        else:
            return render(request, 'HTML/CH/Blank/introduction.html', {})


#跳转到Top-down的intro-test页面
def CHIntrotop(request):
    return render(request,'HTML/CH/Top-down/intro-test.html',{})

#判断回答是否正确
def Checktop(request):
    if request.method =="POST":
        test1 = request.POST.get('test1')
        test2 = request.POST.get('test2')
        test3 = request.POST.get('test3')
        if test1 =="1" and test2 == "2" and test3 =="1" :
            TaskDes = TaskDescriptionCH.objects.all()
            taskdes = TaskDes.filter(id=1)
            return render(request, 'HTML/CH/TaskDetail.html', {"taskdes": taskdes, })
        else:
            return render(request,'HTML/CH/Top-down/intro-again.html',{})


#跳转到Bottom的intro-test页面
def CHIntroup(request):
    return render(request,'HTML/CH/Bottom-up/intro-test.html',{})

#判断回答是否正确
def Checkup(request):
    if request.method =="POST":
        test1 = request.POST.get('test1')
        test2 = request.POST.get('test2')
        test3 = request.POST.get('test3')
        if test1 =="1" and test2 == "2" and test3 =="1" :
            TaskDes = TaskDescriptionCH.objects.all()
            taskdes = TaskDes.filter(id=1)
            return render(request, 'HTML/CH/TaskDetail.html', {"taskdes": taskdes, })
        else:
            return render(request,'HTML/CH/Bottom-up/intro-again.html',{})

#跳转到Tag-Cloud的intro-test页面
def CHIntrotag(request):
    return render(request,'HTML/CH/Tag-Cloud/intro-test.html',{})

#判断回答是否正确
def Checktag(request):
    if request.method =="POST":
        test1 = request.POST.get('test1')
        test2 = request.POST.get('test2')
        test3 = request.POST.get('test3')
        if test1 =="1" and test2 == "2" and test3 =="1":
            TaskDes = TaskDescriptionCH.objects.all()
            taskdes = TaskDes.filter(id=1)
            return render(request, 'HTML/CH/TaskDetail.html', {"taskdes": taskdes, })
        else:
            return render(request,'HTML/CH/Tag-Cloud/intro-again.html',{})

#跳转到Blank的intro-test页面
def CHIntroblank(request):
    return render(request,'HTML/CH/Blank/intro-test.html',{})

#判断回答是否正确
def Checkblank(request):
    if request.method =="POST":
        test1 = request.POST.get('test1')
        test2 = request.POST.get('test2')
        if test1 =="1" and test2 == "2" :
            TaskDes = TaskDescriptionCH.objects.all()
            taskdes = TaskDes.filter(id=1)
            return render(request, 'HTML/CH/TaskDetail.html', {"taskdes": taskdes, })
        else:
            return render(request,'HTML/CH/Blank/intro-again.html',{})




# 判断去哪个中文页面
def SwitchCH(request):
    user_id = request.user.id
    mode_id = user_id % 4
    # 跳转到Top-down页面
    if mode_id == 0:
        task_all= TaskDescriptionCH.objects.all()
        taskdes = task_all.filter(id=1)
        all_techch = TechinforCH.objects.all().order_by('?')
        attribut1 = TDDesignCH.objects.all()
        attribut2 = TDDependencyCH.objects.all()
        attribut3 = TDDurationCH.objects.all()
        attribut4 = TDParticipationCH.objects.all()
        attribut5 = TDEvaluationCH.objects.all()
        user_id = request.user.id

        design_id = request.GET.get('design', "")
        if design_id:
            all_techch = all_techch.filter(TDDesign_id=int(design_id))

        dependency_id = request.GET.get('dependency', "")
        if dependency_id:
            all_techch = all_techch.filter(TDDependency_id=int(dependency_id))

        duration_id = request.GET.get('duration', "")
        if duration_id:
            all_techch = all_techch.filter(TDDuration_id=int(duration_id))

        participant_id = request.GET.get('participant', "")
        if participant_id:
            all_techch = all_techch.filter(TDParticipation_id=int(participant_id))

        evaluation_id = request.GET.get('evaluation', "")
        if evaluation_id:
            all_techch = all_techch.filter(TDEvaluation_id=int(evaluation_id))
        return render(request, 'HTML/CH/Top-down/Top-down1.html',
                      {"all_techch": all_techch, "attribut1": attribut1, "attribut2": attribut2, "attribut3": attribut3,
                       "attribut4": attribut4, "attribut5": attribut5, "design_id": design_id,
                       "dependency_id": dependency_id, "duration_id": duration_id, "participant_id": participant_id,
                        "evaluation_id": evaluation_id,"taskdes":taskdes,
                       })
    # 跳转到Bottom-up页面
    elif mode_id == 1:
        task_all = TaskDescriptionCH.objects.all()
        task = task_all.filter(id=1)
        all_techch = TechinforCH.objects.all().order_by('?')
        attribut1 = BUDesignCH.objects.all()
        attribut2 = BUCollectionCH.objects.all()
        attribut3 = BUDurationCH.objects.all()
        attribut4 = BUParticipantCH.objects.all()

        de_id = request.GET.get('de', "")
        if de_id:
            all_techch = all_techch.filter(BUDesign_id=int(de_id))

        col_id = request.GET.get('col', "")
        if col_id:
            all_techch = all_techch.filter(BUCollection_id=int(col_id))

        du_id = request.GET.get('du', "")
        if du_id:
            all_techch = all_techch.filter(BUCollection_id=int(du_id))

        pa_id = request.GET.get('pa', "")
        if pa_id:
            all_techch = all_techch.filter(BUParticipant_id=int(pa_id))

        return render(request, 'HTML/CH/Bottom-up/Bottom-up1.html',
                      {"all_techch": all_techch, "attribut1": attribut1, "attribut2": attribut2, "attribut3": attribut3,
                       "attribut4": attribut4, "de_id": de_id, "col_id": col_id, "du_id": du_id, "pa_id": pa_id, "task":task,
                       })
    # 跳转到Tag Cloud页面
    elif mode_id == 2:
        all_techch = TechinforCH.objects.all().order_by('?')
        attribut1 = TagCloudCH.objects.all()
        task_all=TaskDescriptionCH.objects.all()
        task = task_all.filter(id=1)
        attri1_id = request.GET.get('attri1', "")
        if attri1_id:
            all_techch = all_techch.filter(UserParticipationgroup=attri1_id)

        attri2_id = request.GET.get('attri2', "")
        if attri2_id:
            all_techch = all_techch.filter(MidDuration=attri2_id)

        attri3_id = request.GET.get('attri3', "")
        if attri3_id:
            all_techch = all_techch.filter(Observation=attri3_id)

        attri4_id = request.GET.get('attri4', "")
        if attri4_id:
            all_techch = all_techch.filter(IdeaGeneration=attri4_id)

        attri5_id = request.GET.get('attri5', "")
        if attri5_id:
            all_techch = all_techch.filter(CollaborationStakeholders=attri5_id)

        attri6_id = request.GET.get('attri6', "")
        if attri6_id:
            all_techch = all_techch.filter(FeedbackOnline=attri6_id)

        attri7_id = request.GET.get('attri7', "")
        if attri7_id:
            all_techch = all_techch.filter(PrototypeEvaluation=attri7_id)

        attri8_id = request.GET.get('attri8', "")
        if attri8_id:
            all_techch = all_techch.filter(DataCollection=attri8_id)

        attri9_id = request.GET.get('attri9', "")
        if attri9_id:
            all_techch = all_techch.filter(Prototyping=attri9_id)

        attri10_id = request.GET.get('attri10', "")
        if attri10_id:
            all_techch = all_techch.filter(ShortDuration=attri10_id)

        attri11_id = request.GET.get('attri11', "")
        if attri11_id:
            all_techch = all_techch.filter(Evaluation=attri11_id)

        attri12_id = request.GET.get('attri12', "")
        if attri12_id:
            all_techch = all_techch.filter(ProductEvaluation=attri12_id)

        attri13_id = request.GET.get('attri13', "")
        if attri13_id:
            all_techch = all_techch.filter(ProjectOrganization=attri13_id)

        attri14_id = request.GET.get('attri14', "")
        if attri14_id:
            all_techch = all_techch.filter(FlexibleLength=attri14_id)

        attri15_id = request.GET.get('attri15', "")
        if attri15_id:
            all_techch = all_techch.filter(UserParticipation=attri15_id)

        attri16_id = request.GET.get('attri16', "")
        if attri16_id:
            all_techch = all_techch.filter(InformationOrganization=attri16_id)

        attri17_id = request.GET.get('attri17', "")
        if attri17_id:
            all_techch = all_techch.filter(FeedbackOffline=attri17_id)

        attri18_id = request.GET.get('attri18', "")
        if attri18_id:
            all_techch = all_techch.filter(LongDuration=attri18_id)

        attri19_id = request.GET.get('attri19', "")
        if attri19_id:
            all_techch = all_techch.filter(UserResearch=attri19_id)

        attri20_id = request.GET.get('attri20', "")
        if attri20_id:
            all_techch = all_techch.filter(RelationshipDependency=attri20_id)

        attri21_id = request.GET.get('attri21', "")
        if attri21_id:
            all_techch = all_techch.filter(UserSimulation=attri21_id)

        attri22_id = request.GET.get('attri22', "")
        if attri22_id:
            all_techch = all_techch.filter(ExpertParticipation=attri22_id)

        attri23_id = request.GET.get('attri23', "")
        if attri23_id:
            all_techch = all_techch.filter(UXEvaluation=attri23_id)

        attri24_id = request.GET.get('attri24', "")
        if attri24_id:
            all_techch = all_techch.filter(FeedbackCollection=attri24_id)

        return render(request, 'HTML/CH/Tag-Cloud/Tag Cloud1.html',
                      {"all_techch": all_techch, "attribut1": attribut1, "attri1_id": attri1_id,
                       "attri2_id": attri2_id, "attri3_id": attri3_id, "attri4_id": attri4_id,
                       "attri5_id": attri5_id, "attri6_id": attri6_id, "attri7_id": attri7_id,
                       "attri8_id": attri8_id, "attri9_id": attri9_id, "attri10_id": attri10_id,
                       "attri11_id": attri11_id, "attri12_id": attri12_id, "attri13_id": attri13_id,
                       "attri14_id": attri14_id, "attri15_id": attri15_id, "attri16_id": attri16_id,
                       "attri17_id": attri17_id, "attri18_id": attri18_id, "attri19_id": attri19_id,
                       "attri20_id": attri20_id, "attri21_id": attri21_id, "attri22_id": attri22_id,
                       "attri23_id": attri23_id, "attri24_id": attri24_id,"task":task,
                       })
    # 跳转到blank页面
    else:
        tech = TechinforCH.objects.all().order_by('?')
        task_all=TaskDescriptionCH.objects.all()
        task=task_all.filter(id=1)
        return render(request, 'HTML/CH/Blank/blank1.html', {
            "tech": tech,
            "task":task,
        })



# 如果选择了Blank
# 添加选择的tech，并跳转到Post-question 1页面
def B_AddTech1(request):
    selected1 = request.POST.get('selectedone',"")
    selected2 = request.POST.get('selectedtwo',"")
    selected3 = request.POST.get('selectedthree',"")
    user_id = request.user.id
    mode_id = user_id % 4
    SelectedTechniqueOne.objects.create(chose_Tech1=selected1,chose_Tech2=selected2, chose_Tech3=selected3,Test_User_id=user_id,mode_id= mode_id )
    return render(request, 'HTML/CH/post-test Q3.html', { })


# 添加Post-question1A到数据库，跳转到post-test1B
def B_AddPost1A(request):
    if request.method == "POST":
        post1 = request.POST.get('post1')
        post2 = request.POST.get('post2')
        post3 = request.POST.get('post3')
        post4 = request.POST.get('post4')
        post5 = request.POST.get('post5')
        post6 = request.POST.get('post6')
        user_id = request.user.id
        mode = request.user.id % 4
        PostQuestionResultOne.objects.create(mode_id=mode,Test_User_id=user_id,Q1_proficiency=post1,Q2_globalapproach=post2,Q3_localizedapproach=post3,
                                             Q4_objects=post4,Q5_rulesbased=post5,Q6_learncategory=post6, )
    return render(request, 'HTML/CH/Blank/post-test1B.html',{ })


#添加Post-question1A到数据库，跳转到TaskDetail页面
def B_AddPost1B(request):
    if request.method == "POST":
        post7 = request.POST.get('post7')
        post8 = request.POST.get('post8')
        post9 = request.POST.get('post9')
        post10 = request.POST.get('post10')
        post11 = request.POST.get('post11')
        post12 = request.POST.get('post12')
        post13 = request.POST.get('post13')
        post14 = request.POST.get('post14')
        post15 = request.POST.get('post15')
        post16 = request.POST.get('post16')
        user_id = request.user.id
        mode = request.user.id % 4
        TaskDes = TaskDescriptionCH.objects.all()
        taskdes = TaskDes.filter(id=2)
        PostQuestionResultOne.objects.filter(Test_User_id=user_id).update(Q7_organize=post7,Q8_formallogic=post8,Q9_logicalrules=post9,
                                                                        Q10_individual=post10,Q11_surrounding=post11,Q12_littelrule=post12,
                                                                        Q13_difficultrule=post13,Q14_thematically=post14,Q15_dialectical=post15,Q16_contradiction=post16,)
    return render(request, 'HTML/CH/Blank/TaskDetailtwo.html', {"taskdes": taskdes, })


# 跳转到blank2，显示tech信息等内容
def CH_blank2(request):
    tech = TechinforCH.objects.all()
    task_all=TaskDescriptionCH.objects.all().order_by('?')
    task=task_all.filter(id=2)
    return render(request, 'HTML/CH/Blank/blank2.html', {
        "tech": tech,
        "task":task,
    })


# 添加选择技术到数据库，并跳转到post-question2页面
def B_AddTech2(request):
    selected1 = request.POST.get('selectedone',"")
    selected2 = request.POST.get('selectedtwo',"")
    selected3 = request.POST.get('selectedthree',"")
    user_id = request.user.id
    mode = request.user.id % 4
    taskdes_all = TaskDescriptionCH.objects.all()
    taskdes = taskdes_all.filter(id=2)
    SelectedTechniqueTwo.objects.create(mode_id=mode,chose_Tech1=selected1,chose_Tech2=selected2, chose_Tech3=selected3,Test_User_id=user_id )
    return render(request, 'HTML/CH/Blank/post-test2A.html',{
        "taskdes":taskdes,
    })


# 添加post-question2A 答案到数据库，并跳转到post-test 2B页面
def B_AddPost2A(request):
    if request.method == "POST":
        post1 = request.POST.get('post1')
        post2 = request.POST.get('post2')
        post3 = request.POST.get('post3')
        post4 = request.POST.get('post4')
        post5 = request.POST.get('post5')
        post6 = request.POST.get('post6')
        user_id = request.user.id
        mode = request.user.id % 4
        PostQuestionResultTwo.objects.create(mode_id=mode,Test_User_id=user_id,Q1_proficiency=post1,Q2_globalapproach=post2,Q3_localizedapproach=post3,Q4_objects=post4,Q5_rulesbased=post5,Q6_learncategory=post6,)

    return render(request,'HTML/CH/Blank/post-test2B.html',{})


#添加到Post-test2B，跳转到TaskDetail3页面
def B_AddPost2B(request):
    if request.method == "POST":
        post7 = request.POST.get('post7')
        post8 = request.POST.get('post8')
        post9 = request.POST.get('post9')
        post10 = request.POST.get('post10')
        post11 = request.POST.get('post11')
        post12 = request.POST.get('post12')
        post13 = request.POST.get('post13')
        post14 = request.POST.get('post14')
        post15 = request.POST.get('post15')
        post16 = request.POST.get('post16')
        user_id = request.user.id
        mode = request.user.id % 4
        TaskDes = TaskDescriptionCH.objects.all()
        taskdes = TaskDes.filter(id=3)
        PostQuestionResultTwo.objects.filter(Test_User_id=user_id).update(Q7_organize=post7,Q8_formallogic=post8,Q9_logicalrules=post9,Q10_individual=post10,Q11_surrounding=post11,Q12_littelrule=post12,
                                                                          Q13_difficultrule=post13,Q14_thematically=post14,Q15_dialectical=post15,
                                                                          Q16_contradiction=post16,)
    return render(request, 'HTML/CH/Blank/TaskDetailthree.html', {"taskdes": taskdes, })


# 跳转到blank3页面，并显示相关信息
def CH_blank3(request):
    tech = TechinforCH.objects.all().order_by('?')
    task_all=TaskDescriptionCH.objects.all()
    task=task_all.filter(id=3)
    return render(request, 'HTML/CH/Blank/blank3.html', {
        "tech": tech,
        "task":task,
    })


# 添加选中技术，并跳转到post-question 3页面
def B_AddTech3(request):
    selected1 = request.POST.get('selectedone',"")
    selected2 = request.POST.get('selectedtwo',"")
    selected3 = request.POST.get('selectedthree',"")
    user_id = request.user.id
    mode = request.user.id % 4
    taskdes_all = TaskDescriptionCH.objects.all()
    taskdes = taskdes_all.filter(id=3)
    SelectedTechniqueThree.objects.create(mode_id=mode,chose_Tech1=selected1,chose_Tech2=selected2, chose_Tech3=selected3,Test_User_id=user_id )
    return render(request, 'HTML/CH/post-test Q3.html',{
        "taskdes":taskdes,
    })


# 添加post-question3 到数据库，并转到post Q31页面
def AddPost3(request):
    if request.method == "POST":
        post1 = request.POST.get('post1')
        post2 = request.POST.get('post2')
        post3 = request.POST.get('post3')
        post4 = request.POST.get('post4')
        post5 = request.POST.get('post5')
        post6 = request.POST.get('post6')
        user_id = request.user.id
        mode = request.user.id % 4
        PostQuestionResultThree.objects.create(mode_id=mode,Test_User_id=user_id, Q1_proficiency=post1, Q2_globalapproach=post2,
                                             Q3_localizedapproach=post3, Q4_objects=post4, Q5_rulesbased=post5,
                                             Q6_learncategory=post6, )
    return render(request, 'HTML/CH/post-test Q3A.html', {})

#
def AddPost31(request):
    if request.method == "POST":
        post7 = request.POST.get('post7')
        post8 = request.POST.get('post8')
        post9 = request.POST.get('post9')
        post10 = request.POST.get('post10')
        post11 = request.POST.get('post11')
        post12 = request.POST.get('post12')
        post13 = request.POST.get('post13')
        post14 = request.POST.get('post14')
        post15 = request.POST.get('post15')
        post16 = request.POST.get('post16')
        user_id = request.user.id
        PostQuestionResultThree.objects.filter(Test_User_id=user_id).update(Q7_organize=post7, Q8_formallogic=post8,
                                             Q9_logicalrules=post9, Q10_individual=post10, Q11_surrounding=post11,
                                             Q12_littelrule=post12, Q13_difficultrule=post13,
                                             Q14_thematically=post14, Q15_dialectical=post15,
                                             Q16_contradiction=post16,)
    return render(request, 'HTML/CH/post-test Q3B.html', {})

def AddPost32(request):
    if request.method == "POST":
        post17 = request.POST.get('post17')
        post18 = request.POST.get('post18')
        post19 = request.POST.get('post19')
        post20 = request.POST.get('post20')
        post21 = request.POST.get('post21')
        post22 = request.POST.get('post22')
        user_id = request.user.id
        mode = request.user.id % 4
        PostQuestionResultThree.objects.filter(Test_User_id=user_id).update( Q17_pressures=post17,
                                             Q18_thematically=post18,Q19_littelrule=post19,Q20_difficultrule=post20,Q21_thematically=post21,
                                             Q22_dialectical=post22,)
        UserProfile.objects.filter(id=user_id).update(endtime=datetime.now(), mode_id=mode,)
        return render(request,'HTML/CH/end.html',{})







# 如果选择了Top-down
# 添加选择的tech，并跳转到Post-question 1页面
def T_AddTech1(request):
    selected1 = request.POST.get('selectedone',"")
    selected2 = request.POST.get('selectedtwo',"")
    selected3 = request.POST.get('selectedthree',"")
    user_id = request.user.id
    mode = request.user.id % 4
    SelectedTechniqueOne.objects.create(chose_Tech1=selected1,chose_Tech2=selected2, chose_Tech3=selected3,Test_User_id=user_id ,mode_id = mode)
    return render(request, 'HTML/CH/post-test Q3.html',{
    })


# 添加Post-question1B到数据库，并跳转到TaskDetailtwo页面
def T_AddPost1A(request):
    if request.method == "POST":
        post1 = request.POST.get('post1')
        post2 = request.POST.get('post2')
        post3 = request.POST.get('post3')
        post4 = request.POST.get('post4')
        post5 = request.POST.get('post5')
        post6 = request.POST.get('post6')

        user_id = request.user.id
        mode = request.user.id % 4
        PostQuestionResultOne.objects.create(mode_id=mode,Test_User_id=user_id,Q1_proficiency=post1,Q2_globalapproach=post2,Q3_localizedapproach=post3,
                                             Q4_objects=post4,Q5_rulesbased=post5,Q6_learncategory=post6,)


    return render(request, 'HTML/CH/Top-down/post-test1B.html',{

        })


#跳转到TaskDetail2页面
def T_AddPost1B(request):
    if request.method == "POST":
        post7 = request.POST.get('post7')
        post8 = request.POST.get('post8')
        post9 = request.POST.get('post9')
        post10 = request.POST.get('post10')
        post11 = request.POST.get('post11')
        post12 = request.POST.get('post12')
        post13 = request.POST.get('post13')
        post14 = request.POST.get('post14')
        post15 = request.POST.get('post15')
        post16 = request.POST.get('post16')
        user_id = request.user.id
        mode = request.user.id % 4
        PostQuestionResultOne.objects.filter(Test_User_id=user_id).update(Q7_organize=post7,Q8_formallogic=post8,Q9_logicalrules=post9,Q10_individual=post10,Q11_surrounding=post11,Q12_littelrule=post12,Q13_difficultrule=post13,Q14_thematically=post14,Q15_dialectical=post15,Q16_contradiction=post16, )
        TaskDes = TaskDescriptionCH.objects.all()
        taskdes = TaskDes.filter(id=2)
    return render(request, 'HTML/CH/Top-down/TaskDetailtwo.html',{
            "taskdes":taskdes,
        })

# 跳转到Top-down2，显示tech信息等内容
def CH_Top2(request):
    task_all = TaskDescriptionCH.objects.all()
    task = task_all.filter(id=2)
    all_techch = TechinforCH.objects.all().order_by('?')
    attribut1 = TDDesignCH.objects.all()
    attribut2 = TDDependencyCH.objects.all()
    attribut3 = TDDurationCH.objects.all()
    attribut4 = TDParticipationCH.objects.all()
    attribut5 = TDEvaluationCH.objects.all()
    user_id = request.user.id
    design_id = request.GET.get('design', "")
    if design_id:
        all_techch = all_techch.filter(TDDesign_id=int(design_id))


    dependency_id = request.GET.get('dependency', "")
    if dependency_id:
        all_techch = all_techch.filter(TDDependency_id=int(dependency_id))

    duration_id = request.GET.get('duration', "")
    if duration_id:
        all_techch = all_techch.filter(TDDuration_id=int(duration_id))

    participant_id = request.GET.get('participant', "")
    if participant_id:
        all_techch = all_techch.filter(TDParticipation_id=int(participant_id))

    evaluation_id = request.GET.get('evaluation', "")
    if evaluation_id:
        all_techch = all_techch.filter(TDEvaluation_id=int(evaluation_id))
    return render(request, 'HTML/CH/Top-down/Top-down2.html',
                  {"all_techch": all_techch, "attribut1": attribut1, "attribut2": attribut2, "attribut3": attribut3,
                   "attribut4": attribut4, "attribut5": attribut5, "design_id": design_id,
                   "dependency_id": dependency_id, "duration_id": duration_id, "participant_id": participant_id,
                   "evaluation_id": evaluation_id, "task": task, })

@csrf_exempt
def ajax_CH_Top_add(request):
    design = request.POST.get("desp1")
    dependency = request.POST.get("dep1")
    duration = request.POST.get("dur1")
    participant = request.POST.get("part1")
    evaluation = request.POST.get("evalu1")

    if design:
        if design == u'计划阶段':
            design2=2
            design3=3
            design4=4
        if design == u'草图阶段':
            design2=1
            design3=3
            design4=4
        if design == u'高保真模型阶段':
            design2=1
            design3=2
            design4=4
        if design == u'发布阶段':
            design2=1
            design3=2
            design4=3
    else:
        design2=256
        design3=256
        design4=256

    if dependency:
        if dependency == u'即时的':
            dependency1=2
        if dependency == u'回顾的':
            dependency1=1
    else:
        dependency1=256

    if duration:
        if duration == u'长期研究':
            duration1 = 2
        if duration == u'短期研究':
            duration1 = 1
    else:
        duration1 = 256

    if participant:
        if participant == u'有用户参与':
            participant1 = 2
        if participant == u'没有用户参与':
            participant1 = 1
    else:
        participant1 = 256

    if evaluation:
        if evaluation == u'问卷':
            evaluation1=2
            evaluation2=3
            evaluation3=4
            evaluation4=5
        if evaluation == u'访谈':
            evaluation1=1
            evaluation2=3
            evaluation3=4
            evaluation4=5
        if evaluation == u'实验':
            evaluation1=1
            evaluation2=2
            evaluation3=4
            evaluation4=5
        if evaluation == u'观察':
            evaluation1=1
            evaluation2=3
            evaluation3=2
            evaluation4=5
        if evaluation == u'小组讨论':
            evaluation1=1
            evaluation2=3
            evaluation3=4
            evaluation4=2
    else:
        evaluation1=256
        evaluation2=256
        evaluation3=256
        evaluation4=256
    Tech_infor = TechinforCH.objects.exclude(TDDesign_id=design2).exclude(TDDesign_id=design3).exclude(TDDesign_id=design4).exclude(TDDependency_id=dependency1).exclude(TDDuration_id=duration1).exclude(TDParticipation_id=participant1).exclude(TDEvaluation_id=evaluation1).exclude(TDEvaluation_id=evaluation2).exclude(TDEvaluation_id=evaluation3).exclude(TDEvaluation_id=evaluation4).order_by('?')
    Tech_infor = serializers.serialize("json", list(Tech_infor))
    return HttpResponse(Tech_infor, content_type='application/json')


@csrf_exempt
def ajax_DE_Top_add(request):
    design = request.POST.get("desp1")
    dependency = request.POST.get("dep1")
    duration = request.POST.get("dur1")
    participant = request.POST.get("part1")
    evaluation = request.POST.get("evalu1")

    if design:
        if design == "Plannung":
            design2=2
            design3=3
            design4=4
        if design == "Entwurfsprototyp":
            design2=1
            design3=3
            design4=4
        if design == "Detaillierter Prototyp":
            design2=1
            design3=2
            design4=4
        if design == "Launch":
            design2=1
            design3=2
            design4=3
    else:
        design2=256
        design3=256
        design4=256

    if dependency:
        if dependency == "Echtzeit":
            dependency1=2
        if dependency == "Retrospektiv":
            dependency1=1
    else:
        dependency1=256

    if duration:
        if duration == "Längerer Zeitraum":
            duration1 = 2
        if duration == "Kurzer Zeitraum":
            duration1 = 1
    else:
        duration1 = 256

    if participant:
        if participant == "Nutzereinbindung":
            participant1 = 2
        if participant == "Ohne reale Nutzer":
            participant1 = 1
    else:
        participant1 = 256

    if evaluation:
        if evaluation == "Fragebogen":
            evaluation1=2
            evaluation2=3
            evaluation3=4
            evaluation4=5
        if evaluation == "Interview":
            evaluation1=1
            evaluation2=3
            evaluation3=4
            evaluation4=5
        if evaluation == "Experiment":
            evaluation1=1
            evaluation2=2
            evaluation3=4
            evaluation4=5
        if evaluation == "Beobachtung":
            evaluation1=1
            evaluation2=3
            evaluation3=2
            evaluation4=5
        if evaluation == "Gruppendiskussion":
            evaluation1=1
            evaluation2=3
            evaluation3=4
            evaluation4=2
    else:
        evaluation1=256
        evaluation2=256
        evaluation3=256
        evaluation4=256
    Tech_infor = TechinforDE.objects.exclude(TDDesign_id=design2).exclude(TDDesign_id=design3).exclude(TDDesign_id=design4).exclude(TDDependency_id=dependency1).exclude(TDDuration_id=duration1).exclude(TDParticipation_id=participant1).exclude(TDEvaluation_id=evaluation1).exclude(TDEvaluation_id=evaluation2).exclude(TDEvaluation_id=evaluation3).exclude(TDEvaluation_id=evaluation4).order_by('?')
    Tech_infor = serializers.serialize("json", list(Tech_infor))
    print(design2)
    return HttpResponse(Tech_infor, content_type='application/json')


@csrf_exempt
def ajax_EN_Top_add(request):
    design = request.POST.get("desp1")
    dependency = request.POST.get("dep1")
    duration = request.POST.get("dur1")
    participant = request.POST.get("part1")
    evaluation = request.POST.get("evalu1")

    if design:
        if design == "Planning":
            design2=2
            design3=3
            design1=4
        if design == "Low-fidelity prototyping":
            design2=1
            design3=3
            design1=4
        if design == "High-fidelity prototyping":
            design2=1
            design3=2
            design1=4
        if design == "Release":
            design2=1
            design3=2
            design1=3
    else:
        design2=256
        design3=256
        design1=256

    if dependency:
        if dependency == "Real-time":
            dependency1=2
        if dependency == "Retrospective":
            dependency1=1
    else:
        dependency1=256

    if duration:
        if duration == "Long-term":
            duration1 = 2
        if duration == "Short-term":
            duration1 = 1
    else:
        duration1 = 256

    if participant:
        if participant == "User attendance":
            participant1 = 2
        if participant == "User absence":
            participant1 = 1
    else:
        participant1 = 256

    if evaluation:
        if evaluation == "Questionnaire":
            evaluation1=2
            evaluation2=3
            evaluation3=4
            evaluation4=5
        if evaluation == "Interview":
            evaluation1=1
            evaluation2=3
            evaluation3=4
            evaluation4=5
        if evaluation == "Experiment":
            evaluation1=1
            evaluation2=2
            evaluation3=4
            evaluation4=5
        if evaluation == "Observation":
            evaluation1=1
            evaluation2=3
            evaluation3=2
            evaluation4=5
        if evaluation == "Group discussion":
            evaluation1=1
            evaluation2=3
            evaluation3=4
            evaluation4=2
    else:
        evaluation1=256
        evaluation2=256
        evaluation3=256
        evaluation4=256
    Tech_infor = TechinforEN.objects.exclude(TDDesign_id=design3).exclude(TDDesign_id=design2).exclude(TDDesign_id=design1).exclude(TDDependency_id=dependency1).exclude(TDDuration_id=duration1).exclude(TDParticipation_id=participant1).exclude(TDEvaluation_id=evaluation1).exclude(TDEvaluation_id=evaluation2).exclude(TDEvaluation_id=evaluation3).exclude(TDEvaluation_id=evaluation4).order_by('?')
    Tech_infor = serializers.serialize("json", list(Tech_infor))
    print(design1)
    print(design)
    print(Tech_infor)
    return HttpResponse(Tech_infor, content_type='application/json')


@csrf_exempt
def ajax_CH_Up_add(request):
    design = request.POST.get("des1")
    collection = request.POST.get("col1")
    duration = request.POST.get("dur1")
    participant = request.POST.get("part1")

    if design:
        if design == u'用户研究':
            design2=2
            design3=3
            design4=4
        if design == u'产生想法':
            design2=1
            design3=3
            design4=4
        if design == u'模型评价':
            design2=1
            design3=2
            design4=4
        if design == u'产品评价':
            design2=1
            design3=2
            design4=3
    else:
        design2=256
        design3=256
        design4=256

    if duration:
        if duration == u'短期':
            duration1 = 2
            duration2 = 3
        if duration == u'长期':
            duration1 = 1
            duration2 = 3
        if duration == u'时间灵活':
            duration1 = 1
            duration2 = 2
    else:
        duration1 = 256
        duration2 = 256

    if participant:
        if participant == u'用户':
            participant1 = 2
            participant2 = 3
        if participant == u'利益共享者':
            participant1 = 1
            participant2 = 3
        if participant == u'专家':
            participant1 = 1
            participant2 = 2
    else:
        participant1 = 256
        participant2 = 256

    if collection:
        if collection == u'组织信息':
            collection1 = 2
            collection2 = 3
            collection3 = 4
            collection4 = 5
            collection5 = 6
            collection6 = 7
        if collection == u'观察':
            collection1 = 1
            collection2 = 3
            collection3 = 4
            collection4 = 5
            collection5 = 6
            collection6 = 7
        if collection == u'用户模拟':
            collection1 = 1
            collection2 = 2
            collection3 = 4
            collection4 = 5
            collection5 = 6
            collection6 = 7
        if collection == u'关系和依赖':
            collection1 = 1
            collection2 = 3
            collection3 = 2
            collection4 = 5
            collection5 = 6
            collection6 = 7
        if collection == u'模型制作':
            collection1 = 2
            collection2 = 3
            collection3 = 4
            collection4 = 1
            collection5 = 6
            collection6 = 7
        if collection == u'收集反馈':
            collection1 = 2
            collection2 = 3
            collection3 = 4
            collection4 = 1
            collection5 = 5
            collection6 = 7
        if collection == u'用户体验反馈':
            collection1 = 2
            collection2 = 3
            collection3 = 4
            collection4 = 1
            collection5 = 6
            collection6 = 5
    else:
        collection1 = 256
        collection2 = 256
        collection3 = 256
        collection4 = 256
        collection5 = 256
        collection6 = 256
    Tech_infor = TechinforCH.objects.exclude(BUDesign_id=design2).exclude(BUDesign_id=design3).exclude(BUDesign_id=design4).exclude(BUDuration_id=duration1).exclude(BUDuration_id=duration2).exclude(BUParticipant_id=participant1).exclude(BUParticipant_id=participant2).exclude(BUCollection_id=collection1).exclude(BUCollection_id=collection2).exclude(BUCollection_id=collection3).exclude(BUCollection_id=collection4).exclude(BUCollection_id=collection5).exclude(BUCollection_id=collection6).order_by('?')
    Tech_infor = serializers.serialize("json", list(Tech_infor))
    return HttpResponse(Tech_infor, content_type='application/json')


@csrf_exempt
def ajax_DE_Up_add(request):
    design = request.POST.get("des1")
    collection = request.POST.get("col1")
    duration = request.POST.get("dur1")
    participant = request.POST.get("part1")

    if design:
        if design == "Nutzerforschung":
            design2=2
            design3=3
            design4=4
        if design == "Ideengenerierung":
            design2=1
            design3=3
            design4=4
        if design == "Prototyp-evaluation":
            design2=1
            design3=2
            design4=4
        if design == "Produkt-evaluation":
            design2=1
            design3=2
            design4=3
    else:
        design2=256
        design3=256
        design4=256

    if duration:
        if duration == "Kurzer Zeitraum":
            duration1 = 2
            duration2 = 3
        if duration == "Längerer Zeitraum":
            duration1 = 1
            duration2 = 3
        if duration == "Flexbiler Zeitraum":
            duration1 = 1
            duration2 = 2
    else:
        duration1 = 256
        duration2 = 256

    if participant:
        if participant == "Nutzer":
            participant1 = 2
            participant2 = 3
        if participant == "Interessenvertreter":
            participant1 = 1
            participant2 = 3
        if participant == "Experte":
            participant1 = 1
            participant2 = 2
    else:
        participant1 = 256
        participant2 = 256

    if collection:
        if collection == "Informations-organisation":
            collection1 = 2
            collection2 = 3
            collection3 = 4
            collection4 = 5
            collection5 = 6
            collection6 = 7
        if collection == "Beobachtung":
            collection1 = 1
            collection2 = 3
            collection3 = 4
            collection4 = 5
            collection5 = 6
            collection6 = 7
        if collection == "Benutzersimulation":
            collection1 = 1
            collection2 = 2
            collection3 = 4
            collection4 = 5
            collection5 = 6
            collection6 = 7
        if collection == "Beziehung und Abhängigkeit":
            collection1 = 1
            collection2 = 3
            collection3 = 2
            collection4 = 5
            collection5 = 6
            collection6 = 7
        if collection == "Prototyping":
            collection1 = 2
            collection2 = 3
            collection3 = 4
            collection4 = 1
            collection5 = 6
            collection6 = 7
        if collection == "Feedbacksammlung":
            collection1 = 2
            collection2 = 3
            collection3 = 4
            collection4 = 1
            collection5 = 5
            collection6 = 7
        if collection == "UX Evaluation":
            collection1 = 2
            collection2 = 3
            collection3 = 4
            collection4 = 1
            collection5 = 6
            collection6 = 5
    else:
        collection1 = 256
        collection2 = 256
        collection3 = 256
        collection4 = 256
        collection5 = 256
        collection6 = 256
    Tech_infor = TechinforDE.objects.exclude(BUDesign_id=design2).exclude(BUDesign_id=design3).exclude(BUDesign_id=design4).exclude(BUDuration_id=duration1).exclude(BUDuration_id=duration2).exclude(BUParticipant_id=participant1).exclude(BUParticipant_id=participant2).exclude(BUCollection_id=collection1).exclude(BUCollection_id=collection2).exclude(BUCollection_id=collection3).exclude(BUCollection_id=collection4).exclude(BUCollection_id=collection5).exclude(BUCollection_id=collection6).order_by('?')
    Tech_infor = serializers.serialize("json", list(Tech_infor))
    return HttpResponse(Tech_infor, content_type='application/json')


@csrf_exempt
def ajax_EN_Up_add(request):
    design = request.POST.get("des1")
    collection = request.POST.get("col1")
    duration = request.POST.get("dur1")
    participant = request.POST.get("part1")

    if design:
        if design == "User Research":
            design2=2
            design3=3
            design4=4
        if design == "Idea Generation":
            design2=1
            design3=3
            design4=4
        if design == "Prototype Evaluation":
            design2=1
            design3=2
            design4=4
        if design == "Product Evaluation":
            design2=1
            design3=2
            design4=3
    else:
        design2=256
        design3=256
        design4=256

    if duration:
        if duration == "Short-term":
            duration1 = 2
            duration2 = 3
        if duration == "Long-term":
            duration1 = 1
            duration2 = 3
        if duration == "Flexible":
            duration1 = 1
            duration2 = 2
    else:
        duration1 = 256
        duration2 = 256

    if participant:
        if participant == "User":
            participant1 = 2
            participant2 = 3
        if participant == "Stakeholder":
            participant1 = 1
            participant2 = 3
        if participant == "Expert":
            participant1 = 1
            participant2 = 2
    else:
        participant1 = 256
        participant2 = 256

    if collection:
        if collection == "Information Organization":
            collection1 = 2
            collection2 = 3
            collection3 = 4
            collection4 = 5
            collection5 = 6
            collection6 = 7
        if collection == "Observation":
            collection1 = 1
            collection2 = 3
            collection3 = 4
            collection4 = 5
            collection5 = 6
            collection6 = 7
        if collection == "User Simulation":
            collection1 = 1
            collection2 = 2
            collection3 = 4
            collection4 = 5
            collection5 = 6
            collection6 = 7
        if collection == "Relationship and Dependency":
            collection1 = 1
            collection2 = 3
            collection3 = 2
            collection4 = 5
            collection5 = 6
            collection6 = 7
        if collection == "Prototyping":
            collection1 = 2
            collection2 = 3
            collection3 = 4
            collection4 = 1
            collection5 = 6
            collection6 = 7
        if collection == "Feedback Collection":
            collection1 = 2
            collection2 = 3
            collection3 = 4
            collection4 = 1
            collection5 = 5
            collection6 = 7
        if collection == "UX Evaluation":
            collection1 = 2
            collection2 = 3
            collection3 = 4
            collection4 = 1
            collection5 = 6
            collection6 = 5
    else:
        collection1 = 256
        collection2 = 256
        collection3 = 256
        collection4 = 256
        collection5 = 256
        collection6 = 256
    Tech_infor = TechinforEN.objects.exclude(BUDesign_id=design2).exclude(BUDesign_id=design3).exclude(BUDesign_id=design4).exclude(BUDuration_id=duration1).exclude(BUDuration_id=duration2).exclude(BUParticipant_id=participant1).exclude(BUParticipant_id=participant2).exclude(BUCollection_id=collection1).exclude(BUCollection_id=collection2).exclude(BUCollection_id=collection3).exclude(BUCollection_id=collection4).exclude(BUCollection_id=collection5).exclude(BUCollection_id=collection6).order_by('?')
    Tech_infor = serializers.serialize("json", list(Tech_infor))
    return HttpResponse(Tech_infor, content_type='application/json')


@csrf_exempt
def ajax_CH_Tag_add(request):
    TagValue1 = request.POST.get("TagValue1")
    TagValue2 = request.POST.get("TagValue2")
    TagValue3 = request.POST.get("TagValue3")
    TagValue4 = request.POST.get("TagValue4")
    TagValue5 = request.POST.get("TagValue5")
    TagValue6 = request.POST.get("TagValue6")
    TagValue7 = request.POST.get("TagValue7")
    TagValue8 = request.POST.get("TagValue8")
    TagValue9 = request.POST.get("TagValue9")
    TagValue10 = request.POST.get("TagValue10")
    TagValue11 = request.POST.get("TagValue11")
    TagValue12 = request.POST.get("TagValue12")
    TagValue13 = request.POST.get("TagValue13")
    TagValue14 = request.POST.get("TagValue14")
    TagValue15 = request.POST.get("TagValue15")
    TagValue16 = request.POST.get("TagValue16")
    TagValue17 = request.POST.get("TagValue17")
    TagValue18 = request.POST.get("TagValue18")
    TagValue19 = request.POST.get("TagValue19")
    TagValue20 = request.POST.get("TagValue20")
    TagValue21 = request.POST.get("TagValue21")
    TagValue22 = request.POST.get("TagValue22")
    TagValue23 = request.POST.get("TagValue23")
    TagValue24 = request.POST.get("TagValue24")
    if TagValue1 == u'用户参与（用户组）':
        tag1 = ""
    else:
        tag1 = 256

    if TagValue2 == u'中等长度的持续时间':
        tag2 = ""
    else:
        tag2 = 256

    if TagValue3 == u'观察':
        tag3 = ""
    else:
        tag3 = 256

    if TagValue4 == u'产生想法':
        tag4 = ""
    else:
        tag4 = 256

    if TagValue5 == u'与利益相关者合作':
        tag5 = ""
    else:
        tag5 = 256

    if TagValue6 == u'反馈收集（在线）':
        tag6 = ""
    else:
        tag6 = 256

    if TagValue7 == u'模型评估':
        tag7 = ""
    else:
        tag7 = 256

    if TagValue8 == u'数据收集':
        tag8 = ""
    else:
        tag8 = 256

    if TagValue9 == u'模型制作':
        tag9 = ""
    else:
        tag9 = 256

    if TagValue10 == u'短期的持续时间':
        tag10 = ""
    else:
        tag10 = 256

    if TagValue11 == u'评估':
        tag11 = ""
    else:
        tag11 = 256

    if TagValue12 == u'产品评估':
        tag12 = ""
    else:
        tag12 = 256

    if TagValue13 == u'项目管理':
        tag13 = ""
    else:
        tag13 = 256

    if TagValue14 == u'灵活的时间长度':
        tag14 = ""
    else:
        tag14 = 256

    if TagValue15 == u'用户参与':
        tag15 = ""
    else:
        tag15 = 256

    if TagValue16 == u'信息组织':
        tag16 = ""
    else:
        tag16 = 256

    if TagValue17 == u'反馈收集（离线）':
        tag17 = ""
    else:
        tag17 = 256

    if TagValue18 == u'长期的持续时间':
        tag18 = ""
    else:
        tag18 = 256

    if TagValue19 == u'用户研究':
        tag19 = ""
    else:
        tag19 = 256

    if TagValue20 == u'关系和依赖':
        tag20 = ""
    else:
        tag20 = 256

    if TagValue21 == u'用户模拟':
        tag21 = ""
    else:
        tag21 = 256

    if TagValue22 == u'专家参与':
        tag22 = ""
    else:
        tag22 = 256

    if TagValue23 == u'用户体验评估':
        tag23 = ""
    else:
        tag23 = 256

    if TagValue24 == u'反馈收集':
        tag24 = ""
    else:
        tag24 = 256
    Tech_infor = TechinforCH.objects.exclude(UserParticipationgroup=tag1).exclude(MidDuration=tag2).exclude(Observation=tag3).exclude(IdeaGeneration=tag4).exclude(CollaborationStakeholders=tag5).exclude(FeedbackOnline=tag6).exclude(PrototypeEvaluation=tag7).exclude(DataCollection=tag8).exclude(Prototyping=tag9).exclude(ShortDuration=tag10).exclude(Evaluation=tag11).exclude(ProductEvaluation=tag12).exclude(ProjectOrganization=tag13).exclude(FlexibleLength=tag14).exclude(UserParticipation=tag15).exclude(InformationOrganization=tag16).exclude(FeedbackOffline=tag17).exclude(LongDuration=tag18).exclude(UserResearch=tag19).exclude(RelationshipDependency=tag20).exclude(UserSimulation=tag21).exclude(ExpertParticipation=tag22).exclude(UXEvaluation=tag23).exclude(FeedbackCollection=tag24).order_by('?')
    Tech_infor = serializers.serialize("json", list(Tech_infor))
    return HttpResponse(Tech_infor, content_type='application/json')


@csrf_exempt
def ajax_DE_Tag_add(request):
    TagValue1 = request.POST.get("TagValue1")
    TagValue2 = request.POST.get("TagValue2")
    TagValue3 = request.POST.get("TagValue3")
    TagValue4 = request.POST.get("TagValue4")
    TagValue5 = request.POST.get("TagValue5")
    TagValue6 = request.POST.get("TagValue6")
    TagValue7 = request.POST.get("TagValue7")
    TagValue8 = request.POST.get("TagValue8")
    TagValue9 = request.POST.get("TagValue9")
    TagValue10 = request.POST.get("TagValue10")
    TagValue11 = request.POST.get("TagValue11")
    TagValue12 = request.POST.get("TagValue12")
    TagValue13 = request.POST.get("TagValue13")
    TagValue14 = request.POST.get("TagValue14")
    TagValue15 = request.POST.get("TagValue15")
    TagValue16 = request.POST.get("TagValue16")
    TagValue17 = request.POST.get("TagValue17")
    TagValue18 = request.POST.get("TagValue18")
    TagValue19 = request.POST.get("TagValue19")
    TagValue20 = request.POST.get("TagValue20")
    TagValue21 = request.POST.get("TagValue21")
    TagValue22 = request.POST.get("TagValue22")
    TagValue23 = request.POST.get("TagValue23")
    TagValue24 = request.POST.get("TagValue24")

    if TagValue1 == "Nutzereinbindung (Nutzergruppen)":
        tag1 = ""
    else:
        tag1 = 256

    if TagValue2 == "Mittlere Zeitraum":
        tag2 = ""
    else:
        tag2 = 256

    if TagValue3 == "Beobachtung":
        tag3 = ""
    else:
        tag3 = 256

    if TagValue4 == "Ideengenerierung":
        tag4 = ""
    else:
        tag4 = 256

    if TagValue5 == "Zusammenarbeit mit Interessenvertreter":
        tag5 = ""
    else:
        tag5 = 256

    if TagValue6 == "Feedbacksammlung (online)":
        tag6 = ""
    else:
        tag6 = 256

    if TagValue7 == "Prototypevaluation":
        tag7 = ""
    else:
        tag7 = 256

    if TagValue8 == "Datensammlung":
        tag8 = ""
    else:
        tag8 = 256

    if TagValue9 == "Prototyping":
        tag9 = ""
    else:
        tag9 = 256

    if TagValue10 == "Kurzer Zeitraum":
        tag10 = ""
    else:
        tag10 = 256

    if TagValue11 == "Evaluation":
        tag11 = ""
    else:
        tag11 = 256

    if TagValue12 == "Produktevaluation":
        tag12 = ""
    else:
        tag12 = 256

    if TagValue13 == "Projektmanagement":
        tag13 = ""
    else:
        tag13 = 256

    if TagValue14 == "Flexibler Zeitraum":
        tag14 = ""
    else:
        tag14 = 256

    if TagValue15 == "Nutzereinbindung":
        tag15 = ""
    else:
        tag15 = 256

    if TagValue16 == "Informationsorganisation":
        tag16 = ""
    else:
        tag16 = 256

    if TagValue17 == "Feedbacksammlung (offline)":
        tag17 = ""
    else:
        tag17 = 256

    if TagValue18 == "Längerer Zeitraum":
        tag18 = ""
    else:
        tag18 = 256

    if TagValue19 == "Nutzerforschung":
        tag19 = ""
    else:
        tag19 = 256

    if TagValue20 == "Beziehung und Abhängigkeit":
        tag20 = ""
    else:
        tag20 = 256

    if TagValue21 == "Nutzersimulation":
        tag21 = ""
    else:
        tag21 = 256

    if TagValue22 == "Expertenbeteiligung":
        tag22 = ""
    else:
        tag22 = 256

    if TagValue23 == "UX Evaluation":
        tag23 = ""
    else:
        tag23 = 256

    if TagValue24 == "Feedbacksammlung":
        tag24 = ""
    else:
        tag24 = 256
    Tech_infor = TechinforDE.objects.exclude(UserParticipationgroup=tag1).exclude(MidDuration=tag2).exclude(Observation=tag3).exclude(IdeaGeneration=tag4).exclude(CollaborationStakeholders=tag5).exclude(FeedbackOnline=tag6).exclude(PrototypeEvaluation=tag7).exclude(DataCollection=tag8).exclude(Prototyping=tag9).exclude(ShortDuration=tag10).exclude(Evaluation=tag11).exclude(ProductEvaluation=tag12).exclude(ProjectOrganization=tag13).exclude(FlexibleLength=tag14).exclude(UserParticipation=tag15).exclude(InformationOrganization=tag16).exclude(FeedbackOffline=tag17).exclude(LongDuration=tag18).exclude(UserResearch=tag19).exclude(RelationshipDependency=tag20).exclude(UserSimulation=tag21).exclude(ExpertParticipation=tag22).exclude(UXEvaluation=tag23).exclude(FeedbackCollection=tag24).order_by('?')
    Tech_infor = serializers.serialize("json", list(Tech_infor))
    return HttpResponse(Tech_infor, content_type='application/json')


@csrf_exempt
def ajax_EN_Tag_add(request):
    TagValue1 = request.POST.get("TagValue1")
    TagValue2 = request.POST.get("TagValue2")
    TagValue3 = request.POST.get("TagValue3")
    TagValue4 = request.POST.get("TagValue4")
    TagValue5 = request.POST.get("TagValue5")
    TagValue6 = request.POST.get("TagValue6")
    TagValue7 = request.POST.get("TagValue7")
    TagValue8 = request.POST.get("TagValue8")
    TagValue9 = request.POST.get("TagValue9")
    TagValue10 = request.POST.get("TagValue10")
    TagValue11 = request.POST.get("TagValue11")
    TagValue12 = request.POST.get("TagValue12")
    TagValue13 = request.POST.get("TagValue13")
    TagValue14 = request.POST.get("TagValue14")
    TagValue15 = request.POST.get("TagValue15")
    TagValue16 = request.POST.get("TagValue16")
    TagValue17 = request.POST.get("TagValue17")
    TagValue18 = request.POST.get("TagValue18")
    TagValue19 = request.POST.get("TagValue19")
    TagValue20 = request.POST.get("TagValue20")
    TagValue21 = request.POST.get("TagValue21")
    TagValue22 = request.POST.get("TagValue22")
    TagValue23 = request.POST.get("TagValue23")
    TagValue24 = request.POST.get("TagValue24")

    if TagValue1 == "User Participation (user group)":
        tag1 = ""
    else:
        tag1 = 256

    if TagValue2 == "Mid-term Duration":
        tag2 = ""
    else:
        tag2 = 256

    if TagValue3 == "Observation":
        tag3 = ""
    else:
        tag3 = 256

    if TagValue4 == "Idea generation":
        tag4 = ""
    else:
        tag4 = 256

    if TagValue5 == "Collaboration with Stakeholders":
        tag5 = ""
    else:
        tag5 = 256

    if TagValue6 == "Feedback Collection (Online)":
        tag6 = ""
    else:
        tag6 = 256

    if TagValue7 == "Prototype Evaluation":
        tag7 = ""
    else:
        tag7 = 256

    if TagValue8 == "Data Collection":
        tag8 = ""
    else:
        tag8 = 256

    if TagValue9 == "Prototyping":
        tag9 = ""
    else:
        tag9 = 256

    if TagValue10 == "Short-term Duration":
        tag10 = ""
    else:
        tag10 = 256

    if TagValue11 == "Evaluation":
        tag11 = ""
    else:
        tag11 = 256

    if TagValue12 == "Product Evaluation":
        tag12 = ""
    else:
        tag12 = 256

    if TagValue13 == "Project Management":
        tag13 = ""
    else:
        tag13 = 256

    if TagValue14 == "Flexible Time Length":
        tag14 = ""
    else:
        tag14 = 256

    if TagValue15 == "User Participation":
        tag15 = ""
    else:
        tag15 = 256

    if TagValue16 == "Information Organization":
        tag16 = ""
    else:
        tag16 = 256

    if TagValue17 == "Feedback Collection (Offline)":
        tag17 = ""
    else:
        tag17 = 256

    if TagValue18 == "Long term duration":
        tag18 = ""
    else:
        tag18 = 256

    if TagValue19 == "User Research":
        tag19 = ""
    else:
        tag19 = 256

    if TagValue20 == "Relationship and Dependency":
        tag20 = ""
    else:
        tag20 = 256

    if TagValue21 == "User Simulation":
        tag21 = ""
    else:
        tag21 = 256

    if TagValue22 == "Expert Participation":
        tag22 = ""
    else:
        tag22 = 256

    if TagValue23 == "UX Evaluation":
        tag23 = ""
    else:
        tag23 = 256

    if TagValue24 == "Feedback Collection":
        tag24 = ""
    else:
        tag24 = 256
    Tech_infor = TechinforEN.objects.exclude(UserParticipationgroup=tag1).exclude(MidDuration=tag2).exclude(Observation=tag3).exclude(IdeaGeneration=tag4).exclude(CollaborationStakeholders=tag5).exclude(FeedbackOnline=tag6).exclude(PrototypeEvaluation=tag7).exclude(DataCollection=tag8).exclude(Prototyping=tag9).exclude(ShortDuration=tag10).exclude(Evaluation=tag11).exclude(ProductEvaluation=tag12).exclude(ProjectOrganization=tag13).exclude(FlexibleLength=tag14).exclude(UserParticipation=tag15).exclude(InformationOrganization=tag16).exclude(FeedbackOffline=tag17).exclude(LongDuration=tag18).exclude(UserResearch=tag19).exclude(RelationshipDependency=tag20).exclude(UserSimulation=tag21).exclude(ExpertParticipation=tag22).exclude(UXEvaluation=tag23).exclude(FeedbackCollection=tag24).order_by('?')
    Tech_infor = serializers.serialize("json", list(Tech_infor))
    return HttpResponse(Tech_infor, content_type='application/json')


# 添加选择技术到数据库，并跳转到post-question2页面
def T_AddTech2(request):
    selected1 = request.POST.get('selectedone',"")
    selected2 = request.POST.get('selectedtwo',"")
    selected3 = request.POST.get('selectedthree',"")
    user_id = request.user.id
    mode = request.user.id % 4
    taskdes_all = TaskDescriptionCH.objects.all()
    taskdes = taskdes_all.filter(id=2)
    SelectedTechniqueTwo.objects.create(mode_id=mode,chose_Tech1=selected1,chose_Tech2=selected2, chose_Tech3=selected3,Test_User_id=user_id )
    return render(request, 'HTML/CH/Top-down/post-test2A.html', {
        "taskdes":taskdes,
    })


# 添加post-question2A 答案到数据库，并跳转到post-question2B页面
def T_AddPost2A(request):
    if request.method == "POST":
        post1 = request.POST.get('post1')
        post2 = request.POST.get('post2')
        post3 = request.POST.get('post3')
        post4 = request.POST.get('post4')
        post5 = request.POST.get('post5')
        post6 = request.POST.get('post6')
        user_id = request.user.id
        mode = request.user.id % 4
        PostQuestionResultTwo.objects.create(mode_id=mode,Test_User_id=user_id,Q1_proficiency=post1,Q2_globalapproach=post2,Q3_localizedapproach=post3,Q4_objects=post4,Q5_rulesbased=post5,Q6_learncategory=post6,
                                           )
        TaskDes = TaskDescriptionCH.objects.all()
        taskdes = TaskDes.filter(id=3)
    return render(request, 'HTML/CH/Top-down/post-test2B.html',{
            "taskdes":taskdes,
        })


# 添加post-question2B 答案到数据库，并跳转到TaskDetail 3页面
def T_AddPost2B(request):
    if request.method == "POST":
        post7 = request.POST.get('post7')
        post8 = request.POST.get('post8')
        post9 = request.POST.get('post9')
        post10 = request.POST.get('post10')
        post11 = request.POST.get('post11')
        post12 = request.POST.get('post12')
        post13 = request.POST.get('post13')
        post14 = request.POST.get('post14')
        post15 = request.POST.get('post15')
        post16 = request.POST.get('post16')
        user_id = request.user.id
        mode = request.user.id % 4
        PostQuestionResultTwo.objects.filter(Test_User_id=user_id).update(Q7_organize=post7,
                                             Q8_formallogic=post8, Q9_logicalrules=post9, Q10_individual=post10,
                                             Q11_surrounding=post11, Q12_littelrule=post12, Q13_difficultrule=post13,
                                             Q14_thematically=post14, Q15_dialectical=post15,
                                             Q16_contradiction=post16, )
        TaskDes = TaskDescriptionCH.objects.all()
        taskdes = TaskDes.filter(id=3)
    return render(request, 'HTML/CH/Top-down/TaskDetailthree.html', {"taskdes": taskdes, })


# 跳转到Top-down3页面，并显示相关信息
def CH_Top3(request):
    task_all = TaskDescriptionCH.objects.all()
    taskdes = task_all.filter(id=3)
    all_techch = TechinforCH.objects.all().order_by('?')
    attribut1 = TDDesignCH.objects.all()
    attribut2 = TDDependencyCH.objects.all()
    attribut3 = TDDurationCH.objects.all()
    attribut4 = TDParticipationCH.objects.all()
    attribut5 = TDEvaluationCH.objects.all()
    user_id = request.user.id
    design_id = request.GET.get('design', "")
    if design_id:
        all_techch = all_techch.filter(TDDesign_id=int(design_id))

    dependency_id = request.GET.get('dependency', "")
    if dependency_id:
        all_techch = all_techch.filter(TDDependency_id=int(dependency_id))

    duration_id = request.GET.get('duration', "")
    if duration_id:
        all_techch = all_techch.filter(TDDuration_id=int(duration_id))

    participant_id = request.GET.get('participant', "")
    if participant_id:
        all_techch = all_techch.filter(TDParticipation_id=int(participant_id))

    evaluation_id = request.GET.get('evaluation', "")
    if evaluation_id:
        all_techch = all_techch.filter(TDEvaluation_id=int(evaluation_id))
    return render(request, 'HTML/CH/Top-down/Top-down3.html',
                  {"all_techch": all_techch, "attribut1": attribut1, "attribut2": attribut2, "attribut3": attribut3,
                   "attribut4": attribut4, "attribut5": attribut5, "design_id": design_id,
                   "dependency_id": dependency_id, "duration_id": duration_id, "participant_id": participant_id,
                   "evaluation_id": evaluation_id, "taskdes": taskdes, })


# 添加选中技术，并跳转到post-question 3页面
def T_AddTech3(request):
    selected1 = request.POST.get('selectedone',"")
    selected2 = request.POST.get('selectedtwo',"")
    selected3 = request.POST.get('selectedthree',"")
    user_id = request.user.id
    mode = request.user.id % 4
    taskdes_all = TaskDescriptionCH.objects.all()
    taskdes = taskdes_all.filter(id=3)
    SelectedTechniqueThree.objects.create(mode_id=mode,chose_Tech1=selected1,chose_Tech2=selected2, chose_Tech3=selected3,Test_User_id=user_id )
    return render(request, 'HTML/CH/post-test Q3.html',{
        "taskdes":taskdes,
    })






# 如果选择了Bottom-up
# 添加选择的tech，并跳转到Post-question 1A页面
def U_AddTech1(request):
    selected1 = request.POST.get('selectedone',"")
    selected2 = request.POST.get('selectedtwo',"")
    selected3 = request.POST.get('selectedthree',"")
    user_id = request.user.id
    mode = request.user.id % 4
    SelectedTechniqueOne.objects.create(mode_id=mode,chose_Tech1=selected1,chose_Tech2=selected2, chose_Tech3=selected3,Test_User_id=user_id )
    return render(request, 'HTML/CH/post-test Q3.html',{
    })


# 添加Post-question1A到数据库，并跳转到Task-Detail 2页面
def U_AddPost1A(request):
    if request.method == "POST":
        post1 = request.POST.get('post1')
        post2 = request.POST.get('post2')
        post3 = request.POST.get('post3')
        post4 = request.POST.get('post4')
        post5 = request.POST.get('post5')
        post6 = request.POST.get('post6')
        user_id = request.user.id
        mode = request.user.id % 4
        PostQuestionResultOne.objects.create(mode_id=mode,Test_User_id=user_id,Q1_proficiency=post1,Q2_globalapproach=post2,Q3_localizedapproach=post3,Q4_objects=post4,Q5_rulesbased=post5,Q6_learncategory=post6,)
    return render(request, 'HTML/CH/Bottom-up/post-test1B.html',{
        })


 # 添加Post-question1B到数据库，并跳转到Task-Detail 2页面
def U_AddPost1B(request):
    if request.method == "POST":
        post7 = request.POST.get('post7')
        post8 = request.POST.get('post8')
        post9 = request.POST.get('post9')
        post10 = request.POST.get('post10')
        post11 = request.POST.get('post11')
        post12 = request.POST.get('post12')
        post13 = request.POST.get('post13')
        post14 = request.POST.get('post14')
        post15 = request.POST.get('post15')
        post16 = request.POST.get('post16')
        user_id = request.user.id
        mode = request.user.id % 4
        PostQuestionResultOne.objects.filter(Test_User_id=user_id).update(Q7_organize=post7,
                                             Q8_formallogic=post8, Q9_logicalrules=post9, Q10_individual=post10,
                                             Q11_surrounding=post11, Q12_littelrule=post12, Q13_difficultrule=post13,
                                             Q14_thematically=post14, Q15_dialectical=post15, Q16_contradiction=post16, )
        TaskDes = TaskDescriptionCH.objects.all()
        taskdes = TaskDes.filter(id=2)
    return render(request, 'HTML/CH/Bottom-up/TaskDetailtwo.html', {"taskdes": taskdes, })


# 跳转到Bottom-up2，显示tech信息等内容
def CH_Up2(request):
    task_all = TaskDescriptionCH.objects.all()
    task = task_all.filter(id=2)
    all_techch = TechinforCH.objects.all().order_by('?')
    attribut1 = BUDesignCH.objects.all()
    attribut2 = BUCollectionCH.objects.all()
    attribut3 = BUDurationCH.objects.all()
    attribut4 = BUParticipantCH.objects.all()
    de_id = request.GET.get('de', "")
    if de_id:
        all_techch = all_techch.filter(BUDesign_id=int(de_id))

    col_id = request.GET.get('col', "")
    if col_id:
        all_techch = all_techch.filter(BUCollection_id=int(col_id))

    du_id = request.GET.get('du', "")
    if du_id:
        all_techch = all_techch.filter(BUCollection_id=int(du_id))

    pa_id = request.GET.get('pa', "")
    if pa_id:
        all_techch = all_techch.filter(BUParticipant_id=int(pa_id))

    return render(request, 'HTML/CH/Bottom-up/Bottom-up2.html',
                  {"all_techch": all_techch, "attribut1": attribut1, "attribut2": attribut2, "attribut3": attribut3,
                   "attribut4": attribut4, "de_id": de_id, "col_id": col_id, "du_id": du_id, "pa_id": pa_id,
                   "task": task, })


# 添加选择技术到数据库，并跳转到post-question2A页面
def U_AddTech2(request):
    selected1 = request.POST.get('selectedone',"")
    selected2 = request.POST.get('selectedtwo',"")
    selected3 = request.POST.get('selectedthree',"")
    user_id = request.user.id
    mode = request.user.id % 4
    taskdes_all = TaskDescriptionCH.objects.all()
    taskdes = taskdes_all.filter(id=2)
    SelectedTechniqueOne.objects.create(mode_id=mode,chose_Tech1=selected1,chose_Tech2=selected2, chose_Tech3=selected3,Test_User_id=user_id )
    return render(request, 'HTML/CH/Bottom-up/post-test2A.html',{
        "taskdes":taskdes,
    })


# 添加post-question2A 答案到数据库，并跳转到post-test2B页面
def U_AddPost2A(request):
    if request.method == "POST":
        post1 = request.POST.get('post1')
        post2 = request.POST.get('post2')
        post3 = request.POST.get('post3')
        post4 = request.POST.get('post4')
        post5 = request.POST.get('post5')
        post6 = request.POST.get('post6')
        user_id = request.user.id
        mode = request.user.id % 4
        PostQuestionResultTwo.objects.create(mode_id=mode,Test_User_id=user_id,Q1_proficiency=post1,Q2_globalapproach=post2,Q3_localizedapproach=post3,
                                             Q4_objects=post4,Q5_rulesbased=post5,Q6_learncategory=post6,)
    return render(request, 'HTML/CH/Bottom-up/post-test2B.html',{

        })

# 添加post-question2A 答案到数据库，并跳转到post-question2B页面
def U_AddPost2B(request):
    if request.method == "POST":
        post7 = request.POST.get('post7')
        post8 = request.POST.get('post8')
        post9 = request.POST.get('post9')
        post10 = request.POST.get('post10')
        post11 = request.POST.get('post11')
        post12 = request.POST.get('post12')
        post13 = request.POST.get('post13')
        post14 = request.POST.get('post14')
        post15 = request.POST.get('post15')
        post16 = request.POST.get('post16')
        user_id = request.user.id
        mode = request.user.id % 4
        PostQuestionResultTwo.objects.filter(Test_User_id=user_id).update(
                                             Q8_formallogic=post8, Q9_logicalrules=post9, Q10_individual=post10,
                                             Q11_surrounding=post11, Q12_littelrule=post12, Q13_difficultrule=post13,
                                             Q14_thematically=post14, Q15_dialectical=post15, Q16_contradiction=post16, )
        TaskDes = TaskDescriptionCH.objects.all()
        taskdes = TaskDes.filter(id=3)
    return render(request, 'HTML/CH/Bottom-up/TaskDetailthree.html', {"taskdes": taskdes, })

# 跳转到Bottom-up 3页面，并显示相关信息
def CH_Up3(request):
    task_all = TaskDescriptionCH.objects.all()
    task = task_all.filter(id=3)
    all_techch = TechinforCH.objects.all().order_by('?')
    attribut1 = BUDesignCH.objects.all()
    attribut2 = BUCollectionCH.objects.all()
    attribut3 = BUDurationCH.objects.all()
    attribut4 = BUParticipantCH.objects.all()
    de_id = request.GET.get('de', "")
    if de_id:
        all_techch = all_techch.filter(BUDesign_id=int(de_id))

    col_id = request.GET.get('col', "")
    if col_id:
        all_techch = all_techch.filter(BUCollection_id=int(col_id))

    du_id = request.GET.get('du', "")
    if du_id:
        all_techch = all_techch.filter(BUCollection_id=int(du_id))

    pa_id = request.GET.get('pa', "")
    if pa_id:
        all_techch = all_techch.filter(BUParticipant_id=int(pa_id))

    return render(request, 'HTML/CH/Bottom-up/Bottom-up3.html',
                  {"all_techch": all_techch, "attribut1": attribut1, "attribut2": attribut2, "attribut3": attribut3,
                   "attribut4": attribut4, "de_id": de_id, "col_id": col_id, "du_id": du_id, "pa_id": pa_id,
                   "task": task, })


# 添加选中技术，并跳转到post-question 3页面
def U_AddTech3(request):
    selected1 = request.POST.get('selectedone',"")
    selected2 = request.POST.get('selectedtwo',"")
    selected3 = request.POST.get('selectedthree',"")
    user_id = request.user.id
    mode = request.user.id % 4
    taskdes_all = TaskDescriptionCH.objects.all()
    taskdes = taskdes_all.filter(id=3)
    SelectedTechniqueOne.objects.create(mode_id=mode,chose_Tech1=selected1,chose_Tech2=selected2, chose_Tech3=selected3,Test_User_id=user_id )
    return render(request, 'HTML/CH/post-test Q3.html',{
        "taskdes":taskdes,
    })




# 选择了Tag Cloud
# 添加选择的tech，并跳转到Post-question 1A页面
def C_AddTech1(request):
    selected1 = request.POST.get('selectedone',"")
    selected2 = request.POST.get('selectedtwo',"")
    selected3 = request.POST.get('selectedthree',"")
    user_id = request.user.id
    mode = request.user.id % 4
    SelectedTechniqueOne.objects.create(mode_id=mode,chose_Tech1=selected1,chose_Tech2=selected2, chose_Tech3=selected3,Test_User_id=user_id )
    return render(request, 'HTML/CH/post-test Q3.html',{
    })


# 添加Post-question1A到数据库，并跳转到Post-question1B页面
def C_AddPost1A(request):
    if request.method == "POST":
        post1 = request.POST.get('post1')
        post2 = request.POST.get('post2')
        post3 = request.POST.get('post3')
        post4 = request.POST.get('post4')
        post5 = request.POST.get('post5')
        post6 = request.POST.get('post6')
        user_id = request.user.id
        mode = request.user.id % 4
        PostQuestionResultOne.objects.create(mode_id=mode,Test_User_id=user_id,Q1_proficiency=post1,Q2_globalapproach=post2,Q3_localizedapproach=post3,Q4_objects=post4,Q5_rulesbased=post5,Q6_learncategory=post6,)
    return render(request, 'HTML/CH/Tag-Cloud/post-test1B.html',{

        })


# 添加Post-question1到数据库，并跳转到Task-Detail 2页面
def C_AddPost1B(request):
    if request.method == "POST":
        post7 = request.POST.get('post7')
        post8 = request.POST.get('post8')
        post9 = request.POST.get('post9')
        post10 = request.POST.get('post10')
        post11 = request.POST.get('post11')
        post12 = request.POST.get('post12')
        post13 = request.POST.get('post13')
        post14 = request.POST.get('post14')
        post15 = request.POST.get('post15')
        post16 = request.POST.get('post16')
        user_id = request.user.id
        mode = request.user.id % 4
        PostQuestionResultOne.objects.filter(Test_User_id=user_id).update(Q7_organize=post7,Q8_formallogic=post8,Q9_logicalrules=post9,Q10_individual=post10,Q11_surrounding=post11,Q12_littelrule=post12,Q13_difficultrule=post13,Q14_thematically=post14,Q15_dialectical=post15,Q16_contradiction=post16,)
        TaskDes = TaskDescriptionCH.objects.all()
        taskdes = TaskDes.filter(id=2)
    return render(request, 'HTML/CH/Tag-Cloud/TaskDetailtwo.html',{
            "taskdes":taskdes,
        })

# 跳转到blank2，显示tech信息等内容
def CH_C2(request):
    all_techch = TechinforCH.objects.all().order_by('?')
    attribut1 = TagCloudCH.objects.all()
    task_all = TaskDescriptionCH.objects.all()
    task = task_all.filter(id=2)

    attri1_id = request.GET.get('attri1', "")
    if attri1_id:
        all_techch = all_techch.filter(UserParticipationgroup=attri1_id)

    attri2_id = request.GET.get('attri2', "")
    if attri2_id:
        all_techch = all_techch.filter(MidDuration=attri2_id)

    attri3_id = request.GET.get('attri3', "")
    if attri3_id:
        all_techch = all_techch.filter(Observation=attri3_id)

    attri4_id = request.GET.get('attri4', "")
    if attri4_id:
        all_techch = all_techch.filter(IdeaGeneration=attri4_id)

    attri5_id = request.GET.get('attri5', "")
    if attri5_id:
        all_techch = all_techch.filter(CollaborationStakeholders=attri5_id)

    attri6_id = request.GET.get('attri6', "")
    if attri6_id:
        all_techch = all_techch.filter(FeedbackOnline=attri6_id)

    attri7_id = request.GET.get('attri7', "")
    if attri7_id:
        all_techch = all_techch.filter(PrototypeEvaluation=attri7_id)

    attri8_id = request.GET.get('attri8', "")
    if attri8_id:
        all_techch = all_techch.filter(DataCollection=attri8_id)

    attri9_id = request.GET.get('attri9', "")
    if attri9_id:
        all_techch = all_techch.filter(Prototyping=attri9_id)

    attri10_id = request.GET.get('attri10', "")
    if attri10_id:
        all_techch = all_techch.filter(ShortDuration=attri10_id)

    attri11_id = request.GET.get('attri11', "")
    if attri11_id:
        all_techch = all_techch.filter(Evaluation=attri11_id)

    attri12_id = request.GET.get('attri12', "")
    if attri12_id:
        all_techch = all_techch.filter(ProductEvaluation=attri12_id)

    attri13_id = request.GET.get('attri13', "")
    if attri13_id:
        all_techch = all_techch.filter(ProjectOrganization=attri13_id)

    attri14_id = request.GET.get('attri14', "")
    if attri14_id:
        all_techch = all_techch.filter(FlexibleLength=attri14_id)

    attri15_id = request.GET.get('attri15', "")
    if attri15_id:
        all_techch = all_techch.filter(UserParticipation=attri15_id)

    attri16_id = request.GET.get('attri16', "")
    if attri16_id:
        all_techch = all_techch.filter(InformationOrganization=attri16_id)

    attri17_id = request.GET.get('attri17', "")
    if attri17_id:
        all_techch = all_techch.filter(FeedbackOffline=attri17_id)

    attri18_id = request.GET.get('attri18', "")
    if attri18_id:
        all_techch = all_techch.filter(LongDuration=attri18_id)

    attri19_id = request.GET.get('attri19', "")
    if attri19_id:
        all_techch = all_techch.filter(UserResearch=attri19_id)

    attri20_id = request.GET.get('attri20', "")
    if attri20_id:
        all_techch = all_techch.filter(RelationshipDependency=attri20_id)

    attri21_id = request.GET.get('attri21', "")
    if attri21_id:
        all_techch = all_techch.filter(UserSimulation=attri21_id)

    attri22_id = request.GET.get('attri22', "")
    if attri22_id:
        all_techch = all_techch.filter(ExpertParticipation=attri22_id)

    attri23_id = request.GET.get('attri23', "")
    if attri23_id:
        all_techch = all_techch.filter(UXEvaluation=attri23_id)

    attri24_id = request.GET.get('attri24', "")
    if attri24_id:
        all_techch = all_techch.filter(FeedbackCollection=attri24_id)

    return render(request, 'HTML/CH/Tag-Cloud/Tag Cloud2.html', {
        "all_techch": all_techch,
        "task":task,
        "attribut1":attribut1,
    })


# 添加选择技术到数据库，并跳转到post-question2页面
def C_AddTech2(request):
    selected1 = request.POST.get('selectedone',"")
    selected2 = request.POST.get('selectedtwo',"")
    selected3 = request.POST.get('selectedthree',"")
    user_id = request.user.id
    mode = request.user.id % 4
    taskdes_all = TaskDescriptionCH.objects.all()
    taskdes = taskdes_all.filter(id=2)
    SelectedTechniqueOne.objects.create(mode_id=mode,chose_Tech1=selected1,chose_Tech2=selected2, chose_Tech3=selected3,Test_User_id=user_id )
    return render(request, 'HTML/CH/Tag-Cloud/post-test2A.html', {
        "taskdes":taskdes,
    })


# 添加post-question2A答案到数据库，并跳转到post-test2B页面
def C_AddPost2A(request):
    if request.method == "POST":
        post1 = request.POST.get('post1')
        post2 = request.POST.get('post2')
        post3 = request.POST.get('post3')
        post4 = request.POST.get('post4')
        post5 = request.POST.get('post5')
        post6 = request.POST.get('post6')
        user_id = request.user.id
        mode = request.user.id % 4
        PostQuestionResultTwo.objects.create(mode_id=mode,Test_User_id=user_id,Q1_proficiency=post1,Q2_globalapproach=post2,Q3_localizedapproach=post3,Q4_objects=post4,Q5_rulesbased=post5,Q6_learncategory=post6,)
    return render(request, 'HTML/CH/Tag-Cloud/post-test2B.html',{

        })


# 添加post-question2A答案到数据库，并跳转到TaskDetail 3页面
def C_AddPost2B(request):
        if request.method == "POST":
            post7 = request.POST.get('post7')
            post8 = request.POST.get('post8')
            post9 = request.POST.get('post9')
            post10 = request.POST.get('post10')
            post11 = request.POST.get('post11')
            post12 = request.POST.get('post12')
            post13 = request.POST.get('post13')
            post14 = request.POST.get('post14')
            post15 = request.POST.get('post15')
            post16 = request.POST.get('post16')
            user_id = request.user.id
            mode = request.user.id % 4
            PostQuestionResultTwo.objects.filter(Test_User_id=user_id).update(Q7_organize=post7,
                                                 Q8_formallogic=post8, Q9_logicalrules=post9, Q10_individual=post10,
                                                 Q11_surrounding=post11, Q12_littelrule=post12,
                                                 Q13_difficultrule=post13, Q14_thematically=post14,
                                                 Q15_dialectical=post15, Q16_contradiction=post16, )
            TaskDes = TaskDescriptionCH.objects.all()
            taskdes = TaskDes.filter(id=3)
        return render(request, 'HTML/CH/Tag-Cloud/TaskDetailthree.html', {"taskdes": taskdes, })


# 跳转到blank3页面，并显示相关信息
def CH_C3(request):
    all_techch = TechinforCH.objects.all().order_by('?')
    attribut1 = TagCloudCH.objects.all()
    task_all = TaskDescriptionCH.objects.all()
    task = task_all.filter(id=3)

    attri1_id = request.GET.get('attri1', "")
    if attri1_id:
        all_techch = all_techch.filter(UserParticipationgroup=attri1_id)

    attri2_id = request.GET.get('attri2', "")
    if attri2_id:
        all_techch = all_techch.filter(MidDuration=attri2_id)

    attri3_id = request.GET.get('attri3', "")
    if attri3_id:
        all_techch = all_techch.filter(Observation=attri3_id)

    attri4_id = request.GET.get('attri4', "")
    if attri4_id:
        all_techch = all_techch.filter(IdeaGeneration=attri4_id)

    attri5_id = request.GET.get('attri5', "")
    if attri5_id:
        all_techch = all_techch.filter(CollaborationStakeholders=attri5_id)

    attri6_id = request.GET.get('attri6', "")
    if attri6_id:
        all_techch = all_techch.filter(FeedbackOnline=attri6_id)

    attri7_id = request.GET.get('attri7', "")
    if attri7_id:
        all_techch = all_techch.filter(PrototypeEvaluation=attri7_id)

    attri8_id = request.GET.get('attri8', "")
    if attri8_id:
        all_techch = all_techch.filter(DataCollection=attri8_id)

    attri9_id = request.GET.get('attri9', "")
    if attri9_id:
        all_techch = all_techch.filter(Prototyping=attri9_id)

    attri10_id = request.GET.get('attri10', "")
    if attri10_id:
        all_techch = all_techch.filter(ShortDuration=attri10_id)

    attri11_id = request.GET.get('attri11', "")
    if attri11_id:
        all_techch = all_techch.filter(Evaluation=attri11_id)

    attri12_id = request.GET.get('attri12', "")
    if attri12_id:
        all_techch = all_techch.filter(ProductEvaluation=attri12_id)

    attri13_id = request.GET.get('attri13', "")
    if attri13_id:
        all_techch = all_techch.filter(ProjectOrganization=attri13_id)

    attri14_id = request.GET.get('attri14', "")
    if attri14_id:
        all_techch = all_techch.filter(FlexibleLength=attri14_id)

    attri15_id = request.GET.get('attri15', "")
    if attri15_id:
        all_techch = all_techch.filter(UserParticipation=attri15_id)

    attri16_id = request.GET.get('attri16', "")
    if attri16_id:
        all_techch = all_techch.filter(InformationOrganization=attri16_id)

    attri17_id = request.GET.get('attri17', "")
    if attri17_id:
        all_techch = all_techch.filter(FeedbackOffline=attri17_id)

    attri18_id = request.GET.get('attri18', "")
    if attri18_id:
        all_techch = all_techch.filter(LongDuration=attri18_id)

    attri19_id = request.GET.get('attri19', "")
    if attri19_id:
        all_techch = all_techch.filter(UserResearch=attri19_id)

    attri20_id = request.GET.get('attri20', "")
    if attri20_id:
        all_techch = all_techch.filter(RelationshipDependency=attri20_id)

    attri21_id = request.GET.get('attri21', "")
    if attri21_id:
        all_techch = all_techch.filter(UserSimulation=attri21_id)

    attri22_id = request.GET.get('attri22', "")
    if attri22_id:
        all_techch = all_techch.filter(ExpertParticipation=attri22_id)

    attri23_id = request.GET.get('attri23', "")
    if attri23_id:
        all_techch = all_techch.filter(UXEvaluation=attri23_id)

    attri24_id = request.GET.get('attri24', "")
    if attri24_id:
        all_techch = all_techch.filter(FeedbackCollection=attri24_id)

    return render(request, 'HTML/CH/Tag-Cloud/Tag Cloud3.html',
                  {"all_techch": all_techch, "task": task, "attribut1": attribut1, })


# 添加选中技术，并跳转到post-question 3页面
def C_AddTech3(request):
    selected1 = request.POST.get('selectedone',"")
    selected2 = request.POST.get('selectedtwo',"")
    selected3 = request.POST.get('selectedthree',"")
    user_id = request.user.id
    mode = request.user.id % 4
    taskdes_all = TaskDescriptionCH.objects.all()
    taskdes = taskdes_all.filter(id=3)
    SelectedTechniqueOne.objects.create(mode_id=mode,chose_Tech1=selected1,chose_Tech2=selected2, chose_Tech3=selected3,Test_User_id=user_id )
    return render(request, 'HTML/CH/post-test Q3.html',{
        "taskdes":taskdes,
    })






#跳转到英文介绍页面
def Enlink(request):
    return  render(request,'HTML/EN/indexEN.html',{})


#跳转到英文Instruction页面
def Eninstro(request):
    return render(request,'HTML/EN/Instruction.html')


# 跳转到注册页面
def LogEn(request):
    return  render(request,'HTML/EN/login.html',{})


#  注册和登录操作，并跳转到pre-test.html
class LoginEnView(View):
    def post(self,request):
        user_name = request.POST.get("username","")
        user_password = 0
        if UserProfile.objects.filter(username=user_name):
            return render(request, 'HTML/EN/login.html',{
                "msg":"The information has already been registered. Please use other information."
            })
        userinfor = UserProfile()
        userinfor.username = user_name
        userinfor.password = user_password
        userinfor.start_time = datetime.now()
        userinfor.save()
        user_um = userinfor.id % 4
        userinfor.Mode_id = user_um
        user = authenticate(username=user_name,password=user_password)
        if user is not None:
            login(request,user)
            return render(request, 'HTML/EN/pre-test.html')


# 添加pre question到数据库，并跳转到pre questionA
def PreAddEn(request):
    if request.method == "POST":
        age = request.POST.get('age')
        sex = request.POST.get('sex')
        national = request.POST.get('national',"")
        livecountry = request.POST.get('othercontry', "")
        user_id = request.user.id
        mode = request.user.id % 4
        PreQuestionResult.objects.create(mode_id=mode,Q1_age=age,Q2_gender=sex,Q3_nationa=national, livecountry=livecountry,Test_User_id=user_id)
        if livecountry == "Yes":
            return render(request, 'HTML/EN/pre-testA.html', {})
        else:
            return render(request, 'HTML/EN/pre-testB.html', {})


# 添加pre questionA到数据库，并跳转到pre questionB
def PreAddEnA(request):
    if request.method == "POST":
        country = request.POST.get('countryname', "")
        longst = request.POST.get('yearslong', "")
        F1 = request.POST.get('F1', )
        F2 = request.POST.get('F2', )
        F3 = request.POST.get('F3', )
        F4 = request.POST.get('F4', )
        F5 = request.POST.get('F5', )
        F6 = request.POST.get('F6', )
        user_id = request.user.id
        mode = request.user.id % 4
        PreQuestionResult.objects.filter(Test_User_id=user_id).update(CountryName=country, CountryYears=longst, FC_1=F1,
                                                                      FC_2=F2, FC_3=F3, FC_4=F4, FC_5=F5, FC_6=F6, )
        return render(request, 'HTML/EN/pre-testB.html', { })


# 添加pre questionB到数据库，并跳转到pre question1
def PreAddEnB(request):
    if request.method == "POST":
        edu = request.POST.get('edu')
        eduother = request.POST.get('eduother')
        role = request.POST.getlist('role')
        roleother = request.POST.get('roleother', "")
        years = request.POST.get('years', "0")
        pronu = request.POST.get('pronu')
        cours = request.POST.get('cours')
        tech = request.POST.get('tech')
        samtech = request.POST.getlist('samtech')
        user_id = request.user.id
        mode = request.user.id % 4
        PreQuestionResult.objects.filter(Test_User_id=user_id).update(Q4_educationlevel=edu,Q41_educationlevel=eduother,
                                         Q6_role=role,Q61_role= roleother,Q7_fulltime=years,Q8_ProjectCount=pronu,Q9_DesigCourse=cours, Q10_UsedTechnique=tech,
                                         Q11_FamiliarTechnique=samtech,)
        return render(request, 'HTML/EN/pre-test1.html', { })


# 添加pre question1到数据库，并跳转到pre question2
def PreAddEn1(request):
    if request.method == "POST":
        que1 = request.POST.get('que11')
        que2 = request.POST.get('que12')
        que3 = request.POST.get('que13')
        que4 = request.POST.get('que14')
        que5 = request.POST.get('que15')
        que6 = request.POST.get('que16')
        que7 = request.POST.get('que17')
        user_id = request.user.id
        mode = request.user.id % 4
        PreQuestionResult.objects.filter(Test_User_id=user_id).update( Q12_knewpretty=que1, Q13_experts=que2, Q14_knewless=que3, Q15_donotknow=que4,
                                         Q16_donotfeel=que5, Q17_lotofexperiences=que6, Q18_familiar=que7,)

        return render(request,'HTML/EN/pre-test2.html',{})


# 添加pre question2到数据库，并跳转到introduction.html
def PreAddEn2(request):
    if request.method == "POST":
        que8 = request.POST.get('que18')
        que9 = request.POST.get('que19')
        que10 = request.POST.get('que20')
        que11 = request.POST.get('que21')
        que12 = request.POST.get('que22')
        que13 = request.POST.get('que23')
        que14 = request.POST.get('que24')
        que15 = request.POST.get('que25')
        que16 = request.POST.get('que26')
        que17 = request.POST.get('que27')
        que18 = request.POST.get('que28')
        que19 = request.POST.get('que29')
        que20 = request.POST.get('que30')
        que21 = request.POST.get('que31')
        user_id = request.user.id
        mode = request.user.id % 4
        PreQuestionResult.objects.filter(Test_User_id=user_id).update(
                                                                      Q19_focusobjects=que8,Q20_basedcategories=que9,Q21_easylearncategories=que10,
                                                                    Q22_organizefunctionally=que11, Q23_useformallogic=que12,Q24_adherelogicalrules=que13,
                                                                    Q25_individualbehavior=que14,Q26_focussurobj=que15,Q27_focussurfeld=que16,Q28_difflearncate=que17,
                                                                    Q29_organthematically=que18,Q30_diareasoning=que19,Q31_preflogic=que20,Q32_peopbehav=que21)
        if mode == 0:
            return  render(request,'HTML/EN/Top-down/introduction.html',{})
        elif mode == 1:
            return  render(request,'HTML/EN/Bottom-up/introduction.html',{})
        elif mode == 2:
            return  render(request,'HTML/EN/Tag-Cloud/introduction.html',{})
        else:
            return render(request,'HTML/EN/Blank/introduction.html')


# 跳转到Top-down的intro-test页面
def ENIntrotop(request):
    return render(request, 'HTML/EN/Top-down/intro-test.html', {})

# 判断回答是否正确
def ENChecktop(request):
    if request.method == "POST":
        test1 = request.POST.get('test1')
        test2 = request.POST.get('test2')
        test3 = request.POST.get('test3')
        if test1 == "1" and test2 == "2" and test3 == "1" :
            TaskDes = TaskDescriptionEN.objects.all()
            taskdes = TaskDes.filter(id=1)
            return render(request, 'HTML/EN/TaskDetail.html', {"taskdes": taskdes, })
        else:
            return render(request, 'HTML/EN/Top-down/intro-again.html', {})

# 跳转到Bottom的intro-test页面
def ENIntroup(request):
    return render(request, 'HTML/EN/Bottom-up/intro-test.html', {})

# 判断回答是否正确
def ENCheckup(request):
    if request.method == "POST":
        test1 = request.POST.get('test1')
        test2 = request.POST.get('test2')
        test3 = request.POST.get('test3')
        if test1 == "1" and test2 == "2" and test3 == "1" :
            TaskDes = TaskDescriptionEN.objects.all()
            taskdes = TaskDes.filter(id=1)
            return render(request, 'HTML/EN/TaskDetail.html', {"taskdes": taskdes, })
        else:
            return render(request, 'HTML/EN/Bottom-up/intro-again.html', {})

# 跳转到Tag-Cloud的intro-test页面
def ENIntrotag(request):
    return render(request, 'HTML/EN/Tag-Cloud/intro-test.html', {})

# 判断回答是否正确
def ENChecktag(request):
    if request.method == "POST":
        test1 = request.POST.get('test1')
        test2 = request.POST.get('test2')
        test3 = request.POST.get('test3')
        if test1 == "1" and test2 == "2" and test3 == "1" :
            TaskDes = TaskDescriptionEN.objects.all()
            taskdes = TaskDes.filter(id=1)
            return render(request, 'HTML/EN/TaskDetail.html', {"taskdes": taskdes, })
        else:
            return render(request, 'HTML/EN/Tag-Cloud/intro-again.html', {})

# 跳转到Blank的intro-test页面
def ENIntroblank(request):
    return render(request, 'HTML/EN/Blank/intro-test.html', {})

# 判断回答是否正确
def ENCheckblank(request):
    if request.method == "POST":
        test1 = request.POST.get('test1')
        test2 = request.POST.get('test2')    
        if test1 == "1" and test2 == "2":
            TaskDes = TaskDescriptionEN.objects.all()
            taskdes = TaskDes.filter(id=1)
            return render(request, 'HTML/EN/TaskDetail.html', {"taskdes": taskdes, })
        else:
            return render(request, 'HTML/EN/Blank/intro-again.html', {})



# 判断去哪个页面
def SwitchEN(request):
    user_id = request.user.id
    mode_id = user_id % 4
    # 跳转到Top-down页面
    if mode_id == 0:
        task_all= TaskDescriptionEN.objects.all()
        taskdes = task_all.filter(id=1)
        all_techch = TechinforEN.objects.all().order_by('?')
        attribut1 = TDDesignEN.objects.all()
        attribut2 = TDDependencyEN.objects.all()
        attribut3 = TDDurationEN.objects.all()
        attribut4 = TDParticipationEN.objects.all()
        attribut5 = TDEvaluationEN.objects.all()
        user_id = request.user.id
        design_id = request.GET.get('design', "")
        if design_id:
            all_techch = all_techch.filter(TDDesign_id=int(design_id))

        dependency_id = request.GET.get('dependency', "")
        if dependency_id:
            all_techch = all_techch.filter(TDDependency_id=int(dependency_id))

        duration_id = request.GET.get('duration', "")
        if duration_id:
            all_techch = all_techch.filter(TDDuration_id=int(duration_id))

        participant_id = request.GET.get('participant', "")
        if participant_id:
            all_techch = all_techch.filter(TDParticipation_id=int(participant_id))

        evaluation_id = request.GET.get('evaluation', "")
        if evaluation_id:
            all_techch = all_techch.filter(TDEvaluation_id=int(evaluation_id))
        return render(request, 'HTML/EN/Top-down/Top-down1.html',
                      {"all_techch": all_techch, "attribut1": attribut1, "attribut2": attribut2, "attribut3": attribut3,
                       "attribut4": attribut4, "attribut5": attribut5, "design_id": design_id,
                       "dependency_id": dependency_id, "duration_id": duration_id, "participant_id": participant_id,
                        "evaluation_id": evaluation_id,"taskdes":taskdes,
                       })
    # 跳转到Bottom-up页面
    elif mode_id == 1:
        task_all = TaskDescriptionEN.objects.all()
        taskdes = task_all.filter(id=1)
        all_techch = TechinforEN.objects.all().order_by('?')
        attribut1 = BUDesignEN.objects.all()
        attribut2 = BUCollectionEN.objects.all()
        attribut3 = BUDurationEN.objects.all()
        attribut4 = BUParticipantEN.objects.all()
        de_id = request.GET.get('de', "")
        if de_id:
            all_techch = all_techch.filter(BUDesign_id=int(de_id))

        col_id = request.GET.get('col', "")
        if col_id:
            all_techch = all_techch.filter(BUCollection_id=int(col_id))

        du_id = request.GET.get('du', "")
        if du_id:
            all_techch = all_techch.filter(BUCollection_id=int(du_id))

        pa_id = request.GET.get('pa', "")
        if pa_id:
            all_techch = all_techch.filter(BUParticipant_id=int(pa_id))

        return render(request, 'HTML/EN/Bottom-up/Bottom-up1.html',
                      {"all_techch": all_techch, "attribut1": attribut1, "attribut2": attribut2, "attribut3": attribut3,
                       "attribut4": attribut4, "de_id": de_id, "col_id": col_id, "du_id": du_id, "pa_id": pa_id, "taskdes":taskdes,
                       })
    # 跳转到Tag Cloud页面
    elif mode_id == 2:
        all_techch = TechinforEN.objects.all().order_by('?')
        attribut1 = TagCloudEN.objects.all()
        task_all=TaskDescriptionEN.objects.all()
        taskdes = task_all.filter(id=1)
        attri1_id = request.GET.get('attri1', "")
        if attri1_id:
            all_techch = all_techch.filter(UserParticipationgroup=attri1_id)

        attri2_id = request.GET.get('attri2', "")
        if attri2_id:
            all_techch = all_techch.filter(MidDuration=attri2_id)

        attri3_id = request.GET.get('attri3', "")
        if attri3_id:
            all_techch = all_techch.filter(Observation=attri3_id)

        attri4_id = request.GET.get('attri4', "")
        if attri4_id:
            all_techch = all_techch.filter(IdeaGeneration=attri4_id)

        attri5_id = request.GET.get('attri5', "")
        if attri5_id:
            all_techch = all_techch.filter(CollaborationStakeholders=attri5_id)

        attri6_id = request.GET.get('attri6', "")
        if attri6_id:
            all_techch = all_techch.filter(FeedbackOnline=attri6_id)

        attri7_id = request.GET.get('attri7', "")
        if attri7_id:
            all_techch = all_techch.filter(PrototypeEvaluation=attri7_id)

        attri8_id = request.GET.get('attri8', "")
        if attri8_id:
            all_techch = all_techch.filter(DataCollection=attri8_id)

        attri9_id = request.GET.get('attri9', "")
        if attri9_id:
            all_techch = all_techch.filter(Prototyping=attri9_id)

        attri10_id = request.GET.get('attri10', "")
        if attri10_id:
            all_techch = all_techch.filter(ShortDuration=attri10_id)

        attri11_id = request.GET.get('attri11', "")
        if attri11_id:
            all_techch = all_techch.filter(Evaluation=attri11_id)

        attri12_id = request.GET.get('attri12', "")
        if attri12_id:
            all_techch = all_techch.filter(ProductEvaluation=attri12_id)

        attri13_id = request.GET.get('attri13', "")
        if attri13_id:
            all_techch = all_techch.filter(ProjectOrganization=attri13_id)

        attri14_id = request.GET.get('attri14', "")
        if attri14_id:
            all_techch = all_techch.filter(FlexibleLength=attri14_id)

        attri15_id = request.GET.get('attri15', "")
        if attri15_id:
            all_techch = all_techch.filter(UserParticipation=attri15_id)

        attri16_id = request.GET.get('attri16', "")
        if attri16_id:
            all_techch = all_techch.filter(InformationOrganization=attri16_id)

        attri17_id = request.GET.get('attri17', "")
        if attri17_id:
            all_techch = all_techch.filter(FeedbackOffline=attri17_id)

        attri18_id = request.GET.get('attri18', "")
        if attri18_id:
            all_techch = all_techch.filter(LongDuration=attri18_id)

        attri19_id = request.GET.get('attri19', "")
        if attri19_id:
            all_techch = all_techch.filter(UserResearch=attri19_id)

        attri20_id = request.GET.get('attri20', "")
        if attri20_id:
            all_techch = all_techch.filter(RelationshipDependency=attri20_id)

        attri21_id = request.GET.get('attri21', "")
        if attri21_id:
            all_techch = all_techch.filter(UserSimulation=attri21_id)

        attri22_id = request.GET.get('attri22', "")
        if attri22_id:
            all_techch = all_techch.filter(ExpertParticipation=attri22_id)

        attri23_id = request.GET.get('attri23', "")
        if attri23_id:
            all_techch = all_techch.filter(UXEvaluation=attri23_id)

        attri24_id = request.GET.get('attri24', "")
        if attri24_id:
            all_techch = all_techch.filter(FeedbackCollection=attri24_id)

        return render(request, 'HTML/EN/Tag-Cloud/Tag Cloud1.html',
                      {"all_techch": all_techch, "attribut1": attribut1, "attri1_id": attri1_id,
                       "attri2_id": attri2_id, "attri3_id": attri3_id, "attri4_id": attri4_id,
                       "attri5_id": attri5_id, "attri6_id": attri6_id, "attri7_id": attri7_id,
                       "attri8_id": attri8_id, "attri9_id": attri9_id, "attri10_id": attri10_id,
                       "attri11_id": attri11_id, "attri12_id": attri12_id, "attri13_id": attri13_id,
                       "attri14_id": attri14_id, "attri15_id": attri15_id, "attri16_id": attri16_id,
                       "attri17_id": attri17_id, "attri18_id": attri18_id, "attri19_id": attri19_id,
                       "attri20_id": attri20_id, "attri21_id": attri21_id, "attri22_id": attri22_id,
                       "attri23_id": attri23_id, "attri24_id": attri24_id,"taskdes":taskdes,
                       })
    # 跳转到blank页面
    else:
        all_tech = TechinforEN.objects.all()
        task_all=TaskDescriptionEN.objects.all()
        taskdes = task_all.filter(id=1)
        return render(request, 'HTML/EN/Blank/blank1.html', {
            "all_tech": all_tech,
            "taskdes":taskdes,
        })



# 如果选择了Blank
# 添加选择的tech，并跳转到Post-question 1页面
def B_AddTech1EN(request):
    selected1 = request.POST.get('selectedone',"")
    selected2 = request.POST.get('selectedtwo',"")
    selected3 = request.POST.get('selectedthree',"")
    user_id = request.user.id
    mode_id = request.user.id % 4
    SelectedTechniqueOne.objects.create(chose_Tech1=selected1,chose_Tech2=selected2, chose_Tech3=selected3,Test_User_id=user_id,mode_id= mode_id )
    return render(request, 'HTML/EN/post-test Q3.html',{ })


# 添加Post-question1A到数据库，并跳转到Task-Detail 2页面
def B_AddPost1AEN(request):
    if request.method == "POST":
        post1 = request.POST.get('post1')
        post2 = request.POST.get('post2')
        post3 = request.POST.get('post3')
        post4 = request.POST.get('post4')
        post5 = request.POST.get('post5')
        post6 = request.POST.get('post6')
        user_id = request.user.id
        mode = request.user.id % 4
        PostQuestionResultOne.objects.create(mode_id=mode,Test_User_id=user_id,Q1_proficiency=post1,Q2_globalapproach=post2,Q3_localizedapproach=post3,Q4_objects=post4,Q5_rulesbased=post5,Q6_learncategory=post6,)
        return render(request, 'HTML/EN/Blank/post-test 1B.html',{

        })


# 添加Post-question1B到数据库，并跳转到Task-Detail 2页面
def B_AddPost1BEN(request):
        if request.method == "POST":
            post7 = request.POST.get('post7')
            post8 = request.POST.get('post8')
            post9 = request.POST.get('post9')
            post10 = request.POST.get('post10')
            post11 = request.POST.get('post11')
            post12 = request.POST.get('post12')
            post13 = request.POST.get('post13')
            post14 = request.POST.get('post14')
            post15 = request.POST.get('post15')
            post16 = request.POST.get('post16')
            user_id = request.user.id
            mode = request.user.id % 4
            PostQuestionResultOne.objects.filter(Test_User_id=user_id).update(Q7_organize=post7,
                                                 Q8_formallogic=post8, Q9_logicalrules=post9, Q10_individual=post10,
                                                 Q11_surrounding=post11, Q12_littelrule=post12,
                                                 Q13_difficultrule=post13, Q14_thematically=post14,
                                                 Q15_dialectical=post15, Q16_contradiction=post16, )
            TaskDes = TaskDescriptionEN.objects.all()
            taskdes = TaskDes.filter(id=2)
            return render(request, 'HTML/EN/Blank/TaskDetailtwo.html', {"taskdes": taskdes, })


# 跳转到blank2，显示tech信息等内容
def EN_blank2(request):
    all_tech = TechinforEN.objects.all().order_by('?')
    task_all = TaskDescriptionEN.objects.all()
    taskdes = task_all.filter(id=2)
    return render(request, 'HTML/EN/Blank/blank2.html', {
        "all_tech": all_tech,
        "taskdes":taskdes,
    })


# 添加选择技术到数据库，并跳转到post-question2A页面
def B_AddTech2EN(request):
    selected1 = request.POST.get('selectedone',"")
    selected2 = request.POST.get('selectedtwo',"")
    selected3 = request.POST.get('selectedthree',"")
    user_id = request.user.id
    mode = request.user.id % 4
    taskdes_all = TaskDescriptionEN.objects.all()
    taskdes = taskdes_all.filter(id=2)
    SelectedTechniqueTwo.objects.create(mode_id=mode,chose_Tech1=selected1,chose_Tech2=selected2, chose_Tech3=selected3,Test_User_id=user_id )
    return render(request, 'HTML/EN/Blank/post-test 2A.html',{
        "taskdes":taskdes,
    })


# 添加post-question2A 答案到数据库，并跳转到post-question2B页面
def B_AddPost2AEN(request):
    if request.method == "POST":
        post1 = request.POST.get('post1')
        post2 = request.POST.get('post2')
        post3 = request.POST.get('post3')
        post4 = request.POST.get('post4')
        post5 = request.POST.get('post5')
        post6 = request.POST.get('post6')
        user_id = request.user.id
        mode = request.user.id % 4
        PostQuestionResultOne.objects.create(mode_id=mode,Test_User_id=user_id,Q1_proficiency=post1,Q2_globalapproach=post2,Q3_localizedapproach=post3,
                                             Q4_objects=post4,Q5_rulesbased=post5,Q6_learncategory=post6,)
        return render(request, 'HTML/EN/Blank/post-test 2B.html',{

        })


# 添加post-question2B 答案到数据库，并跳转到TaskDetail 3页面
def B_AddPost2BEN(request):
    if request.method == "POST":
        post7 = request.POST.get('post7')
        post8 = request.POST.get('post8')
        post9 = request.POST.get('post9')
        post10 = request.POST.get('post10')
        post11 = request.POST.get('post11')
        post12 = request.POST.get('post12')
        post13 = request.POST.get('post13')
        post14 = request.POST.get('post14')
        post15 = request.POST.get('post15')
        post16 = request.POST.get('post16')
        user_id = request.user.id
        mode = request.user.id % 4
        PostQuestionResultOne.objects.filter(Test_User_id=user_id).update(Q7_organize=post7,
                                                                             Q8_formallogic=post8, Q9_logicalrules=post9, Q10_individual=post10,
                                                                             Q11_surrounding=post11, Q12_littelrule=post12,
                                                                             Q13_difficultrule=post13, Q14_thematically=post14,
                                                                             Q15_dialectical=post15, Q16_contradiction=post16, )
        TaskDes = TaskDescriptionEN.objects.all()
        taskdes = TaskDes.filter(id=3)
        return render(request, 'HTML/EN/Blank/TaskDetailthree.html', {
            "taskdes": taskdes,
        })


# 跳转到blank3页面，并显示相关信息
def EN_blank3(request):
    all_tech = TechinforEN.objects.all().order_by('?')
    task_all=TaskDescriptionEN.objects.all()
    taskdes =task_all.filter(id=3)
    return render(request, 'HTML/EN/Blank/blank3.html', {
        "all_tech": all_tech,
        "taskdes":taskdes,
    })


# 添加选中技术，并跳转到post-question 3页面
def B_AddTech3EN(request):
    selected1 = request.POST.get('selectedone',"")
    selected2 = request.POST.get('selectedtwo',"")
    selected3 = request.POST.get('selectedthree',"")
    user_id = request.user.id
    mode = request.user.id % 4
    taskdes_all = TaskDescriptionEN.objects.all()
    taskdes = taskdes_all.filter(id=3)
    SelectedTechniqueThree.objects.create(mode_id=mode,chose_Tech1=selected1,chose_Tech2=selected2, chose_Tech3=selected3,Test_User_id=user_id )
    return render(request, 'HTML/EN/post-test Q3.html',{
        "taskdes":taskdes,
    })


# 添加post-question3 到数据库，并转到end页面
def AddPost3AEn(request):
    if request.method == "POST":
        post1 = request.POST.get('post1')
        post2 = request.POST.get('post2')
        post3 = request.POST.get('post3')
        post4 = request.POST.get('post4')
        post5 = request.POST.get('post5')
        post6 = request.POST.get('post6')
        user_id = request.user.id
        mode = request.user.id % 4
        PostQuestionResultThree.objects.create(mode_id=mode,Test_User_id=user_id, Q1_proficiency=post1, Q2_globalapproach=post2,
                                             Q3_localizedapproach=post3, Q4_objects=post4, Q5_rulesbased=post5,
                                             Q6_learncategory=post6, )
        return render(request,'HTML/EN/post-test Q3A.html',{})


# 添加post-question3A 到数据库，并转到post-test 3B页面
def AddPost3BEn(request):
    if request.method == "POST":
        post7 = request.POST.get('post7')
        post8 = request.POST.get('post8')
        post9 = request.POST.get('post9')
        post10 = request.POST.get('post10')
        post11 = request.POST.get('post11')
        post12 = request.POST.get('post12')
        post13 = request.POST.get('post13')
        post14 = request.POST.get('post14')
        post15 = request.POST.get('post15')
        post16 = request.POST.get('post16')

        user_id = request.user.id
        mode = request.user.id % 4
        PostQuestionResultThree.objects.filter(Test_User_id=user_id).update(
                                               Q7_organize=post7, Q8_formallogic=post8, Q9_logicalrules=post9,
                                               Q10_individual=post10, Q11_surrounding=post11, Q12_littelrule=post12,
                                               Q13_difficultrule=post13, Q14_thematically=post14,
                                               Q15_dialectical=post15, Q16_contradiction=post16,
                                               )
        UserProfile.objects.filter(id=user_id).update(endtime=datetime.now(), mode_id=mode, )
        return render(request, 'HTML/EN/post-test Q3B.html', {})


# 添加post-question3B 到数据库，并转到end页面
def AddPost3CEn(request):
    if request.method == "POST":
        post17 = request.POST.get('post17')
        post18 = request.POST.get('post18')
        post19 = request.POST.get('post19')
        post20 = request.POST.get('post20')
        post21 = request.POST.get('post21')
        post22 = request.POST.get('post22')
        user_id = request.user.id
        mode = request.user.id % 4
        PostQuestionResultThree.objects.filter(Test_User_id=user_id).update(Q17_pressures=post17,
                                               Q18_thematically=post18, Q19_littelrule=post19,
                                               Q20_difficultrule=post20, Q21_thematically=post21,
                                               Q22_dialectical=post22, )

        UserProfile.objects.filter(id=user_id).update(endtime=datetime.now(), mode_id=mode, )
        return render(request, 'HTML/EN/end.html', {})



# 如果选择了Top-down
# 添加选择的tech，并跳转到Post-question 1页面
def T_AddTech1EN(request):
    selected1 = request.POST.get('selectedone',"")
    selected2 = request.POST.get('selectedtwo',"")
    selected3 = request.POST.get('selectedthree',"")
    user_id = request.user.id
    mode = request.user.id % 4
    SelectedTechniqueOne.objects.create(chose_Tech1=selected1,chose_Tech2=selected2, chose_Tech3=selected3,Test_User_id=user_id ,mode_id = mode)
    return render(request, 'HTML/EN/post-test Q3.html',{
    })


# 添加Post-question1A到数据库，并跳转到Post-question1B页面
def T_AddPost1AEN(request):
    if request.method == "POST":
        post1 = request.POST.get('post1')
        post2 = request.POST.get('post2')
        post3 = request.POST.get('post3')
        post4 = request.POST.get('post4')
        post5 = request.POST.get('post5')
        post6 = request.POST.get('post6')
        user_id = request.user.id
        mode = request.user.id % 4
        PostQuestionResultOne.objects.create(mode_id=mode,Test_User_id=user_id,Q1_proficiency=post1,Q2_globalapproach=post2,Q3_localizedapproach=post3,
                                             Q4_objects=post4,Q5_rulesbased=post5,Q6_learncategory=post6,
                                            )

        return render(request, 'HTML/EN/Top-down/post-test 1B.html',{

        })


# 添加Post-question1B到数据库，并跳转到Task-Detail 2页面
def T_AddPost1BEN(request):
        if request.method == "POST":
            post7 = request.POST.get('post7')
            post8 = request.POST.get('post8')
            post9 = request.POST.get('post9')
            post10 = request.POST.get('post10')
            post11 = request.POST.get('post11')
            post12 = request.POST.get('post12')
            post13 = request.POST.get('post13')
            post14 = request.POST.get('post14')
            post15 = request.POST.get('post15')
            post16 = request.POST.get('post16')
            user_id = request.user.id
            mode = request.user.id % 4
            PostQuestionResultOne.objects.filter(Test_User_id=user_id).update(Q7_organize=post7,
                                                 Q8_formallogic=post8, Q9_logicalrules=post9, Q10_individual=post10,
                                                 Q11_surrounding=post11, Q12_littelrule=post12,
                                                 Q13_difficultrule=post13, Q14_thematically=post14,
                                                 Q15_dialectical=post15, Q16_contradiction=post16, )
            TaskDes = TaskDescriptionEN.objects.all()
            taskdes = TaskDes.filter(id=2)
            return render(request, 'HTML/EN/Top-down/TaskDetailtwo.html', {"taskdes": taskdes, })


# 跳转到Top-down2，显示tech信息等内容
def EN_Top2(request):
    task_all = TaskDescriptionEN.objects.all()
    taskdes = task_all.filter(id=2)
    all_techch = TechinforEN.objects.all().order_by('?')
    attribut1 = TDDesignEN.objects.all()
    attribut2 = TDDependencyEN.objects.all()
    attribut3 = TDDurationEN.objects.all()
    attribut4 = TDParticipationEN.objects.all()
    attribut5 = TDEvaluationEN.objects.all()
    user_id = request.user.id
    design_id = request.GET.get('design', "")
    if design_id:
        all_techch = all_techch.filter(TDDesign_id=int(design_id))

    dependency_id = request.GET.get('dependency', "")
    if dependency_id:
        all_techch = all_techch.filter(TDDependency_id=int(dependency_id))

    duration_id = request.GET.get('duration', "")
    if duration_id:
        all_techch = all_techch.filter(TDDuration_id=int(duration_id))

    participant_id = request.GET.get('participant', "")
    if participant_id:
        all_techch = all_techch.filter(TDParticipation_id=int(participant_id))

    evaluation_id = request.GET.get('evaluation', "")
    if evaluation_id:
        all_techch = all_techch.filter(TDEvaluation_id=int(evaluation_id))
    return render(request, 'HTML/EN/Top-down/Top-down2.html',
                  {"all_techch": all_techch, "attribut1": attribut1, "attribut2": attribut2, "attribut3": attribut3,
                   "attribut4": attribut4, "attribut5": attribut5, "design_id": design_id,
                   "dependency_id": dependency_id, "duration_id": duration_id, "participant_id": participant_id,
                   "evaluation_id": evaluation_id, "taskdes": taskdes, })


# 添加选择技术到数据库，并跳转到post-question2页面
def T_AddTech2EN(request):
    selected1 = request.POST.get('selectedone',"")
    selected2 = request.POST.get('selectedtwo',"")
    selected3 = request.POST.get('selectedthree',"")
    user_id = request.user.id
    mode = request.user.id % 4
    taskdes_all = TaskDescriptionEN.objects.all()
    taskdes = taskdes_all.filter(id=2)
    SelectedTechniqueTwo.objects.create(mode_id=mode,chose_Tech1=selected1,chose_Tech2=selected2, chose_Tech3=selected3,Test_User_id=user_id )
    return render(request, 'HTML/EN/Top-down/post-test 2A.html', {
        "taskdes":taskdes,
    })


# 添加post-question2A 答案到数据库，并跳转到post-question2B页面
def T_AddPost2AEN(request):
    if request.method == "POST":
        post1 = request.POST.get('post1')
        post2 = request.POST.get('post2')
        post3 = request.POST.get('post3')
        post4 = request.POST.get('post4')
        post5 = request.POST.get('post5')
        post6 = request.POST.get('post6')
        user_id = request.user.id
        mode = request.user.id % 4
        PostQuestionResultTwo.objects.create(mode_id=mode,Test_User_id=user_id,Q1_proficiency=post1,Q2_globalapproach=post2,Q3_localizedapproach=post3,
                                             Q4_objects=post4,Q5_rulesbased=post5,Q6_learncategory=post6,
                                             )
        TaskDes = TaskDescriptionEN.objects.all()
        taskdes = TaskDes.filter(id=3)
        return render(request, 'HTML/EN/Top-down/post-test 2B.html',{
            "taskdes":taskdes,
        })


# 添加post-question2B 答案到数据库，并跳转到TaskDetail 3页面
def T_AddPost2BEN(request):
    if request.method == "POST":
        post7 = request.POST.get('post7')
        post8 = request.POST.get('post8')
        post9 = request.POST.get('post9')
        post10 = request.POST.get('post10')
        post11 = request.POST.get('post11')
        post12 = request.POST.get('post12')
        post13 = request.POST.get('post13')
        post14 = request.POST.get('post14')
        post15 = request.POST.get('post15')
        post16 = request.POST.get('post16')
        user_id = request.user.id
        mode = request.user.id % 4
        PostQuestionResultTwo.objects.filter(Test_User_id=user_id).update(Q7_organize=post7,
                                             Q8_formallogic=post8, Q9_logicalrules=post9, Q10_individual=post10,
                                             Q11_surrounding=post11, Q12_littelrule=post12,
                                             Q13_difficultrule=post13, Q14_thematically=post14,
                                             Q15_dialectical=post15, Q16_contradiction=post16, )
        TaskDes = TaskDescriptionEN.objects.all()
        taskdes = TaskDes.filter(id=3)
        return render(request, 'HTML/EN/Top-down/TaskDetailthree.html', {"taskdes": taskdes, })

# 跳转到Top-down3页面，并显示相关信息
def EN_Top3(request):
    task_all = TaskDescriptionEN.objects.all()
    taskdes = task_all.filter(id=3)
    all_techch = TechinforEN.objects.all().order_by('?')
    attribut1 = TDDesignEN.objects.all()
    attribut2 = TDDependencyEN.objects.all()
    attribut3 = TDDurationEN.objects.all()
    attribut4 = TDParticipationEN.objects.all()
    attribut5 = TDEvaluationEN.objects.all()
    user_id = request.user.id
    design_id = request.GET.get('design', "")
    if design_id:
        all_techch = all_techch.filter(TDDesign_id=int(design_id))

    dependency_id = request.GET.get('dependency', "")
    if dependency_id:
        all_techch = all_techch.filter(TDDependency_id=int(dependency_id))

    duration_id = request.GET.get('duration', "")
    if duration_id:
        all_techch = all_techch.filter(TDDuration_id=int(duration_id))

    participant_id = request.GET.get('participant', "")
    if participant_id:
        all_techch = all_techch.filter(TDParticipation_id=int(participant_id))

    evaluation_id = request.GET.get('evaluation', "")
    if evaluation_id:
        all_techch = all_techch.filter(TDEvaluation_id=int(evaluation_id))
    return render(request, 'HTML/EN/Top-down/Top-down3.html',
                  {"all_techch": all_techch, "attribut1": attribut1, "attribut2": attribut2, "attribut3": attribut3,
                   "attribut4": attribut4, "attribut5": attribut5, "design_id": design_id,
                   "dependency_id": dependency_id, "duration_id": duration_id, "participant_id": participant_id,
                   "evaluation_id": evaluation_id, "taskdes": taskdes, })


# 添加选中技术，并跳转到post-question 3页面
def T_AddTech3EN(request):
    selected1 = request.POST.get('selectedone',"")
    selected2 = request.POST.get('selectedtwo',"")
    selected3 = request.POST.get('selectedthree',"")
    user_id = request.user.id
    mode = request.user.id % 4
    taskdes_all = TaskDescriptionEN.objects.all()
    taskdes = taskdes_all.filter(id=3)
    SelectedTechniqueThree.objects.create(mode_id=mode,chose_Tech1=selected1,chose_Tech2=selected2, chose_Tech3=selected3,Test_User_id=user_id )
    return render(request, 'HTML/EN/post-test Q3.html',{
        "taskdes":taskdes,
    })



# 如果选择了Bottom-up
# 添加选择的tech，并跳转到Post-question 1页面
def U_AddTech1EN(request):
    selected1 = request.POST.get('selectedone',"")
    selected2 = request.POST.get('selectedtwo',"")
    selected3 = request.POST.get('selectedthree',"")
    user_id = request.user.id
    mode = request.user.id % 4
    SelectedTechniqueOne.objects.create(mode_id=mode,chose_Tech1=selected1,chose_Tech2=selected2, chose_Tech3=selected3,Test_User_id=user_id )
    return render(request, 'HTML/EN/post-test Q3.html',{
    })


# 添加Post-question1A到数据库，并跳转到Post-question1B页面
def U_AddPost1AEN(request):
    if request.method == "POST":
        post1 = request.POST.get('post1')
        post2 = request.POST.get('post2')
        post3 = request.POST.get('post3')
        post4 = request.POST.get('post4')
        post5 = request.POST.get('post5')
        post6 = request.POST.get('post6')
        user_id = request.user.id
        mode = request.user.id % 4
        PostQuestionResultOne.objects.create(mode_id=mode, Test_User_id=user_id, Q1_proficiency=post1,
                                             Q2_globalapproach=post2, Q3_localizedapproach=post3, Q4_objects=post4,
                                             Q5_rulesbased=post5, Q6_learncategory=post6, )
        return render(request, 'HTML/EN/Bottom-up/post-test 1B.html',{

        })



# 添加Post-question1B到数据库，并跳转到Task-Detail 2页面
def U_AddPost1BEN(request):
        if request.method == "POST":
            post7 = request.POST.get('post7')
            post8 = request.POST.get('post8')
            post9 = request.POST.get('post9')
            post10 = request.POST.get('post10')
            post11 = request.POST.get('post11')
            post12 = request.POST.get('post12')
            post13 = request.POST.get('post13')
            post14 = request.POST.get('post14')
            post15 = request.POST.get('post15')
            post16 = request.POST.get('post16')
            user_id = request.user.id
            mode = request.user.id % 4
            PostQuestionResultOne.objects.filter(Test_User_id=user_id).update(Q7_organize=post7,
                                                 Q8_formallogic=post8, Q9_logicalrules=post9, Q10_individual=post10,
                                                 Q11_surrounding=post11, Q12_littelrule=post12,
                                                 Q13_difficultrule=post13, Q14_thematically=post14,
                                                 Q15_dialectical=post15, Q16_contradiction=post16, )
            TaskDes = TaskDescriptionEN.objects.all()
            taskdes = TaskDes.filter(id=2)
            return render(request, 'HTML/EN/Bottom-up/TaskDetailtwo.html', {"taskdes": taskdes, })



# 跳转到Bottom-up 2，显示tech信息等内容
def EN_Up2(request):
    all_techch = TechinforEN.objects.all().order_by('?')
    task_all = TaskDescriptionEN.objects.all()
    taskdes = task_all.filter(id=2)
    attribut1 = BUDesignEN.objects.all()
    attribut2 = BUCollectionEN.objects.all()
    attribut3 = BUDurationEN.objects.all()
    attribut4 = BUParticipantEN.objects.all()
    de_id = request.GET.get('de', "")
    if de_id:
        all_techch = all_techch.filter(BUDesign_id=int(de_id))

    col_id = request.GET.get('col', "")
    if col_id:
        all_techch = all_techch.filter(BUCollection_id=int(col_id))

    du_id = request.GET.get('du', "")
    if du_id:
        all_techch = all_techch.filter(BUCollection_id=int(du_id))

    pa_id = request.GET.get('pa', "")
    if pa_id:
        all_techch = all_techch.filter(BUParticipant_id=int(pa_id))

    return render(request, 'HTML/EN/Bottom-up/Bottom-up2.html',
                  {"all_techch": all_techch, "attribut1": attribut1, "attribut2": attribut2, "attribut3": attribut3,
                   "attribut4": attribut4, "de_id": de_id, "col_id": col_id, "du_id": du_id, "pa_id": pa_id,
                   "taskdes": taskdes, })


# 添加选择技术到数据库，并跳转到post-question2A页面
def U_AddTech2EN(request):
    selected1 = request.POST.get('selectedone',"")
    selected2 = request.POST.get('selectedtwo',"")
    selected3 = request.POST.get('selectedthree',"")
    user_id = request.user.id
    mode = request.user.id % 4
    taskdes_all = TaskDescriptionEN.objects.all()
    taskdes = taskdes_all.filter(id=2)
    SelectedTechniqueOne.objects.create(mode_id=mode,chose_Tech1=selected1,chose_Tech2=selected2, chose_Tech3=selected3,Test_User_id=user_id )
    return render(request, 'HTML/EN/Bottom-up/post-test 2A.html',{
        "taskdes":taskdes,
    })


# 添加post-question2A 答案到数据库，并跳转到post-question2B页面
def U_AddPost2AEN(request):
    if request.method == "POST":
        post1 = request.POST.get('post1')
        post2 = request.POST.get('post2')
        post3 = request.POST.get('post3')
        post4 = request.POST.get('post4')
        post5 = request.POST.get('post5')
        post6 = request.POST.get('post6')
        user_id = request.user.id
        mode = request.user.id % 4
        PostQuestionResultOne.objects.create(mode_id=mode,Test_User_id=user_id,Q1_proficiency=post1,Q2_globalapproach=post2,Q3_localizedapproach=post3,
                                             Q4_objects=post4,Q5_rulesbased=post5,Q6_learncategory=post6, )
        return render(request, 'HTML/EN/Bottom-up/post-test 2B.html',{

        })


# 添加post-question2B 答案到数据库，并跳转到TaskDetail 3页面
def U_AddPost2BEN(request):
        if request.method == "POST":
            post7 = request.POST.get('post7')
            post8 = request.POST.get('post8')
            post9 = request.POST.get('post9')
            post10 = request.POST.get('post10')
            post11 = request.POST.get('post11')
            post12 = request.POST.get('post12')
            post13 = request.POST.get('post13')
            post14 = request.POST.get('post14')
            post15 = request.POST.get('post15')
            post16 = request.POST.get('post16')
            user_id = request.user.id
            mode = request.user.id % 4
            PostQuestionResultOne.objects.filter(Test_User_id=user_id).update(Q7_organize=post7,
                                                 Q8_formallogic=post8, Q9_logicalrules=post9, Q10_individual=post10,
                                                 Q11_surrounding=post11, Q12_littelrule=post12,
                                                 Q13_difficultrule=post13, Q14_thematically=post14,
                                                 Q15_dialectical=post15, Q16_contradiction=post16, )
            TaskDes = TaskDescriptionEN.objects.all()
            taskdes = TaskDes.filter(id=3)
            return render(request, 'HTML/EN/Bottom-up/TaskDetailthree.html', {"taskdes": taskdes, })


# 跳转到Bottom-up3页面，并显示相关信息
def EN_Up3(request):
    all_techch = TechinforEN.objects.all().order_by('?')
    task_all = TaskDescriptionEN.objects.all()
    taskdes = task_all.filter(id=3)
    attribut1 = BUDesignEN.objects.all()
    attribut2 = BUCollectionEN.objects.all()
    attribut3 = BUDurationEN.objects.all()
    attribut4 = BUParticipantEN.objects.all()
    de_id = request.GET.get('de', "")
    if de_id:
        all_techch = all_techch.filter(BUDesign_id=int(de_id))

    col_id = request.GET.get('col', "")
    if col_id:
        all_techch = all_techch.filter(BUCollection_id=int(col_id))

    du_id = request.GET.get('du', "")
    if du_id:
        all_techch = all_techch.filter(BUCollection_id=int(du_id))

    pa_id = request.GET.get('pa', "")
    if pa_id:
        all_techch = all_techch.filter(BUParticipant_id=int(pa_id))

    return render(request, 'HTML/EN/Bottom-up/Bottom-up3.html',
                  {"all_techch": all_techch, "attribut1": attribut1, "attribut2": attribut2, "attribut3": attribut3,
                   "attribut4": attribut4, "de_id": de_id, "col_id": col_id, "du_id": du_id, "pa_id": pa_id,
                   "taskdes": taskdes, })


# 添加选中技术，并跳转到post-question 3页面
def U_AddTech3EN(request):
    selected1 = request.POST.get('selectedone',"")
    selected2 = request.POST.get('selectedtwo',"")
    selected3 = request.POST.get('selectedthree',"")
    user_id = request.user.id
    mode = request.user.id % 4
    taskdes_all = TaskDescriptionEN.objects.all()
    taskdes = taskdes_all.filter(id=3)
    SelectedTechniqueOne.objects.create(mode_id=mode,chose_Tech1=selected1,chose_Tech2=selected2, chose_Tech3=selected3,Test_User_id=user_id )
    return render(request, 'HTML/EN/post-test Q3.html',{
        "taskdes":taskdes,
    })






# 选择了Tag Cloud
# 添加选择的tech，并跳转到Post-question 1页面
def C_AddTech1EN(request):
    selected1 = request.POST.get('selectedone',"")
    selected2 = request.POST.get('selectedtwo',"")
    selected3 = request.POST.get('selectedthree',"")
    user_id = request.user.id
    mode = request.user.id % 4
    SelectedTechniqueOne.objects.create(mode_id=mode,chose_Tech1=selected1,chose_Tech2=selected2, chose_Tech3=selected3,Test_User_id=user_id )
    return render(request, 'HTML/EN/post-test Q3.html', {
    })


# 添加Post-question1到数据库，并跳转到Task-Detail 2页面
def C_AddPost1AEN(request):
    if request.method == "POST":
        post1 = request.POST.get('post1')
        post2 = request.POST.get('post2')
        post3 = request.POST.get('post3')
        post4 = request.POST.get('post4')
        post5 = request.POST.get('post5')
        post6 = request.POST.get('post6')

        user_id = request.user.id
        mode = request.user.id % 4
        PostQuestionResultOne.objects.create(mode_id=mode,Test_User_id=user_id,Q1_proficiency=post1,Q2_globalapproach=post2,Q3_localizedapproach=post3,
                                             Q4_objects=post4,Q5_rulesbased=post5,Q6_learncategory=post6,)
        return render(request, 'HTML/EN/Tag-Cloud/post-test 1B.html',{

        })


# 添加Post-question1到数据库，并跳转到Task-Detail 2页面
def C_AddPost1BEN(request):
        if request.method == "POST":
            post7 = request.POST.get('post7')
            post8 = request.POST.get('post8')
            post9 = request.POST.get('post9')
            post10 = request.POST.get('post10')
            post11 = request.POST.get('post11')
            post12 = request.POST.get('post12')
            post13 = request.POST.get('post13')
            post14 = request.POST.get('post14')
            post15 = request.POST.get('post15')
            post16 = request.POST.get('post16')
            user_id = request.user.id
            mode = request.user.id % 4
            PostQuestionResultOne.objects.filter(Test_User_id=user_id).update(Q7_organize=post7,
                                                 Q8_formallogic=post8, Q9_logicalrules=post9, Q10_individual=post10,
                                                 Q11_surrounding=post11, Q12_littelrule=post12,
                                                 Q13_difficultrule=post13, Q14_thematically=post14,
                                                 Q15_dialectical=post15, Q16_contradiction=post16, )
            TaskDes = TaskDescriptionEN.objects.all()
            taskdes = TaskDes.filter(id=2)
            return render(request, 'HTML/EN/Tag-Cloud/TaskDetailtwo.html', {"taskdes": taskdes, })


# 跳转到Tag Cloud 2，显示tech信息等内容
def EN_C2(request):
        all_techch = TechinforEN.objects.all().order_by('?')
        attribut1 = TagCloudEN.objects.all()
        task_all=TaskDescriptionEN.objects.all()
        taskdes = task_all.filter(id=2)

        attri1_id = request.GET.get('attri1', "")
        if attri1_id:
            all_techch = all_techch.filter(UserParticipationgroup=attri1_id)

        attri2_id = request.GET.get('attri2', "")
        if attri2_id:
            all_techch = all_techch.filter(MidDuration=attri2_id)

        attri3_id = request.GET.get('attri3', "")
        if attri3_id:
            all_techch = all_techch.filter(Observation=attri3_id)

        attri4_id = request.GET.get('attri4', "")
        if attri4_id:
            all_techch = all_techch.filter(IdeaGeneration=attri4_id)

        attri5_id = request.GET.get('attri5', "")
        if attri5_id:
            all_techch = all_techch.filter(CollaborationStakeholders=attri5_id)

        attri6_id = request.GET.get('attri6', "")
        if attri6_id:
            all_techch = all_techch.filter(FeedbackOnline=attri6_id)

        attri7_id = request.GET.get('attri7', "")
        if attri7_id:
            all_techch = all_techch.filter(PrototypeEvaluation=attri7_id)

        attri8_id = request.GET.get('attri8', "")
        if attri8_id:
            all_techch = all_techch.filter(DataCollection=attri8_id)

        attri9_id = request.GET.get('attri9', "")
        if attri9_id:
            all_techch = all_techch.filter(Prototyping=attri9_id)

        attri10_id = request.GET.get('attri10', "")
        if attri10_id:
            all_techch = all_techch.filter(ShortDuration=attri10_id)

        attri11_id = request.GET.get('attri11', "")
        if attri11_id:
            all_techch = all_techch.filter(Evaluation=attri11_id)

        attri12_id = request.GET.get('attri12', "")
        if attri12_id:
            all_techch = all_techch.filter(ProductEvaluation=attri12_id)

        attri13_id = request.GET.get('attri13', "")
        if attri13_id:
            all_techch = all_techch.filter(ProjectOrganization=attri13_id)

        attri14_id = request.GET.get('attri14', "")
        if attri14_id:
            all_techch = all_techch.filter(FlexibleLength=attri14_id)

        attri15_id = request.GET.get('attri15', "")
        if attri15_id:
            all_techch = all_techch.filter(UserParticipation=attri15_id)

        attri16_id = request.GET.get('attri16', "")
        if attri16_id:
            all_techch = all_techch.filter(InformationOrganization=attri16_id)

        attri17_id = request.GET.get('attri17', "")
        if attri17_id:
            all_techch = all_techch.filter(FeedbackOffline=attri17_id)

        attri18_id = request.GET.get('attri18', "")
        if attri18_id:
            all_techch = all_techch.filter(LongDuration=attri18_id)

        attri19_id = request.GET.get('attri19', "")
        if attri19_id:
            all_techch = all_techch.filter(UserResearch=attri19_id)

        attri20_id = request.GET.get('attri20', "")
        if attri20_id:
            all_techch = all_techch.filter(RelationshipDependency=attri20_id)

        attri21_id = request.GET.get('attri21', "")
        if attri21_id:
            all_techch = all_techch.filter(UserSimulation=attri21_id)

        attri22_id = request.GET.get('attri22', "")
        if attri22_id:
            all_techch = all_techch.filter(ExpertParticipation=attri22_id)

        attri23_id = request.GET.get('attri23', "")
        if attri23_id:
            all_techch = all_techch.filter(UXEvaluation=attri23_id)

        attri24_id = request.GET.get('attri24', "")
        if attri24_id:
            all_techch = all_techch.filter(FeedbackCollection=attri24_id)

        return render(request, 'HTML/EN/Tag-Cloud/Tag Cloud2.html',
                      {"all_techch": all_techch, "attribut1": attribut1, "attri1_id": attri1_id,
                       "attri2_id": attri2_id, "attri3_id": attri3_id, "attri4_id": attri4_id,
                       "attri5_id": attri5_id, "attri6_id": attri6_id, "attri7_id": attri7_id,
                       "attri8_id": attri8_id, "attri9_id": attri9_id, "attri10_id": attri10_id,
                       "attri11_id": attri11_id, "attri12_id": attri12_id, "attri13_id": attri13_id,
                       "attri14_id": attri14_id, "attri15_id": attri15_id, "attri16_id": attri16_id,
                       "attri17_id": attri17_id, "attri18_id": attri18_id, "attri19_id": attri19_id,
                       "attri20_id": attri20_id, "attri21_id": attri21_id, "attri22_id": attri22_id,
                       "attri23_id": attri23_id, "attri24_id": attri24_id,"taskdes":taskdes,
                       })


# 添加选择技术到数据库，并跳转到post-question2页面
def C_AddTech2EN(request):
    selected1 = request.POST.get('selectedone',"")
    selected2 = request.POST.get('selectedtwo',"")
    selected3 = request.POST.get('selectedthree',"")
    user_id = request.user.id
    mode = request.user.id % 4
    taskdes_all = TaskDescriptionEN.objects.all()
    taskdes = taskdes_all.filter(id=2)
    SelectedTechniqueOne.objects.create(mode_id=mode,chose_Tech1=selected1,chose_Tech2=selected2, chose_Tech3=selected3,Test_User_id=user_id )
    return render(request, 'HTML/EN/Tag-Cloud/post-test 2A.html', {
        "taskdes":taskdes,
    })


# 添加post-question2A答案到数据库，并跳转到post-question2B页面
def C_AddPost2AEN(request):
    if request.method == "POST":
        post1 = request.POST.get('post1')
        post2 = request.POST.get('post2')
        post3 = request.POST.get('post3')
        post4 = request.POST.get('post4')
        post5 = request.POST.get('post5')
        post6 = request.POST.get('post6')
        user_id = request.user.id
        mode = request.user.id % 4
        PostQuestionResultOne.objects.create(mode_id=mode,Test_User_id=user_id,Q1_proficiency=post1,Q2_globalapproach=post2,Q3_localizedapproach=post3,Q4_objects=post4,Q5_rulesbased=post5,Q6_learncategory=post6,)
        return render(request, 'HTML/EN/Tag-Cloud/post-test 2B.html',{

        })


# 添加post-question2B答案到数据库，并跳转到TaskDetail 3页面
def C_AddPost2BEN(request):
        if request.method == "POST":
            post7 = request.POST.get('post7')
            post8 = request.POST.get('post8')
            post9 = request.POST.get('post9')
            post10 = request.POST.get('post10')
            post11 = request.POST.get('post11')
            post12 = request.POST.get('post12')
            post13 = request.POST.get('post13')
            post14 = request.POST.get('post14')
            post15 = request.POST.get('post15')
            post16 = request.POST.get('post16')
            user_id = request.user.id
            mode = request.user.id % 4
            PostQuestionResultOne.objects.filter(Test_User_id=user_id).update(Q7_organize=post7,
                                                 Q8_formallogic=post8, Q9_logicalrules=post9, Q10_individual=post10,
                                                 Q11_surrounding=post11, Q12_littelrule=post12,
                                                 Q13_difficultrule=post13, Q14_thematically=post14,
                                                 Q15_dialectical=post15, Q16_contradiction=post16, )
            TaskDes = TaskDescriptionEN.objects.all()
            taskdes = TaskDes.filter(id=3)
            return render(request, 'HTML/EN/Tag-Cloud/TaskDetailthree.html', {"taskdes": taskdes, })

# 跳转到Tag Cloud 3页面，并显示相关信息
def EN_C3(request):
    all_techch = TechinforEN.objects.all().order_by('?')
    attribut1 = TagCloudEN.objects.all()
    task_all = TaskDescriptionEN.objects.all()
    taskdes = task_all.filter(id=2)

    attri1_id = request.GET.get('attri1', "")
    if attri1_id:
        all_techch = all_techch.filter(UserParticipationgroup=attri1_id)

    attri2_id = request.GET.get('attri2', "")
    if attri2_id:
        all_techch = all_techch.filter(MidDuration=attri2_id)

    attri3_id = request.GET.get('attri3', "")
    if attri3_id:
        all_techch = all_techch.filter(Observation=attri3_id)

    attri4_id = request.GET.get('attri4', "")
    if attri4_id:
        all_techch = all_techch.filter(IdeaGeneration=attri4_id)

    attri5_id = request.GET.get('attri5', "")
    if attri5_id:
        all_techch = all_techch.filter(CollaborationStakeholders=attri5_id)

    attri6_id = request.GET.get('attri6', "")
    if attri6_id:
        all_techch = all_techch.filter(FeedbackOnline=attri6_id)

    attri7_id = request.GET.get('attri7', "")
    if attri7_id:
        all_techch = all_techch.filter(PrototypeEvaluation=attri7_id)

    attri8_id = request.GET.get('attri8', "")
    if attri8_id:
        all_techch = all_techch.filter(DataCollection=attri8_id)

    attri9_id = request.GET.get('attri9', "")
    if attri9_id:
        all_techch = all_techch.filter(Prototyping=attri9_id)

    attri10_id = request.GET.get('attri10', "")
    if attri10_id:
        all_techch = all_techch.filter(ShortDuration=attri10_id)

    attri11_id = request.GET.get('attri11', "")
    if attri11_id:
        all_techch = all_techch.filter(Evaluation=attri11_id)

    attri12_id = request.GET.get('attri12', "")
    if attri12_id:
        all_techch = all_techch.filter(ProductEvaluation=attri12_id)

    attri13_id = request.GET.get('attri13', "")
    if attri13_id:
        all_techch = all_techch.filter(ProjectOrganization=attri13_id)

    attri14_id = request.GET.get('attri14', "")
    if attri14_id:
        all_techch = all_techch.filter(FlexibleLength=attri14_id)

    attri15_id = request.GET.get('attri15', "")
    if attri15_id:
        all_techch = all_techch.filter(UserParticipation=attri15_id)

    attri16_id = request.GET.get('attri16', "")
    if attri16_id:
        all_techch = all_techch.filter(InformationOrganization=attri16_id)

    attri17_id = request.GET.get('attri17', "")
    if attri17_id:
        all_techch = all_techch.filter(FeedbackOffline=attri17_id)

    attri18_id = request.GET.get('attri18', "")
    if attri18_id:
        all_techch = all_techch.filter(LongDuration=attri18_id)

    attri19_id = request.GET.get('attri19', "")
    if attri19_id:
        all_techch = all_techch.filter(UserResearch=attri19_id)

    attri20_id = request.GET.get('attri20', "")
    if attri20_id:
        all_techch = all_techch.filter(RelationshipDependency=attri20_id)

    attri21_id = request.GET.get('attri21', "")
    if attri21_id:
        all_techch = all_techch.filter(UserSimulation=attri21_id)

    attri22_id = request.GET.get('attri22', "")
    if attri22_id:
        all_techch = all_techch.filter(ExpertParticipation=attri22_id)

    attri23_id = request.GET.get('attri23', "")
    if attri23_id:
        all_techch = all_techch.filter(UXEvaluation=attri23_id)

    attri24_id = request.GET.get('attri24', "")
    if attri24_id:
        all_techch = all_techch.filter(FeedbackCollection=attri24_id)

    return render(request, 'HTML/EN/Tag-Cloud/Tag Cloud3.html',
                  {"all_techch": all_techch, "taskdes": taskdes, "attribut1": attribut1, })


# 添加选中技术，并跳转到post-question 3页面
def C_AddTech3EN(request):
    selected1 = request.POST.get('selectedone',"")
    selected2 = request.POST.get('selectedtwo',"")
    selected3 = request.POST.get('selectedthree',"")
    user_id = request.user.id
    mode = request.user.id % 4
    taskdes_all = TaskDescriptionEN.objects.all()
    taskdes = taskdes_all.filter(id=3)
    SelectedTechniqueOne.objects.create(mode_id=mode,chose_Tech1=selected1,chose_Tech2=selected2, chose_Tech3=selected3,Test_User_id=user_id )
    return render(request, 'HTML/EN/post-test Q3.html',{
        "taskdes":taskdes,
    })











#转到德语介绍界面
def Delink(request):
    return  render(request,'HTML/DE/indexDE.html',{})


#转到德语Instruction页面
def Deinstro(request):
    return render(request,'HTML/DE/Instruction.html')


# 跳转到注册页面
def LogDe(request):
    return  render(request,'HTML/DE/login.html',{})


#  注册和登录操作，并跳转到pre-test.html
class LoginDeView(View):
    def post(self,request):
        user_name = request.POST.get("username","")
        user_password = 0
        if UserProfile.objects.filter(username=user_name):
            return render(request, 'HTML/DE/login.html',{
                "msg":"！Die Informationen wurden bereits registriert. Bitte verwenden Sie andere Informationen."
            })
        userinfor = UserProfile()
        userinfor.username = user_name
        userinfor.password = user_password
        userinfor.start_time = datetime.now()
        userinfor.save()
        user_um = userinfor.id % 4
        userinfor.Mode_id = user_um
        user = authenticate(username=user_name,password=user_password)
        if user is not None:
            login(request,user)
            return render(request,'HTML/DE/pre-test.html')


# 添加pre question到数据库，并跳转到pre-test A
def PreAddDe(request):
    if request.method == "POST":
        age = request.POST.get('age')
        sex = request.POST.get('sex')
        national = request.POST.get('national',"")
        livecountry = request.POST.get('othercontry', "")
        user_id = request.user.id
        mode = request.user.id % 4
        PreQuestionResult.objects.create(mode_id=mode,Q1_age=age,Q2_gender=sex,Q3_nationa=national,livecountry=livecountry,Test_User_id=user_id)
        if livecountry == "Ja":
            return render(request, 'HTML/DE/pre-testA.html', { })
        else:
            return render(request, 'HTML/DE/pre-testB.html', {})



# 添加pre questionA到数据库，并跳转到pre-test B
def PreAddDeA(request):
    if request.method == "POST":
        country = request.POST.get('countryname', "")
        longst = request.POST.get('yearslong', "")
        F1 = request.POST.get('F1', )
        F2 = request.POST.get('F2', )
        F3 = request.POST.get('F3', )
        F4 = request.POST.get('F4', )
        F5 = request.POST.get('F5', )
        F6 = request.POST.get('F6', )
        user_id = request.user.id
        mode = request.user.id % 4
        PreQuestionResult.objects.filter(Test_User_id=user_id).update(CountryName=country, CountryYears=longst, FC_1=F1,FC_2=F2, FC_3=F3, FC_4=F4, FC_5=F5, FC_6=F6, )
        return render(request, 'HTML/DE/pre-testB.html', {})


# 添加pre questionA到数据库，并跳转到pre-test B
def PreAddDeB(request):
    if request.method == "POST":
        edu = request.POST.get('edu')
        eduother = request.POST.get('eduother')
        role = request.POST.getlist('role')
        roleother = request.POST.get('roleother', "")
        years = request.POST.get('years', "0")
        pronu = request.POST.get('pronu')
        cours = request.POST.get('cours')
        tech = request.POST.get('tech')
        samtech = request.POST.getlist('samtech')
        user_id = request.user.id
        mode = request.user.id % 4
        PreQuestionResult.objects.filter(Test_User_id=user_id).update(mode_id=mode, Q4_educationlevel=edu,
                                                                      Q41_educationlevel=eduother, Q6_role=role,
                                                                      Q61_role=roleother, Q7_fulltime=years,
                                                                      Q8_ProjectCount=pronu, Q9_DesigCourse=cours,
                                                                      Q10_UsedTechnique=tech,
                                                                      Q11_FamiliarTechnique=samtech, )
        return render(request,'HTML/DE/pre-test1.html',{})


# 添加pre questionB到数据库，并跳转到pre-test1
def PreAddDe1(request):
    if request.method == "POST":
        que1 = request.POST.get('que11')
        que2 = request.POST.get('que12')
        que3 = request.POST.get('que13')
        que4 = request.POST.get('que14')
        que5 = request.POST.get('que15')
        que6 = request.POST.get('que16')
        que7 = request.POST.get('que17')
        user_id = request.user.id
        mode = request.user.id % 4
        PreQuestionResult.objects.filter(Test_User_id=user_id).update(Q12_knewpretty=que1,
                                         Q13_experts=que2, Q14_knewless=que3, Q15_donotknow=que4,
                                         Q16_donotfeel=que5, Q17_lotofexperiences=que6, Q18_familiar=que7,
                                        )
    return render(request,'HTML/DE/pre-test2.html',{})



# 添加pre question到数据库，并选择跳转到哪个introduction.html
def PreAddDe2(request):
    if request.method == "POST":
        que8 = request.POST.get('que18')
        que9 = request.POST.get('que19')
        que10 = request.POST.get('que20')
        que11 = request.POST.get('que21')
        que12 = request.POST.get('que22')
        que13 = request.POST.get('que23')
        que14 = request.POST.get('que24')
        que15 = request.POST.get('que25')
        que16 = request.POST.get('que26')
        que17 = request.POST.get('que27')
        que18 = request.POST.get('que28')
        que19 = request.POST.get('que29')
        que20 = request.POST.get('que30')
        que21 = request.POST.get('que31')
        user_id = request.user.id
        mode = request.user.id % 4
        PreQuestionResult.objects.filter(Test_User_id=user_id).update(Q19_focusobjects=que8,
                                         Q20_basedcategories=que9, Q21_easylearncategories=que10,
                                         Q22_organizefunctionally=que11, Q23_useformallogic=que12,
                                         Q24_adherelogicalrules=que13, Q25_individualbehavior=que14,
                                         Q26_focussurobj=que15, Q27_focussurfeld=que16,
                                         Q28_difflearncate=que17, Q29_organthematically=que18,
                                         Q30_diareasoning=que19, Q31_preflogic=que20,Q32_peopbehav=que21,)
        if mode == 0:
            return render(request, 'HTML/DE/Top-down/introduction.html', {})
        elif mode == 1:
            return render(request, 'HTML/DE/Bottom-up/introduction.html', {})
        elif mode == 2:
            return render(request, 'HTML/DE/Tag Cloud/introduction.html', {})
        else:
            return render(request, 'HTML/DE/Blank/introduction.html', {})


# 跳转到Top-down的intro-test页面
def DEIntrotop(request):
    return render(request, 'HTML/DE/Top-down/intro-test.html', {})

# 判断回答是否正确
def DEChecktop(request):
    if request.method == "POST":
        test1 = request.POST.get('test1')
        test2 = request.POST.get('test2')
        test3 = request.POST.get('test3')
        if test1 == "1" and test2 == "2" and test3 == "1" :
            TaskDes = TaskDescriptionDE.objects.all()
            taskdes = TaskDes.filter(id=1)
            return render(request, 'HTML/DE/TaskDetail.html', {"taskdes": taskdes, })
        else:
            return render(request, 'HTML/DE/Top-down/intro-again.html', {})

# 跳转到Bottom的intro-test页面
def DEIntroup(request):
    return render(request, 'HTML/DE/Bottom-up/intro-test.html', {})

# 判断回答是否正确
def DECheckup(request):
    if request.method == "POST":
        test1 = request.POST.get('test1')
        test2 = request.POST.get('test2')
        test3 = request.POST.get('test3')
        if test1 == "1" and test2 == "2" and test3 == "1" :
            TaskDes = TaskDescriptionDE.objects.all()
            taskdes = TaskDes.filter(id=1)
            return render(request, 'HTML/DE/TaskDetail.html', {"taskdes": taskdes, })
        else:
            return render(request, 'HTML/DE/Bottom-up/intro-again.html', {})

# 跳转到Tag-Cloud的intro-test页面
def DEIntrotag(request):
    return render(request, 'HTML/DE/Tag Cloud/intro-test.html', {})

# 判断回答是否正确
def DEChecktag(request):
    if request.method == "POST":
        test1 = request.POST.get('test1')
        test2 = request.POST.get('test2')
        test3 = request.POST.get('test3')
        if test1 == "1" and test2 == "2" and test3 == "1" :
            TaskDes = TaskDescriptionDE.objects.all()
            taskdes = TaskDes.filter(id=1)
            return render(request, 'HTML/DE/TaskDetail.html', {"taskdes": taskdes, })
        else:
            return render(request, 'HTML/DE/Tag Cloud/intro-again.html', {})

# 跳转到Blank的intro-test页面
def DEIntroblank(request):
    return render(request, 'HTML/DE/Blank/intro-test.html', {})

# 判断回答是否正确
def DECheckblank(request):
    if request.method == "POST":
        test1 = request.POST.get('test1')
        test2 = request.POST.get('test2')
        if test1 == "1" and test2 == "2" :
            TaskDes = TaskDescriptionDE.objects.all()
            taskdes = TaskDes.filter(id=1)
            return render(request, 'HTML/DE/TaskDetail.html', {"taskdes": taskdes, })
        else:
            return render(request, 'HTML/DE/Blank/intro-again.html', {})


# 跳转到taskDetailone页面
def DeTask1(request):
    TaskDes = TaskDescriptionDE.objects.all()
    taskdes = TaskDes.filter(id=1)
    return render(request, 'HTML/DE/TaskDetail.html',{
        "taskdes":taskdes,
    } )


# 判断去哪个页面
def SwitchDE(request):
    user_id = request.user.id
    mode_id = user_id % 4
    # 跳转到Top-down页面
    if mode_id == 0:
        task_all= TaskDescriptionDE.objects.all()
        taskdes = task_all.filter(id=1)
        all_techch = TechinforDE.objects.all().order_by('?')
        attribut1 = TDDesignDE.objects.all()
        attribut2 = TDDependencyDE.objects.all()
        attribut3 = TDDurationDE.objects.all()
        attribut4 = TDParticipationDE.objects.all()
        attribut5 = TDEvaluationDE.objects.all()
        user_id = request.user.id
        design_id = request.GET.get('design', "")
        if design_id:
            all_techch = all_techch.filter(TDDesign_id=int(design_id))

        dependency_id = request.GET.get('dependency', "")
        if dependency_id:
            all_techch = all_techch.filter(TDDependency_id=int(dependency_id))

        duration_id = request.GET.get('duration', "")
        if duration_id:
            all_techch = all_techch.filter(TDDuration_id=int(duration_id))

        participant_id = request.GET.get('participant', "")
        if participant_id:
            all_techch = all_techch.filter(TDParticipation_id=int(participant_id))

        evaluation_id = request.GET.get('evaluation', "")
        if evaluation_id:
            all_techch = all_techch.filter(TDEvaluation_id=int(evaluation_id))
        return render(request, 'HTML/DE/Top-down/Top-down 1.html',
                      {"all_techch": all_techch, "attribut1": attribut1, "attribut2": attribut2, "attribut3": attribut3,
                       "attribut4": attribut4, "attribut5": attribut5, "design_id": design_id,
                       "dependency_id": dependency_id, "duration_id": duration_id, "participant_id": participant_id,
                        "evaluation_id": evaluation_id,"taskdes":taskdes,
                       })
    # 跳转到Bottom-up页面
    elif mode_id == 1:
        task_all = TaskDescriptionDE.objects.all()
        taskdes = task_all.filter(id=1)
        all_techch = TechinforDE.objects.all().order_by('?')
        attribut1 = BUDesignDE.objects.all()
        attribut2 = BUCollectionDE.objects.all()
        attribut3 = BUDurationDE.objects.all()
        attribut4 = BUParticipantDE.objects.all()
        de_id = request.GET.get('de', "")
        if de_id:
            all_techch = all_techch.filter(BUDesign_id=int(de_id))

        col_id = request.GET.get('col', "")
        if col_id:
            all_techch = all_techch.filter(BUCollection_id=int(col_id))

        du_id = request.GET.get('du', "")
        if du_id:
            all_techch = all_techch.filter(BUCollection_id=int(du_id))

        pa_id = request.GET.get('pa', "")
        if pa_id:
            all_techch = all_techch.filter(BUParticipant_id=int(pa_id))

        return render(request, 'HTML/DE/Bottom-up/Bottom-up 1.html',
                      {"all_techch": all_techch, "attribut1": attribut1, "attribut2": attribut2, "attribut3": attribut3,
                       "attribut4": attribut4, "de_id": de_id, "col_id": col_id, "du_id": du_id, "pa_id": pa_id, "taskdes":taskdes,
                       })
    # 跳转到Tag Cloud页面
    elif mode_id == 2:
        all_techch = TechinforDE.objects.all().order_by('?')
        attribut1 = TagCloudDE.objects.all()
        task_all=TaskDescriptionDE.objects.all()
        taskdes = task_all.filter(id=1)
        attri1_id = request.GET.get('attri1', "")
        if attri1_id:
            all_techch = all_techch.filter(UserParticipationgroup=attri1_id)

        attri2_id = request.GET.get('attri2', "")
        if attri2_id:
            all_techch = all_techch.filter(MidDuration=attri2_id)

        attri3_id = request.GET.get('attri3', "")
        if attri3_id:
            all_techch = all_techch.filter(Observation=attri3_id)

        attri4_id = request.GET.get('attri4', "")
        if attri4_id:
            all_techch = all_techch.filter(IdeaGeneration=attri4_id)

        attri5_id = request.GET.get('attri5', "")
        if attri5_id:
            all_techch = all_techch.filter(CollaborationStakeholders=attri5_id)

        attri6_id = request.GET.get('attri6', "")
        if attri6_id:
            all_techch = all_techch.filter(FeedbackOnline=attri6_id)

        attri7_id = request.GET.get('attri7', "")
        if attri7_id:
            all_techch = all_techch.filter(PrototypeEvaluation=attri7_id)

        attri8_id = request.GET.get('attri8', "")
        if attri8_id:
            all_techch = all_techch.filter(DataCollection=attri8_id)

        attri9_id = request.GET.get('attri9', "")
        if attri9_id:
            all_techch = all_techch.filter(Prototyping=attri9_id)

        attri10_id = request.GET.get('attri10', "")
        if attri10_id:
            all_techch = all_techch.filter(ShortDuration=attri10_id)

        attri11_id = request.GET.get('attri11', "")
        if attri11_id:
            all_techch = all_techch.filter(Evaluation=attri11_id)

        attri12_id = request.GET.get('attri12', "")
        if attri12_id:
            all_techch = all_techch.filter(ProductEvaluation=attri12_id)

        attri13_id = request.GET.get('attri13', "")
        if attri13_id:
            all_techch = all_techch.filter(ProjectOrganization=attri13_id)

        attri14_id = request.GET.get('attri14', "")
        if attri14_id:
            all_techch = all_techch.filter(FlexibleLength=attri14_id)

        attri15_id = request.GET.get('attri15', "")
        if attri15_id:
            all_techch = all_techch.filter(UserParticipation=attri15_id)

        attri16_id = request.GET.get('attri16', "")
        if attri16_id:
            all_techch = all_techch.filter(InformationOrganization=attri16_id)

        attri17_id = request.GET.get('attri17', "")
        if attri17_id:
            all_techch = all_techch.filter(FeedbackOffline=attri17_id)

        attri18_id = request.GET.get('attri18', "")
        if attri18_id:
            all_techch = all_techch.filter(LongDuration=attri18_id)

        attri19_id = request.GET.get('attri19', "")
        if attri19_id:
            all_techch = all_techch.filter(UserResearch=attri19_id)

        attri20_id = request.GET.get('attri20', "")
        if attri20_id:
            all_techch = all_techch.filter(RelationshipDependency=attri20_id)

        attri21_id = request.GET.get('attri21', "")
        if attri21_id:
            all_techch = all_techch.filter(UserSimulation=attri21_id)

        attri22_id = request.GET.get('attri22', "")
        if attri22_id:
            all_techch = all_techch.filter(ExpertParticipation=attri22_id)

        attri23_id = request.GET.get('attri23', "")
        if attri23_id:
            all_techch = all_techch.filter(UXEvaluation=attri23_id)

        attri24_id = request.GET.get('attri24', "")
        if attri24_id:
            all_techch = all_techch.filter(FeedbackCollection=attri24_id)

        return render(request, 'HTML/DE/Tag Cloud/Tag Cloud 1.html',
                      {"all_techch": all_techch, "attribut1": attribut1, "attri1_id": attri1_id,
                       "attri2_id": attri2_id, "attri3_id": attri3_id, "attri4_id": attri4_id,
                       "attri5_id": attri5_id, "attri6_id": attri6_id, "attri7_id": attri7_id,
                       "attri8_id": attri8_id, "attri9_id": attri9_id, "attri10_id": attri10_id,
                       "attri11_id": attri11_id, "attri12_id": attri12_id, "attri13_id": attri13_id,
                       "attri14_id": attri14_id, "attri15_id": attri15_id, "attri16_id": attri16_id,
                       "attri17_id": attri17_id, "attri18_id": attri18_id, "attri19_id": attri19_id,
                       "attri20_id": attri20_id, "attri21_id": attri21_id, "attri22_id": attri22_id,
                       "attri23_id": attri23_id, "attri24_id": attri24_id,"taskdes":taskdes,
                       })
    # 跳转到blank页面
    else:
        all_tech = TechinforDE.objects.all()
        task_all=TaskDescriptionDE.objects.all()
        taskdes = task_all.filter(id=1)
        return render(request, 'HTML/DE/Blank/blank 1.html', {
            "all_tech": all_tech,
            "taskdes":taskdes,
        })



# 如果选择了Blank
# 添加选择的tech，并跳转到Post-question 1页面
def B_AddTech1DE(request):
    selected1 = request.POST.get('selectedone',"")
    selected2 = request.POST.get('selectedtwo',"")
    selected3 = request.POST.get('selectedthree',"")
    user_id = request.user.id
    mode_id = request.user.id % 4
    SelectedTechniqueOne.objects.create(chose_Tech1=selected1,chose_Tech2=selected2, chose_Tech3=selected3,Test_User_id=user_id,mode_id= mode_id )
    return render(request, 'HTML/DE/post-test Q3.html',{ })


# 添加Post-question1到数据库，并跳转到Task-Detail 2页面
def B_AddPost1DE(request):
    if request.method == "POST":
        post1 = request.POST.get('post1')
        post2 = request.POST.get('post2')
        post3 = request.POST.get('post3')
        post4 = request.POST.get('post4')
        post5 = request.POST.get('post5')
        post6 = request.POST.get('post6')
        post7 = request.POST.get('post7')
        post8 = request.POST.get('post8')
        post9 = request.POST.get('post9')
        post10 = request.POST.get('post10')
        post11 = request.POST.get('post11')
        post12 = request.POST.get('post12')
        post13 = request.POST.get('post13')
        post14 = request.POST.get('post14')
        post15 = request.POST.get('post15')
        post16 = request.POST.get('post16')
        user_id = request.user.id
        mode = request.user.id % 4
        PostQuestionResultOne.objects.create(mode_id=mode,Test_User_id=user_id,Q1_proficiency=post1,Q2_globalapproach=post2,Q3_localizedapproach=post3,Q4_objects=post4,Q5_rulesbased=post5,Q6_learncategory=post6,Q7_organize=post7,Q8_formallogic=post8,Q9_logicalrules=post9,Q10_individual=post10,Q11_surrounding=post11,Q12_littelrule=post12,Q13_difficultrule=post13,Q14_thematically=post14,Q15_dialectical=post15,Q16_contradiction=post16,)
        TaskDes = TaskDescriptionDE.objects.all()
        taskdes = TaskDes.filter(id=2)
        return render(request, 'HTML/DE/Blank/TaskDetailtwo.html',{
            "taskdes":taskdes,
        })


# 跳转到blank2，显示tech信息等内容
def DE_blank2(request):
    all_tech = TechinforDE.objects.all().order_by('?')
    task_all = TaskDescriptionDE.objects.all()
    taskdes = task_all.filter(id=2)
    return render(request, 'HTML/DE/Blank/blank 2.html',
    {
        "all_tech": all_tech,
        "taskdes":taskdes,
    })


# 添加选择技术到数据库，并跳转到post-question2页面
def B_AddTech2DE(request):
    selected1 = request.POST.get('selectedone',"")
    selected2 = request.POST.get('selectedtwo',"")
    selected3 = request.POST.get('selectedthree',"")
    user_id = request.user.id
    mode = request.user.id % 4
    taskdes_all = TaskDescriptionDE.objects.all()
    taskdes = taskdes_all.filter(id=2)
    SelectedTechniqueTwo.objects.create(mode_id=mode,chose_Tech1=selected1,chose_Tech2=selected2, chose_Tech3=selected3,Test_User_id=user_id )
    return render(request, 'HTML/DE/Blank/post-test 2.html',{
        "taskdes":taskdes,
    })


# 添加post-question2 答案到数据库，并跳转到TaskDetail 3页面
def B_AddPost2DE(request):
    if request.method == "POST":
        post1 = request.POST.get('post1')
        post2 = request.POST.get('post2')
        post3 = request.POST.get('post3')
        post4 = request.POST.get('post4')
        post5 = request.POST.get('post5')
        post6 = request.POST.get('post6')
        post7 = request.POST.get('post7')
        post8 = request.POST.get('post8')
        post9 = request.POST.get('post9')
        post10 = request.POST.get('post10')
        post11 = request.POST.get('post11')
        post12 = request.POST.get('post12')
        post13 = request.POST.get('post13')
        post14 = request.POST.get('post14')
        post15 = request.POST.get('post15')
        post16 = request.POST.get('post16')
        user_id = request.user.id
        mode = request.user.id % 4
        PostQuestionResultOne.objects.create(mode_id=mode,Test_User_id=user_id,Q1_proficiency=post1,Q2_globalapproach=post2,Q3_localizedapproach=post3,Q4_objects=post4,Q5_rulesbased=post5,Q6_learncategory=post6,Q7_organize=post7,Q8_formallogic=post8,Q9_logicalrules=post9,Q10_individual=post10,Q11_surrounding=post11,Q12_littelrule=post12,Q13_difficultrule=post13,Q14_thematically=post14,Q15_dialectical=post15,Q16_contradiction=post16,)
        TaskDes = TaskDescriptionDE.objects.all()
        taskdes = TaskDes.filter(id=3)
        return render(request, 'HTML/DE/Blank/TaskDetailthree.html',{
            "taskdes":taskdes,
        })


# 跳转到blank3页面，并显示相关信息
def DE_blank3(request):
    all_tech = TechinforDE.objects.all().order_by('?')
    task_all=TaskDescriptionDE.objects.all()
    taskdes =task_all.filter(id=3)
    return render(request, 'HTML/DE/Blank/blank 3.html', {
        "all_tech": all_tech,
        "taskdes":taskdes,
    })


# 添加选中技术，并跳转到post-question 3页面
def B_AddTech3DE(request):
    selected1 = request.POST.get('selectedone',"")
    selected2 = request.POST.get('selectedtwo',"")
    selected3 = request.POST.get('selectedthree',"")
    user_id = request.user.id
    mode = request.user.id % 4
    taskdes_all = TaskDescriptionEN.objects.all()
    taskdes = taskdes_all.filter(id=3)
    SelectedTechniqueThree.objects.create(mode_id=mode,chose_Tech1=selected1,chose_Tech2=selected2, chose_Tech3=selected3,Test_User_id=user_id )
    return render(request, 'HTML/DE/post-test Q3.html',{
        "taskdes":taskdes,
    })


# 添加post-question3 到数据库，并转到post-test Q3A页面
def AddPost3De(request):
    if request.method == "POST":
        post1 = request.POST.get('post1')
        post2 = request.POST.get('post2')
        post3 = request.POST.get('post3')
        post4 = request.POST.get('post4')
        post5 = request.POST.get('post5')
        post6 = request.POST.get('post6')
        user_id = request.user.id
        mode = request.user.id % 4
        PostQuestionResultThree.objects.create(mode_id=mode,Test_User_id=user_id, Q1_proficiency=post1, Q2_globalapproach=post2,
                                             Q3_localizedapproach=post3, Q4_objects=post4, Q5_rulesbased=post5,
                                             Q6_learncategory=post6,)
        return render(request,'HTML/DE/post-test Q3A.html',{})


# 添加post-question3A 到数据库，并转到post-test Q3B页面
def AddPost3ADe(request):
    if request.method == "POST":
            post7 = request.POST.get('post7')
            post8 = request.POST.get('post8')
            post9 = request.POST.get('post9')
            post10 = request.POST.get('post10')
            post11 = request.POST.get('post11')
            post12 = request.POST.get('post12')
            post13 = request.POST.get('post13')
            post14 = request.POST.get('post14')
            post15 = request.POST.get('post15')
            post16 = request.POST.get('post16')
            user_id = request.user.id
            mode = request.user.id % 4
            PostQuestionResultThree.objects.filter(Test_User_id=user_id).update(
                                                   Q7_organize=post7, Q8_formallogic=post8, Q9_logicalrules=post9,
                                                   Q10_individual=post10, Q11_surrounding=post11, Q12_littelrule=post12,
                                                   Q13_difficultrule=post13,Q14_thematically=post14, Q15_dialectical=post15,
                                                       Q16_contradiction=post16, )
            return render(request, 'HTML/DE/post-test Q3B.html', {})

# 添加post-question3B 到数据库，并转到END页面
def AddPost3BDe(request):
    if request.method == "POST":
        post17 = request.POST.get('post17')
        post18 = request.POST.get('post18')
        post19 = request.POST.get('post19')
        post20 = request.POST.get('post20')
        post21 = request.POST.get('post21')
        post22 = request.POST.get('post22')
        user_id = request.user.id
        mode = request.user.id % 4
        PostQuestionResultThree.objects.filter(Test_User_id=user_id).update( Q17_pressures=post17,
                                                       Q18_thematically=post18, Q19_littelrule=post19,
                                                       Q20_difficultrule=post20, Q21_thematically=post21,
                                                       Q22_dialectical=post22,)
        UserProfile.objects.filter(id=user_id).update(endtime=datetime.now(),mode_id=mode,)
        return render(request, 'HTML/DE/end.html', {})






# 如果选择了Top-down
# 添加选择的tech，并跳转到Post-question 1页面
def T_AddTech1DE(request):
    selected1 = request.POST.get('selectedone',"")
    selected2 = request.POST.get('selectedtwo',"")
    selected3 = request.POST.get('selectedthree',"")
    user_id = request.user.id
    mode = request.user.id % 4
    SelectedTechniqueOne.objects.create(chose_Tech1=selected1,chose_Tech2=selected2, chose_Tech3=selected3,Test_User_id=user_id ,mode_id = mode)
    return render(request, 'HTML/DE/post-test Q3.html',{
    })


# 添加Post-question1到数据库，并跳转到Task-Detail 2页面
def T_AddPost1DE(request):
    if request.method == "POST":
        post1 = request.POST.get('post1')
        post2 = request.POST.get('post2')
        post3 = request.POST.get('post3')
        post4 = request.POST.get('post4')
        post5 = request.POST.get('post5')
        post6 = request.POST.get('post6')
        post7 = request.POST.get('post7')
        post8 = request.POST.get('post8')
        post9 = request.POST.get('post9')
        post10 = request.POST.get('post10')
        post11 = request.POST.get('post11')
        post12 = request.POST.get('post12')
        post13 = request.POST.get('post13')
        post14 = request.POST.get('post14')
        post15 = request.POST.get('post15')
        post16 = request.POST.get('post16')
        user_id = request.user.id
        mode = request.user.id % 4
        PostQuestionResultOne.objects.create(mode_id=mode,Test_User_id=user_id,Q1_proficiency=post1,Q2_globalapproach=post2,Q3_localizedapproach=post3,Q4_objects=post4,Q5_rulesbased=post5,Q6_learncategory=post6,Q7_organize=post7,Q8_formallogic=post8,Q9_logicalrules=post9,Q10_individual=post10,Q11_surrounding=post11,Q12_littelrule=post12,Q13_difficultrule=post13,Q14_thematically=post14,Q15_dialectical=post15,Q16_contradiction=post16,)
        TaskDes = TaskDescriptionDE.objects.all()
        taskdes = TaskDes.filter(id=2)
        return render(request, 'HTML/DE/Top-down/TaskDetailtwo.html',{
            "taskdes":taskdes,
        })


# 跳转到Top-down2，显示tech信息等内容
def DE_Top2(request):
    task_all = TaskDescriptionDE.objects.all()
    taskdes = task_all.filter(id=2)
    all_techch = TechinforEN.objects.all().order_by('?')
    attribut1 = TDDesignDE.objects.all()
    attribut2 = TDDependencyDE.objects.all()
    attribut3 = TDDurationDE.objects.all()
    attribut4 = TDParticipationDE.objects.all()
    attribut5 = TDEvaluationDE.objects.all()
    user_id = request.user.id
    design_id = request.GET.get('design', "")
    if design_id:
        all_techch = all_techch.filter(TDDesign_id=int(design_id))

    dependency_id = request.GET.get('dependency', "")
    if dependency_id:
        all_techch = all_techch.filter(TDDependency_id=int(dependency_id))

    duration_id = request.GET.get('duration', "")
    if duration_id:
        all_techch = all_techch.filter(TDDuration_id=int(duration_id))

    participant_id = request.GET.get('participant', "")
    if participant_id:
        all_techch = all_techch.filter(TDParticipation_id=int(participant_id))

    evaluation_id = request.GET.get('evaluation', "")
    if evaluation_id:
        all_techch = all_techch.filter(TDEvaluation_id=int(evaluation_id))
    return render(request, 'HTML/DE/Top-down/Top-down 2.html',
                  {"all_techch": all_techch, "attribut1": attribut1, "attribut2": attribut2, "attribut3": attribut3,
                   "attribut4": attribut4, "attribut5": attribut5, "design_id": design_id,
                   "dependency_id": dependency_id, "duration_id": duration_id, "participant_id": participant_id,
                   "evaluation_id": evaluation_id, "taskdes": taskdes, })


# 添加选择技术到数据库，并跳转到post-question2页面
def T_AddTech2DE(request):
    selected1 = request.POST.get('selectedone',"")
    selected2 = request.POST.get('selectedtwo',"")
    selected3 = request.POST.get('selectedthree',"")
    user_id = request.user.id
    mode = request.user.id % 4
    taskdes_all = TaskDescriptionDE.objects.all()
    taskdes = taskdes_all.filter(id=2)
    SelectedTechniqueTwo.objects.create(mode_id=mode,chose_Tech1=selected1,chose_Tech2=selected2, chose_Tech3=selected3,Test_User_id=user_id )
    return render(request, 'HTML/DE/Top-down/post-test 2.html', {
        "taskdes":taskdes,
    })


# 添加post-question2 答案到数据库，并跳转到TaskDetail 3页面
def T_AddPost2DE(request):
    if request.method == "POST":
        post1 = request.POST.get('post1')
        post2 = request.POST.get('post2')
        post3 = request.POST.get('post3')
        post4 = request.POST.get('post4')
        post5 = request.POST.get('post5')
        post6 = request.POST.get('post6')
        post7 = request.POST.get('post7')
        post8 = request.POST.get('post8')
        post9 = request.POST.get('post9')
        post10 = request.POST.get('post10')
        post11 = request.POST.get('post11')
        post12 = request.POST.get('post12')
        post13 = request.POST.get('post13')
        post14 = request.POST.get('post14')
        post15 = request.POST.get('post15')
        post16 = request.POST.get('post16')
        user_id = request.user.id
        mode = request.user.id % 4
        PostQuestionResultTwo.objects.create(mode_id=mode,Test_User_id=user_id,Q1_proficiency=post1,Q2_globalapproach=post2,Q3_localizedapproach=post3,Q4_objects=post4,Q5_rulesbased=post5,Q6_learncategory=post6,Q7_organize=post7,Q8_formallogic=post8,Q9_logicalrules=post9,Q10_individual=post10,Q11_surrounding=post11,Q12_littelrule=post12,Q13_difficultrule=post13,Q14_thematically=post14,Q15_dialectical=post15,Q16_contradiction=post16,)
        TaskDes = TaskDescriptionDE.objects.all()
        taskdes = TaskDes.filter(id=3)
        return render(request, 'HTML/DE/Top-down/TaskDetailthree.html',{
            "taskdes":taskdes,
        })


# 跳转到Top-down3页面，并显示相关信息
def DE_Top3(request):
    task_all = TaskDescriptionDE.objects.all()
    taskdes = task_all.filter(id=3)
    all_techch = TechinforDE.objects.all().order_by('?')
    attribut1 = TDDesignDE.objects.all()
    attribut2 = TDDependencyDE.objects.all()
    attribut3 = TDDurationDE.objects.all()
    attribut4 = TDParticipationDE.objects.all()
    attribut5 = TDEvaluationDE.objects.all()
    user_id = request.user.id
    design_id = request.GET.get('design', "")
    if design_id:
        all_techch = all_techch.filter(TDDesign_id=int(design_id))

    dependency_id = request.GET.get('dependency', "")
    if dependency_id:
        all_techch = all_techch.filter(TDDependency_id=int(dependency_id))

    duration_id = request.GET.get('duration', "")
    if duration_id:
        all_techch = all_techch.filter(TDDuration_id=int(duration_id))

    participant_id = request.GET.get('participant', "")
    if participant_id:
        all_techch = all_techch.filter(TDParticipation_id=int(participant_id))

    evaluation_id = request.GET.get('evaluation', "")
    if evaluation_id:
        all_techch = all_techch.filter(TDEvaluation_id=int(evaluation_id))
    return render(request, 'HTML/DE/Top-down/Top-down 3.html',
                  {"all_techch": all_techch, "attribut1": attribut1, "attribut2": attribut2, "attribut3": attribut3,
                   "attribut4": attribut4, "attribut5": attribut5, "design_id": design_id,
                   "dependency_id": dependency_id, "duration_id": duration_id, "participant_id": participant_id,
                   "evaluation_id": evaluation_id, "taskdes": taskdes, })


# 添加选中技术，并跳转到post-question 3页面
def T_AddTech3DE(request):
    selected1 = request.POST.get('selectedone',"")
    selected2 = request.POST.get('selectedtwo',"")
    selected3 = request.POST.get('selectedthree',"")
    user_id = request.user.id
    mode = request.user.id % 4
    taskdes_all = TaskDescriptionDE.objects.all()
    taskdes = taskdes_all.filter(id=3)
    SelectedTechniqueThree.objects.create(mode_id=mode,chose_Tech1=selected1,chose_Tech2=selected2, chose_Tech3=selected3,Test_User_id=user_id )
    return render(request, 'HTML/DE/post-test Q3.html',{
        "taskdes":taskdes,
    })



# 如果选择了Bottom-up
# 添加选择的tech，并跳转到Post-question 1页面
def U_AddTech1DE(request):
    selected1 = request.POST.get('selectedone',"")
    selected2 = request.POST.get('selectedtwo',"")
    selected3 = request.POST.get('selectedthree',"")
    user_id = request.user.id
    mode = request.user.id % 4
    SelectedTechniqueOne.objects.create(mode_id=mode,chose_Tech1=selected1,chose_Tech2=selected2, chose_Tech3=selected3,Test_User_id=user_id )
    return render(request, 'HTML/DE/post-test Q3.html',{
    })


# 添加Post-question1到数据库，并跳转到Task-Detail 2页面
def U_AddPost1DE(request):
    if request.method == "POST":
        post1 = request.POST.get('post1')
        post2 = request.POST.get('post2')
        post3 = request.POST.get('post3')
        post4 = request.POST.get('post4')
        post5 = request.POST.get('post5')
        post6 = request.POST.get('post6')
        post7 = request.POST.get('post7')
        post8 = request.POST.get('post8')
        post9 = request.POST.get('post9')
        post10 = request.POST.get('post10')
        post11 = request.POST.get('post11')
        post12 = request.POST.get('post12')
        post13 = request.POST.get('post13')
        post14 = request.POST.get('post14')
        post15 = request.POST.get('post15')
        post16 = request.POST.get('post16')
        user_id = request.user.id
        mode = request.user.id % 4
        PostQuestionResultOne.objects.create(mode_id=mode,Test_User_id=user_id,Q1_proficiency=post1,Q2_globalapproach=post2,Q3_localizedapproach=post3,Q4_objects=post4,Q5_rulesbased=post5,Q6_learncategory=post6,Q7_organize=post7,Q8_formallogic=post8,Q9_logicalrules=post9,Q10_individual=post10,Q11_surrounding=post11,Q12_littelrule=post12,Q13_difficultrule=post13,Q14_thematically=post14,Q15_dialectical=post15,Q16_contradiction=post16,)
        TaskDes = TaskDescriptionDE.objects.all()
        taskdes = TaskDes.filter(id=2)
        return render(request, 'HTML/DE/Bottom-up/TaskDetailtwo.html',{
            "taskdes":taskdes,
        })



# 跳转到Bottom-up 2，显示tech信息等内容
def DE_Up2(request):
    all_techch = TechinforDE.objects.all().order_by('?')
    task_all = TaskDescriptionDE.objects.all()
    taskdes = task_all.filter(id=2)
    attribut1 = BUDesignDE.objects.all()
    attribut2 = BUCollectionDE.objects.all()
    attribut3 = BUDurationDE.objects.all()
    attribut4 = BUParticipantDE.objects.all()
    de_id = request.GET.get('de', "")
    if de_id:
        all_techch = all_techch.filter(BUDesign_id=int(de_id))

    col_id = request.GET.get('col', "")
    if col_id:
        all_techch = all_techch.filter(BUCollection_id=int(col_id))

    du_id = request.GET.get('du', "")
    if du_id:
        all_techch = all_techch.filter(BUCollection_id=int(du_id))

    pa_id = request.GET.get('pa', "")
    if pa_id:
        all_techch = all_techch.filter(BUParticipant_id=int(pa_id))

    return render(request, 'HTML/DE/Bottom-up/Bottom-up 2.html',
                  {"all_techch": all_techch, "attribut1": attribut1, "attribut2": attribut2, "attribut3": attribut3,
                   "attribut4": attribut4, "de_id": de_id, "col_id": col_id, "du_id": du_id, "pa_id": pa_id,
                   "taskdes": taskdes, })


# 添加选择技术到数据库，并跳转到Bottom-up 2页面
def U_AddTech2DE(request):
    selected1 = request.POST.get('selectedone',"")
    selected2 = request.POST.get('selectedtwo',"")
    selected3 = request.POST.get('selectedthree',"")
    user_id = request.user.id
    mode = request.user.id % 4
    taskdes_all = TaskDescriptionDE.objects.all()
    taskdes = taskdes_all.filter(id=2)
    SelectedTechniqueOne.objects.create(mode_id=mode,chose_Tech1=selected1,chose_Tech2=selected2, chose_Tech3=selected3,Test_User_id=user_id )
    return render(request, 'HTML/DE/Bottom-up/post-test 2.html',{
        "taskdes":taskdes,
    })


# 添加post-question2 答案到数据库，并跳转到TaskDetail 3页面
def U_AddPost2DE(request):
    if request.method == "POST":
        post1 = request.POST.get('post1')
        post2 = request.POST.get('post2')
        post3 = request.POST.get('post3')
        post4 = request.POST.get('post4')
        post5 = request.POST.get('post5')
        post6 = request.POST.get('post6')
        post7 = request.POST.get('post7')
        post8 = request.POST.get('post8')
        post9 = request.POST.get('post9')
        post10 = request.POST.get('post10')
        post11 = request.POST.get('post11')
        post12 = request.POST.get('post12')
        post13 = request.POST.get('post13')
        post14 = request.POST.get('post14')
        post15 = request.POST.get('post15')
        post16 = request.POST.get('post16')
        user_id = request.user.id
        mode = request.user.id % 4
        PostQuestionResultOne.objects.create(mode_id=mode,Test_User_id=user_id,Q1_proficiency=post1,Q2_globalapproach=post2,Q3_localizedapproach=post3,Q4_objects=post4,Q5_rulesbased=post5,Q6_learncategory=post6,Q7_organize=post7,Q8_formallogic=post8,Q9_logicalrules=post9,Q10_individual=post10,Q11_surrounding=post11,Q12_littelrule=post12,Q13_difficultrule=post13,Q14_thematically=post14,Q15_dialectical=post15,Q16_contradiction=post16, )
        TaskDes = TaskDescriptionDE.objects.all()
        taskdes = TaskDes.filter(id=3)
        return render(request, 'HTML/DE/Bottom-up/TaskDetailthree.html',{
            "taskdes":taskdes,
        })


# 跳转到Bottom-up3页面，并显示相关信息
def DE_Up3(request):
    all_techch = TechinforDE.objects.all().order_by('?')
    task_all = TaskDescriptionDE.objects.all()
    taskdes = task_all.filter(id=3)
    attribut1 = BUDesignDE.objects.all()
    attribut2 = BUCollectionDE.objects.all()
    attribut3 = BUDurationDE.objects.all()
    attribut4 = BUParticipantDE.objects.all()
    de_id = request.GET.get('de', "")
    if de_id:
        all_techch = all_techch.filter(BUDesign_id=int(de_id))

    col_id = request.GET.get('col', "")
    if col_id:
        all_techch = all_techch.filter(BUCollection_id=int(col_id))

    du_id = request.GET.get('du', "")
    if du_id:
        all_techch = all_techch.filter(BUCollection_id=int(du_id))

    pa_id = request.GET.get('pa', "")
    if pa_id:
        all_techch = all_techch.filter(BUParticipant_id=int(pa_id))

    return render(request, 'HTML/DE/Bottom-up/Bottom-up 3.html',
                  {"all_techch": all_techch, "attribut1": attribut1, "attribut2": attribut2, "attribut3": attribut3,
                   "attribut4": attribut4, "de_id": de_id, "col_id": col_id, "du_id": du_id, "pa_id": pa_id,
                   "taskdes": taskdes, })


# 添加选中技术，并跳转到post-question 3页面
def U_AddTech3EN(request):
    selected1 = request.POST.get('selectedone',"")
    selected2 = request.POST.get('selectedtwo',"")
    selected3 = request.POST.get('selectedthree',"")
    user_id = request.user.id
    mode = request.user.id % 4
    taskdes_all = TaskDescriptionEN.objects.all()
    taskdes = taskdes_all.filter(id=3)
    SelectedTechniqueOne.objects.create(mode_id=mode,chose_Tech1=selected1,chose_Tech2=selected2, chose_Tech3=selected3,Test_User_id=user_id )
    return render(request, 'HTML/DE/post-test Q3.html',{
        "taskdes":taskdes,
    })






# 选择了Tag Cloud
# 添加选择的tech，并跳转到Post-question 1页面
def C_AddTech1DE(request):
    selected1 = request.POST.get('selectedone',"")
    selected2 = request.POST.get('selectedtwo',"")
    selected3 = request.POST.get('selectedthree',"")
    user_id = request.user.id
    mode = request.user.id % 4
    SelectedTechniqueOne.objects.create(mode_id=mode,chose_Tech1=selected1,chose_Tech2=selected2, chose_Tech3=selected3,Test_User_id=user_id )
    return render(request, 'HTML/DE/post-test Q3.html',{
    })


# 添加Post-question1到数据库，并跳转到Task-Detail 2页面
def C_AddPost1DE(request):
    if request.method == "POST":
        post1 = request.POST.get('post1')
        post2 = request.POST.get('post2')
        post3 = request.POST.get('post3')
        post4 = request.POST.get('post4')
        post5 = request.POST.get('post5')
        post6 = request.POST.get('post6')
        post7 = request.POST.get('post7')
        post8 = request.POST.get('post8')
        post9 = request.POST.get('post9')
        post10 = request.POST.get('post10')
        post11 = request.POST.get('post11')
        post12 = request.POST.get('post12')
        post13 = request.POST.get('post13')
        post14 = request.POST.get('post14')
        post15 = request.POST.get('post15')
        post16 = request.POST.get('post16')
        user_id = request.user.id
        mode = request.user.id % 4
        PostQuestionResultOne.objects.create(mode_id=mode,Test_User_id=user_id,Q1_proficiency=post1,Q2_globalapproach=post2,Q3_localizedapproach=post3,Q4_objects=post4,Q5_rulesbased=post5,Q6_learncategory=post6,Q7_organize=post7,Q8_formallogic=post8,Q9_logicalrules=post9,Q10_individual=post10,Q11_surrounding=post11,Q12_littelrule=post12,Q13_difficultrule=post13,Q14_thematically=post14,Q15_dialectical=post15,Q16_contradiction=post16,)
        TaskDes = TaskDescriptionDE.objects.all()
        taskdes = TaskDes.filter(id=2)
        return render(request, 'HTML/DE/Tag Cloud/TaskDetailtwo.html',{
            "taskdes":taskdes,
        })


# 跳转到Tag Cloud 2，显示tech信息等内容
def DE_C2(request):
    all_techch = TechinforDE.objects.all().order_by('?')
    attribut1 = TagCloudDE.objects.all()
    task_all = TaskDescriptionDE.objects.all()
    taskdes = task_all.filter(id=2)

    attri1_id = request.GET.get('attri1', "")
    if attri1_id:
        all_techch = all_techch.filter(UserParticipationgroup=attri1_id)

    attri2_id = request.GET.get('attri2', "")
    if attri2_id:
        all_techch = all_techch.filter(MidDuration=attri2_id)

    attri3_id = request.GET.get('attri3', "")
    if attri3_id:
        all_techch = all_techch.filter(Observation=attri3_id)

    attri4_id = request.GET.get('attri4', "")
    if attri4_id:
        all_techch = all_techch.filter(IdeaGeneration=attri4_id)

    attri5_id = request.GET.get('attri5', "")
    if attri5_id:
        all_techch = all_techch.filter(CollaborationStakeholders=attri5_id)

    attri6_id = request.GET.get('attri6', "")
    if attri6_id:
        all_techch = all_techch.filter(FeedbackOnline=attri6_id)

    attri7_id = request.GET.get('attri7', "")
    if attri7_id:
        all_techch = all_techch.filter(PrototypeEvaluation=attri7_id)

    attri8_id = request.GET.get('attri8', "")
    if attri8_id:
        all_techch = all_techch.filter(DataCollection=attri8_id)

    attri9_id = request.GET.get('attri9', "")
    if attri9_id:
        all_techch = all_techch.filter(Prototyping=attri9_id)

    attri10_id = request.GET.get('attri10', "")
    if attri10_id:
        all_techch = all_techch.filter(ShortDuration=attri10_id)

    attri11_id = request.GET.get('attri11', "")
    if attri11_id:
        all_techch = all_techch.filter(Evaluation=attri11_id)

    attri12_id = request.GET.get('attri12', "")
    if attri12_id:
        all_techch = all_techch.filter(ProductEvaluation=attri12_id)

    attri13_id = request.GET.get('attri13', "")
    if attri13_id:
        all_techch = all_techch.filter(ProjectOrganization=attri13_id)

    attri14_id = request.GET.get('attri14', "")
    if attri14_id:
        all_techch = all_techch.filter(FlexibleLength=attri14_id)

    attri15_id = request.GET.get('attri15', "")
    if attri15_id:
        all_techch = all_techch.filter(UserParticipation=attri15_id)

    attri16_id = request.GET.get('attri16', "")
    if attri16_id:
        all_techch = all_techch.filter(InformationOrganization=attri16_id)

    attri17_id = request.GET.get('attri17', "")
    if attri17_id:
        all_techch = all_techch.filter(FeedbackOffline=attri17_id)

    attri18_id = request.GET.get('attri18', "")
    if attri18_id:
        all_techch = all_techch.filter(LongDuration=attri18_id)

    attri19_id = request.GET.get('attri19', "")
    if attri19_id:
        all_techch = all_techch.filter(UserResearch=attri19_id)

    attri20_id = request.GET.get('attri20', "")
    if attri20_id:
        all_techch = all_techch.filter(RelationshipDependency=attri20_id)

    attri21_id = request.GET.get('attri21', "")
    if attri21_id:
        all_techch = all_techch.filter(UserSimulation=attri21_id)

    attri22_id = request.GET.get('attri22', "")
    if attri22_id:
        all_techch = all_techch.filter(ExpertParticipation=attri22_id)

    attri23_id = request.GET.get('attri23', "")
    if attri23_id:
        all_techch = all_techch.filter(UXEvaluation=attri23_id)

    attri24_id = request.GET.get('attri24', "")
    if attri24_id:
        all_techch = all_techch.filter(FeedbackCollection=attri24_id)

    return render(request, 'HTML/DE/Tag Cloud/Tag Cloud 2.html', {
        "all_techch": all_techch,
        "taskdes":taskdes,
        "attribut1":attribut1,
    })


# 添加选择技术到数据库，并跳转到post-question2页面
def C_AddTech2DE(request):
    selected1 = request.POST.get('selectedone',"")
    selected2 = request.POST.get('selectedtwo',"")
    selected3 = request.POST.get('selectedthree',"")
    user_id = request.user.id
    mode = request.user.id % 4
    taskdes_all = TaskDescriptionDE.objects.all()
    taskdes = taskdes_all.filter(id=2)
    SelectedTechniqueOne.objects.create(mode_id=mode,chose_Tech1=selected1,chose_Tech2=selected2, chose_Tech3=selected3,Test_User_id=user_id )
    return render(request, 'HTML/DE/Tag Cloud/post-test 2.html', {
        "taskdes":taskdes,
    })


# 添加post-question2 答案到数据库，并跳转到TaskDetail 3页面
def C_AddPost2DE(request):
    if request.method == "POST":
        post1 = request.POST.get('post1')
        post2 = request.POST.get('post2')
        post3 = request.POST.get('post3')
        post4 = request.POST.get('post4')
        post5 = request.POST.get('post5')
        post6 = request.POST.get('post6')
        post7 = request.POST.get('post7')
        post8 = request.POST.get('post8')
        post9 = request.POST.get('post9')
        post10 = request.POST.get('post10')
        post11 = request.POST.get('post11')
        post12 = request.POST.get('post12')
        post13 = request.POST.get('post13')
        post14 = request.POST.get('post14')
        post15 = request.POST.get('post15')
        post16 = request.POST.get('post16')
        user_id = request.user.id
        mode = request.user.id % 4
        PostQuestionResultOne.objects.create(mode_id=mode,Test_User_id=user_id,Q1_proficiency=post1,Q2_globalapproach=post2,Q3_localizedapproach=post3,Q4_objects=post4,Q5_rulesbased=post5,Q6_learncategory=post6,Q7_organize=post7,Q8_formallogic=post8,Q9_logicalrules=post9,Q10_individual=post10,Q11_surrounding=post11,Q12_littelrule=post12,Q13_difficultrule=post13,Q14_thematically=post14,Q15_dialectical=post15,Q16_contradiction=post16,)
        TaskDes = TaskDescriptionDE.objects.all()
        taskdes = TaskDes.filter(id=3)
        return render(request, 'HTML/DE/Tag Cloud/TaskDetailthree.html',{
            "taskdes":taskdes,
        })


# 跳转到Tag Cloud 3页面，并显示相关信息
def DE_C3(request):
    all_techch = TechinforDE.objects.all().order_by('?')
    attribut1 = TagCloudDE.objects.all()
    task_all = TaskDescriptionDE.objects.all()
    taskdes = task_all.filter(id=2)

    attri1_id = request.GET.get('attri1', "")
    if attri1_id:
        all_techch = all_techch.filter(UserParticipationgroup=attri1_id)

    attri2_id = request.GET.get('attri2', "")
    if attri2_id:
        all_techch = all_techch.filter(MidDuration=attri2_id)

    attri3_id = request.GET.get('attri3', "")
    if attri3_id:
        all_techch = all_techch.filter(Observation=attri3_id)

    attri4_id = request.GET.get('attri4', "")
    if attri4_id:
        all_techch = all_techch.filter(IdeaGeneration=attri4_id)

    attri5_id = request.GET.get('attri5', "")
    if attri5_id:
        all_techch = all_techch.filter(CollaborationStakeholders=attri5_id)

    attri6_id = request.GET.get('attri6', "")
    if attri6_id:
        all_techch = all_techch.filter(FeedbackOnline=attri6_id)

    attri7_id = request.GET.get('attri7', "")
    if attri7_id:
        all_techch = all_techch.filter(PrototypeEvaluation=attri7_id)

    attri8_id = request.GET.get('attri8', "")
    if attri8_id:
        all_techch = all_techch.filter(DataCollection=attri8_id)

    attri9_id = request.GET.get('attri9', "")
    if attri9_id:
        all_techch = all_techch.filter(Prototyping=attri9_id)

    attri10_id = request.GET.get('attri10', "")
    if attri10_id:
        all_techch = all_techch.filter(ShortDuration=attri10_id)

    attri11_id = request.GET.get('attri11', "")
    if attri11_id:
        all_techch = all_techch.filter(Evaluation=attri11_id)

    attri12_id = request.GET.get('attri12', "")
    if attri12_id:
        all_techch = all_techch.filter(ProductEvaluation=attri12_id)

    attri13_id = request.GET.get('attri13', "")
    if attri13_id:
        all_techch = all_techch.filter(ProjectOrganization=attri13_id)

    attri14_id = request.GET.get('attri14', "")
    if attri14_id:
        all_techch = all_techch.filter(FlexibleLength=attri14_id)

    attri15_id = request.GET.get('attri15', "")
    if attri15_id:
        all_techch = all_techch.filter(UserParticipation=attri15_id)

    attri16_id = request.GET.get('attri16', "")
    if attri16_id:
        all_techch = all_techch.filter(InformationOrganization=attri16_id)

    attri17_id = request.GET.get('attri17', "")
    if attri17_id:
        all_techch = all_techch.filter(FeedbackOffline=attri17_id)

    attri18_id = request.GET.get('attri18', "")
    if attri18_id:
        all_techch = all_techch.filter(LongDuration=attri18_id)

    attri19_id = request.GET.get('attri19', "")
    if attri19_id:
        all_techch = all_techch.filter(UserResearch=attri19_id)

    attri20_id = request.GET.get('attri20', "")
    if attri20_id:
        all_techch = all_techch.filter(RelationshipDependency=attri20_id)

    attri21_id = request.GET.get('attri21', "")
    if attri21_id:
        all_techch = all_techch.filter(UserSimulation=attri21_id)

    attri22_id = request.GET.get('attri22', "")
    if attri22_id:
        all_techch = all_techch.filter(ExpertParticipation=attri22_id)

    attri23_id = request.GET.get('attri23', "")
    if attri23_id:
        all_techch = all_techch.filter(UXEvaluation=attri23_id)

    attri24_id = request.GET.get('attri24', "")
    if attri24_id:
        all_techch = all_techch.filter(FeedbackCollection=attri24_id)

    return render(request, 'HTML/DE/Tag Cloud/Tag Cloud 3.html',
                  {"all_techch": all_techch, "taskdes": taskdes, "attribut1": attribut1, })


# 添加选中技术，并跳转到post-question 3页面
def C_AddTech3DE(request):
    selected1 = request.POST.get('selectedone',"")
    selected2 = request.POST.get('selectedtwo',"")
    selected3 = request.POST.get('selectedthree',"")
    user_id = request.user.id
    mode = request.user.id % 4
    taskdes_all = TaskDescriptionDE.objects.all()
    taskdes = taskdes_all.filter(id=3)
    SelectedTechniqueOne.objects.create(mode_id=mode,chose_Tech1=selected1,chose_Tech2=selected2, chose_Tech3=selected3,Test_User_id=user_id )
    return render(request, 'HTML/DE/post-test Q3.html',{
        "taskdes":taskdes,
    })









class CustomBackend(ModelBackend):
    def authenticate(self, username=None, password=None, **kwargs):
        try:
            user = UserProfile.objects.get(username=username)
            return user
        except Exception as e:
            return None

