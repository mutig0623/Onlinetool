# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
import MySQLdb
from django.db import models
from django.contrib.auth.backends import ModelBackend
from users.models import *
from selected.models import *
from  classification.models import *
from  django.contrib.auth import authenticate,login



def home(request):
    return render(request, 'index.html', {})


#跳转到中文页面
def Chlink(request):
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
                "msg":"该用户名已被注册，请另换一个注册!"
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
            return render(request,'HTML/CH/pre-test.html')


# 添加pre question到数据库，并跳转到introduction.html
def PreAdd(request):
    if request.method == "POST":
        age = request.POST.get('age')
        sex = request.POST.get('sex')
        national = request.POST.get('national',"")
        edu = request.POST.get('edu')
        eduother = request.POST.get('eduother')
        knowledge = request.POST.getlist('knowledge')
        knowother = request.POST.get('knowother',"")
        role = request.POST.getlist('role')
        roleother = request.POST.get('roleother',"")
        years = request.POST.get('years',"0")
        pronu = request.POST.get('pronu')
        cours = request.POST.get('cours')
        tech = request.POST.get('tech')
        samtech = request.POST.getlist('samtech')
        que1 = request.POST.get('que1')
        que2 =request.POST.get('que2')
        que3 = request.POST.get('que3')
        que4 = request.POST.get('que40')
        que5 = request.POST.get('que5')
        que6 = request.POST.get('que6')
        que7 = request.POST.get('que7')
        que8 = request.POST.get('que8')
        que9 = request.POST.get('que9')
        que10 = request.POST.get('que10')
        que11 = request.POST.get('que11')
        que12 = request.POST.get('que12')
        que13 = request.POST.get('que13')
        que14 = request.POST.get('que14')
        que15 = request.POST.get('que15')
        que16 = request.POST.get('que16')
        que17 = request.POST.get('que17')
        que18 = request.POST.get('que18')
        que19 = request.POST.get('que19')
        que20 = request.POST.get('que20')
        que21 = request.POST.get('que21')
        user_id = request.user.id
        PreQuestionResult.objects.create(Q1_age=age,Q2_gender=sex,Q3_nationa=national,Q4_educationlevel=edu,Q41_educationlevel=eduother,Q5_expertise=knowledge,Q51_expertise=knowother,Q6_role=role,Q61_role= roleother,Q7_fulltime=years,Q8_ProjectCount=pronu,Q9_DesigCourse=cours, Q10_UsedTechnique=tech,Q11_FamiliarTechnique=samtech,Q12_knewpretty=que1,Q13_experts=que2,Q14_knewless=que3,Q15_donotknow=que4, Q16_donotfeel=que5,Q17_lotofexperiences=que6, Q18_familiar=que7,Q19_focusobjects=que8,Q20_basedcategories=que9,Q21_easylearncategories=que10,Q22_organizefunctionally=que11, Q23_useformallogic=que12,Q24_adherelogicalrules=que13,Q25_individualbehavior=que14,Q26_focussurobj=que15,Q27_focussurfeld=que16,Q28_difflearncate=que17, Q29_organthematically=que18,Q30_diareasoning=que19,Q31_preflogic=que20,Q32_peopbehav=que21,Test_User_id=user_id)
    return render(request, 'HTML/CH/introduction.html', { })


# 跳转到taskDetailone页面
def ChTask1(request):
    TaskDes = TaskDescriptionCH.objects.all()
    taskdes = TaskDes.filter(id=1)
    return render(request, 'HTML/CH/TaskDetail.html',{
        "taskdes":taskdes,
    } )


# 判断去哪个中文页面
def SwitchCH(request):
    user_id = request.user.id
    mode_id = user_id % 4
    # 跳转到Top-down页面
    if mode_id == 0:
        task_all= TaskDescriptionCH.objects.all()
        task = task_all.filter(id=1)
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
                        "evaluationn_id": evaluation_id,"task":task,
                       })
    # 跳转到Bottom-up页面
    elif mode_id == 1:
        task_all = TaskDescriptionCH.objects.all()
        task = task_all.filter(id=1)
        all_techch = TechinforCH.objects.all()
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
        all_techch = TechinforCH.objects.all()
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
        tech = TechinforCH.objects.all()
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
    mode_id = request.user.id % 4
    SelectedTechniqueOne.objects.create(chose_Tech1=selected1,chose_Tech2=selected2, chose_Tech3=selected3,Test_User_id=user_id,mode_id= mode_id )
    return render(request, 'HTML/CH/Blank/post-test .html',{ })


# 添加Post-question1到数据库，并跳转到Task-Detail 2页面
def B_AddPost1(request):
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
        post17 = request.POST.get('post17')
        post18 = request.POST.get('post18')
        user_id = request.user.id
        mode = request.user.id % 4
        PostQuestionResultOne.objects.create(mode_id=mode,Test_User_id=user_id,Q1_proficiency=post1,Q2_globalapproach=post2,Q3_localizedapproach=post3,Q4_objects=post4,Q5_rulesbased=post5,Q6_learncategory=post6,Q7_organize=post7,Q8_formallogic=post8,Q9_logicalrules=post9,Q10_individual=post10,Q11_surrounding=post11,Q12_littelrule=post12,Q13_difficultrule=post13,Q14_thematically=post14,Q15_dialectical=post15,Q16_contradiction=post16,Q17_pressures=post17,Q18_thematically=post18, )
        TaskDes = TaskDescriptionCH.objects.all()
        taskdes = TaskDes.filter(id=2)
        return render(request, 'HTML/CH/Blank/TaskDetailtwo.html',{
            "taskdes":taskdes,
        })


# 跳转到blank2，显示tech信息等内容
def CH_blank2(request):
    tech = TechinforCH.objects.all()
    task_all=TaskDescriptionCH.objects.all()
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
    return render(request, 'HTML/CH/Blank/post-test 2.html',{
        "taskdes":taskdes,
    })


# 添加post-question2 答案到数据库，并跳转到TaskDetail 3页面
def B_AddPost2(request):
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
        post17 = request.POST.get('post17')
        post18 = request.POST.get('post18')
        user_id = request.user.id
        mode = request.user.id % 4
        PostQuestionResultOne.objects.create(mode_id=mode,Test_User_id=user_id,Q1_proficiency=post1,Q2_globalapproach=post2,Q3_localizedapproach=post3,Q4_objects=post4,Q5_rulesbased=post5,Q6_learncategory=post6,Q7_organize=post7,Q8_formallogic=post8,Q9_logicalrules=post9,Q10_individual=post10,Q11_surrounding=post11,Q12_littelrule=post12,Q13_difficultrule=post13,Q14_thematically=post14,Q15_dialectical=post15,Q16_contradiction=post16,Q17_pressures=post17,Q18_thematically=post18, )
        TaskDes = TaskDescriptionCH.objects.all()
        taskdes = TaskDes.filter(id=3)
        return render(request, 'HTML/CH/Blank/TaskDetailthree.html',{
            "taskdes":taskdes,
        })


# 跳转到blank3页面，并显示相关信息
def CH_blank3(request):
    tech = TechinforCH.objects.all()
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


# 添加post-question3 到数据库，并转到end页面
def AddPost3(request):
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
        post17 = request.POST.get('post17')
        post18 = request.POST.get('post18')
        post19 = request.POST.get('post19')
        post20 = request.POST.get('post20')
        post21 = request.POST.get('post21')
        post22 = request.POST.get('post22')
        post23 = request.POST.get('post23')
        post24 = request.POST.get('post24')
        post25 = request.POST.get('post25')
        user_id = request.user.id
        mode = request.user.id % 4
        PostQuestionResultTwo.objects.create(mode_id=mode,Test_User_id=user_id, Q1_proficiency=post1, Q2_globalapproach=post2,
                                             Q3_localizedapproach=post3, Q4_objects=post4, Q5_rulesbased=post5,
                                             Q6_learncategory=post6, Q7_organize=post7, Q8_formallogic=post8,
                                             Q9_logicalrules=post9, Q10_individual=post10, Q11_surrounding=post11,
                                             Q12_littelrule=post12, Q13_difficultrule=post13,
                                             Q14_thematically=post14, Q15_dialectical=post15,
                                             Q16_contradiction=post16, Q17_pressures=post17,
                                             Q18_thematically=post18,Q19_littelrule=post19,Q20_difficultrule=post20,Q21_thematically=post21,
                                             Q22_dialectical=post22,Q23_contradiction=post23,Q24_pressures=post24,Q25_thematically=post25,)
        TaskDes = TaskDescriptionCH.objects.all()
        taskdes = TaskDes.filter(id=3)
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
    return render(request, 'HTML/CH/Top-down/post-test.html',{
    })


# 添加Post-question1到数据库，并跳转到Task-Detail 2页面
def T_AddPost1(request):
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
        post17 = request.POST.get('post17')
        post18 = request.POST.get('post18')
        user_id = request.user.id
        mode = request.user.id % 4
        PostQuestionResultOne.objects.create(mode_id=mode,Test_User_id=user_id,Q1_proficiency=post1,Q2_globalapproach=post2,Q3_localizedapproach=post3,Q4_objects=post4,Q5_rulesbased=post5,Q6_learncategory=post6,Q7_organize=post7,Q8_formallogic=post8,Q9_logicalrules=post9,Q10_individual=post10,Q11_surrounding=post11,Q12_littelrule=post12,Q13_difficultrule=post13,Q14_thematically=post14,Q15_dialectical=post15,Q16_contradiction=post16,Q17_pressures=post17,Q18_thematically=post18, )
        TaskDes = TaskDescriptionCH.objects.all()
        taskdes = TaskDes.filter(id=2)
        return render(request, 'HTML/CH/Top-down/TaskDetailtwo.html',{
            "taskdes":taskdes,
        })


# 跳转到blank2，显示tech信息等内容
def CH_Top2(request):
    task_all = TaskDescriptionCH.objects.all()
    task = task_all.filter(id=1)
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
                   "evaluationn_id": evaluation_id, "task": task, })


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
    return render(request, 'HTML/CH/Top-down/post-test 2.html', {
        "taskdes":taskdes,
    })


# 添加post-question2 答案到数据库，并跳转到TaskDetail 3页面
def T_AddPost2(request):
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
        post17 = request.POST.get('post17')
        post18 = request.POST.get('post18')
        user_id = request.user.id
        mode = request.user.id % 4
        PostQuestionResultTwo.objects.create(mode_id=mode,Test_User_id=user_id,Q1_proficiency=post1,Q2_globalapproach=post2,Q3_localizedapproach=post3,Q4_objects=post4,Q5_rulesbased=post5,Q6_learncategory=post6,Q7_organize=post7,Q8_formallogic=post8,Q9_logicalrules=post9,Q10_individual=post10,Q11_surrounding=post11,Q12_littelrule=post12,Q13_difficultrule=post13,Q14_thematically=post14,Q15_dialectical=post15,Q16_contradiction=post16,Q17_pressures=post17,Q18_thematically=post18, )
        TaskDes = TaskDescriptionCH.objects.all()
        taskdes = TaskDes.filter(id=3)
        return render(request, 'HTML/CH/Top-down/TaskDetailthree.html',{
            "taskdes":taskdes,
        })


# 跳转到blank3页面，并显示相关信息
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
                   "evaluationn_id": evaluation_id, "taskdes": taskdes, })


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


# 添加post-question3 到数据库，并转到end页面
def AddPost3(request):
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
        post17 = request.POST.get('post17')
        post18 = request.POST.get('post18')
        post19 = request.POST.get('post19')
        post20 = request.POST.get('post20')
        post21 = request.POST.get('post21')
        post22 = request.POST.get('post22')
        post23 = request.POST.get('post23')
        post24 = request.POST.get('post24')
        post25 = request.POST.get('post25')
        user_id = request.user.id
        mode = request.user.id % 4
        PostQuestionResultThree.objects.create(mode_id=mode,Test_User_id=user_id, Q1_proficiency=post1, Q2_globalapproach=post2,
                                             Q3_localizedapproach=post3, Q4_objects=post4, Q5_rulesbased=post5,
                                             Q6_learncategory=post6, Q7_organize=post7, Q8_formallogic=post8,
                                             Q9_logicalrules=post9, Q10_individual=post10, Q11_surrounding=post11,
                                             Q12_littelrule=post12, Q13_difficultrule=post13,
                                             Q14_thematically=post14, Q15_dialectical=post15,
                                             Q16_contradiction=post16, Q17_pressures=post17,
                                             Q18_thematically=post18,Q19_littelrule=post19,Q20_difficultrule=post20,Q21_thematically=post21,
                                             Q22_dialectical=post22,Q23_contradiction=post23,Q24_pressures=post24,Q25_thematically=post25,)
    return render(request,'HTML/CH/end.html',{})







# 如果选择了Bottom-up
# 添加选择的tech，并跳转到Post-question 1页面
def U_AddTech1(request):
    selected1 = request.POST.get('selectedone',"")
    selected2 = request.POST.get('selectedtwo',"")
    selected3 = request.POST.get('selectedthree',"")
    user_id = request.user.id
    mode = request.user.id % 4
    SelectedTechniqueOne.objects.create(mode_id=mode,chose_Tech1=selected1,chose_Tech2=selected2, chose_Tech3=selected3,Test_User_id=user_id )
    return render(request, 'HTML/CH/Bottom-up/post-test.html',{
    })


# 添加Post-question1到数据库，并跳转到Task-Detail 2页面
def U_AddPost1(request):
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
        post17 = request.POST.get('post17')
        post18 = request.POST.get('post18')
        user_id = request.user.id
        mode = request.user.id % 4
        PostQuestionResultOne.objects.create(mode_id=mode,Test_User_id=user_id,Q1_proficiency=post1,Q2_globalapproach=post2,Q3_localizedapproach=post3,Q4_objects=post4,Q5_rulesbased=post5,Q6_learncategory=post6,Q7_organize=post7,Q8_formallogic=post8,Q9_logicalrules=post9,Q10_individual=post10,Q11_surrounding=post11,Q12_littelrule=post12,Q13_difficultrule=post13,Q14_thematically=post14,Q15_dialectical=post15,Q16_contradiction=post16,Q17_pressures=post17,Q18_thematically=post18, )
        TaskDes = TaskDescriptionCH.objects.all()
        taskdes = TaskDes.filter(id=2)
        return render(request, 'HTML/CH/Bottom-up/TaskDetailtwo.html',{
            "taskdes":taskdes,
        })



# 跳转到blank2，显示tech信息等内容
def CH_Up2(request):
    tech = TechinforCH.objects.all()
    task_all=TaskDescriptionCH.objects.all()
    task=task_all.filter(id=2)
    return render(request, 'HTML/CH/Bottom-up/blank2.html', {
        "tech": tech,
        "task":task,
        "de":de,
    })


# 添加选择技术到数据库，并跳转到post-question2页面
def U_AddTech2(request):
    selected1 = request.POST.get('selectedone',"")
    selected2 = request.POST.get('selectedtwo',"")
    selected3 = request.POST.get('selectedthree',"")
    user_id = request.user.id
    mode = request.user.id % 4
    taskdes_all = TaskDescriptionCH.objects.all()
    taskdes = taskdes_all.filter(id=2)
    SelectedTechniqueOne.objects.create(mode_id=mode,chose_Tech1=selected1,chose_Tech2=selected2, chose_Tech3=selected3,Test_User_id=user_id )
    return render(request, 'HTML/CH/Bottom-up/post-test 2.html',{
        "taskdes":taskdes,
    })


# 添加post-question2 答案到数据库，并跳转到TaskDetail 3页面
def U_AddPost2(request):
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
        post17 = request.POST.get('post17')
        post18 = request.POST.get('post18')
        user_id = request.user.id
        mode = request.user.id % 4
        PostQuestionResultOne.objects.create(mode_id=mode,Test_User_id=user_id,Q1_proficiency=post1,Q2_globalapproach=post2,Q3_localizedapproach=post3,Q4_objects=post4,Q5_rulesbased=post5,Q6_learncategory=post6,Q7_organize=post7,Q8_formallogic=post8,Q9_logicalrules=post9,Q10_individual=post10,Q11_surrounding=post11,Q12_littelrule=post12,Q13_difficultrule=post13,Q14_thematically=post14,Q15_dialectical=post15,Q16_contradiction=post16,Q17_pressures=post17,Q18_thematically=post18, )
        TaskDes = TaskDescriptionCH.objects.all()
        taskdes = TaskDes.filter(id=3)
        return render(request, 'HTML/CH/Bottom-up/TaskDetailthree.html',{
            "taskdes":taskdes,
        })


# 跳转到blank3页面，并显示相关信息
def CH_Up3(request):
    tech = TechinforCH.objects.all()
    task_all=TaskDescriptionCH.objects.all()
    task=task_all.filter(id=3)
    return render(request, 'HTML/CH/Bottom-up/blank3.html', {
        "tech": tech,
        "task":task,
    })


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
# 添加选择的tech，并跳转到Post-question 1页面
def C_AddTech1(request):
    selected1 = request.POST.get('selectedone',"")
    selected2 = request.POST.get('selectedtwo',"")
    selected3 = request.POST.get('selectedthree',"")
    user_id = request.user.id
    mode = request.user.id % 4
    SelectedTechniqueOne.objects.create(mode_id=mode,chose_Tech1=selected1,chose_Tech2=selected2, chose_Tech3=selected3,Test_User_id=user_id )
    return render(request, 'HTML/CH/Tag-Cloud/post-test.html',{
    })


# 添加Post-question1到数据库，并跳转到Task-Detail 2页面
def C_AddPost1(request):
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
        post17 = request.POST.get('post17')
        post18 = request.POST.get('post18')
        user_id = request.user.id
        mode = request.user.id % 4
        PostQuestionResultOne.objects.create(mode_id=mode,Test_User_id=user_id,Q1_proficiency=post1,Q2_globalapproach=post2,Q3_localizedapproach=post3,Q4_objects=post4,Q5_rulesbased=post5,Q6_learncategory=post6,Q7_organize=post7,Q8_formallogic=post8,Q9_logicalrules=post9,Q10_individual=post10,Q11_surrounding=post11,Q12_littelrule=post12,Q13_difficultrule=post13,Q14_thematically=post14,Q15_dialectical=post15,Q16_contradiction=post16,Q17_pressures=post17,Q18_thematically=post18, )
        TaskDes = TaskDescriptionCH.objects.all()
        taskdes = TaskDes.filter(id=2)
        return render(request, 'HTML/CH/Tag-Cloud/TaskDetailtwo.html',{
            "taskdes":taskdes,
        })


# 跳转到blank2，显示tech信息等内容
def CH_C2(request):
    all_techch = TechinforCH.objects.all()
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
    return render(request, 'HTML/CH/Tag-Cloud/post-test 2.html', {
        "taskdes":taskdes,
    })


# 添加post-question2 答案到数据库，并跳转到TaskDetail 3页面
def C_AddPost2(request):
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
        post17 = request.POST.get('post17')
        post18 = request.POST.get('post18')
        user_id = request.user.id
        mode = request.user.id % 4
        PostQuestionResultOne.objects.create(mode_id=mode,Test_User_id=user_id,Q1_proficiency=post1,Q2_globalapproach=post2,Q3_localizedapproach=post3,Q4_objects=post4,Q5_rulesbased=post5,Q6_learncategory=post6,Q7_organize=post7,Q8_formallogic=post8,Q9_logicalrules=post9,Q10_individual=post10,Q11_surrounding=post11,Q12_littelrule=post12,Q13_difficultrule=post13,Q14_thematically=post14,Q15_dialectical=post15,Q16_contradiction=post16,Q17_pressures=post17,Q18_thematically=post18, )
        TaskDes = TaskDescriptionCH.objects.all()
        taskdes = TaskDes.filter(id=3)
        return render(request, 'HTML/CH/Tag-Cloud/TaskDetailthree.html',{
            "taskdes":taskdes,
        })


# 跳转到blank3页面，并显示相关信息
def CH_C3(request):
    all_techch = TechinforCH.objects.all()
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







def TdEN(request):
    all_techen = TechinforEN.objects.all()
    attribut1 = TDDesignEN.objects.all()
    attribut2 = TDDependencyEN.objects.all()
    attribut3 = TDDurationEN.objects.all()
    attribut4 = TDParticipationEN.objects.all()
    attribut5 = TDEvaluationEN.objects.all()

    de_id = request.GET.get('de', "")
    if de_id:
        all_techen = all_techen.filter(TDDesign_id=int(de_id))

    td_id = request.GET.get('td', "")
    if td_id:
        all_techen = all_techen.filter(TDDependency_id=int(td_id))

    du_id = request.GET.get('du', "")
    if du_id:
        all_techen = all_techen.filter(TDDuration_id=int(du_id))

    pa_id = request.GET.get('pa', "")
    if pa_id:
        all_techen = all_techen.filter(TDParticipation_id=int(pa_id))

    ev_id = request.GET.get('ev', "")
    if ev_id:
        all_techen = all_techen.filter(TDEvaluation_id=int(ev_id))

    return render(request, 'HTML/EN/Top-down1.html', {
            "all_techen":all_techen,
            "attribut1": attribut1,
            "attribut2": attribut2,
            "attribut3": attribut3,
            "attribut4": attribut4,
            "attribut5": attribut5,
            "de_id":de_id,
            "td_id":td_id,
            "du_id":du_id,
            "pa_id":pa_id,
            "ev_id":ev_id,})


def BpEN(request):
    all_techen = TechinforEN.objects.all()
    attribut1 = BUDesignEN.objects.all()
    attribut2 = BUCollectionEN.objects.all()
    attribut3 = BUDurationEN.objects.all()
    attribut4 = BUParticipantEN.objects.all()

    de_id = request.GET.get('de', "")
    if de_id:
        all_techen = all_techen.filter(BUDesign_id=int(de_id))

    col_id = request.GET.get('col', "")
    if col_id:
        all_techen = all_techen.filter(BUCollection_id=int(col_id))

    du_id = request.GET.get('du', "")
    if du_id:
        all_techen = all_techen.filter(BUCollection_id=int(du_id))

    pa_id = request.GET.get('pa', "")
    if pa_id:
        all_techen = all_techen.filter(BUParticipant_id=int(pa_id))
    return render(request, 'HTML/EN/Bottom-up1.html', {
        "all_techen":all_techen,
        "attribut1":attribut1,
        "attribut2":attribut2,
        "attribut3":attribut3,
        "attribut4":attribut4,
        "de_id":de_id,
        "col_id": col_id,
        "du_id": du_id,
        "pa_id": pa_id,
    })

def CdEN(request):
    all_techch = TechinforEN.objects.all()
    attribut1 = TagCloudEN.objects.all()

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

    return render(request, 'HTML/EN/Tag Cloud1.html', {
            "all_techch": all_techch,
            "attribut1": attribut1,
            "attri1_id": attri1_id,
            "attri2_id": attri2_id,
            "attri3_id": attri3_id,
            "attri4_id": attri4_id,
            "attri5_id": attri5_id,
            "attri6_id": attri6_id,
             "attri7_id": attri7_id,
            "attri8_id": attri8_id,
            "attri9_id": attri9_id,
            "attri10_id": attri10_id,
            "attri11_id": attri11_id,
            "attri12_id": attri12_id,
            "attri13_id": attri13_id,
            "attri14_id": attri14_id,
            "attri15_id": attri15_id,
            "attri16_id": attri16_id,
            "attri17_id": attri17_id,
            "attri18_id": attri18_id,
            "attri19_id": attri19_id,
            "attri20_id": attri20_id,
            "attri21_id": attri21_id,
            "attri22_id": attri22_id,
            "attri23_id": attri23_id,
            "attri24_id": attri24_id,
    })

def PreQEN(request):
    question = PreQuestionEN.objects.all()

    return render(request,'HTML/EN/pre-test.html',{
        "question":question,
    })

def PostQCH(request):
    question = PostQuestionCH.objects.all()
    return render(request,'HTML/CH/post-test Q1.html',{
        "question":question,
    })

def PostPlusCH(request):
    question = PostQuestionCH.objects.all()
    question1 = PostQuestionPlusCH.objects.all()

    return render(request,'HTML/CH/post-test Q3.html',{
        "question":question,
        "question1":question1,
    })

def BlankEN(request):
    teches = TechinforEN.objects.all()
    return render(request, 'HTML/EN/blank1.html', {
        "teches":teches,
    })





def Enlink(request):
    return  render(request,'HTML/EN/Instruction.html',{})

def Delink(request):
    return  render(request,'HTML/DE/Instruction.html',{})

def LogEn(request):
    return render(request,'HTML/EN/login.html',{})

def LogDe(request):
    return render(request,'HTML/DE/login.html',{})






class CustomBackend(ModelBackend):
    def authenticate(self, username=None, password=None, **kwargs):
        try:
            user = UserProfile.objects.get(username=username)
            return user
        except Exception as e:
            return None

