from django.conf.urls import url,include
from django.views.generic import View

from .views import LoginChView
from . import views

urlpatterns = [
        url('^$', views.home),
        url('^CH/overview$', views.Chlink,name='Chlink'),
        url('^CH/log$', views.LogCh, name='LogCh'),
        url('^CH/pre$', LoginChView.as_view(), name='LoginCh'),
        url('^CH/intro$', views.PreAdd, name='PreAdd'),
        url('^CH/t1$', views.ChTask1, name='ChTask1'),
        url('^CH/ch$', views.SwitchCH, name='SwitchCH'),


        url('^CH/B/add1$', views.B_AddTech1, name='B_Addtech1'),
        url('^CH/B/post1$', views.B_AddPost1, name='B_Addpost1'),
        url('^CH/B/2$', views.CH_blank2, name='B_2'),
        url('^CH/B/add2$', views.B_AddTech2, name='B_Addtech2'),
        url('^CH/B/post2$', views.B_AddPost2, name='B_Addpost2'),
        url('^CH/B/3$', views.CH_blank3, name='B_3'),
        url('^CH/B/add3$', views.B_AddTech3, name='B_Addtech3'),
        url('^CH/B/post3$', views.AddPost3, name='Addpost3'),


        url('^CH/T/add1$', views.T_AddTech1, name='T_Addtech1'),
        url('^CH/T/post1$', views.T_AddPost1, name='T_Addpost1'),
        url('^CH/T/2$', views.CH_Top2, name='T_2'),
        url('^CH/T/add2$', views.T_AddTech2, name='T_Addtech2'),
        url('^CH/T/post2$', views.T_AddPost2, name='T_Addpost2'),
        url('^CH/T/3$', views.CH_Top3, name='T_3'),
        url('^CH/T/add3$', views.T_AddTech3, name='T_Addtech3'),
        url('^CH/T/post3$', views.AddPost3, name='Addpost3'),


        url('^CH/U/add1$', views.U_AddTech1, name='U_Addtech1'),
        url('^CH/U/post1$', views.U_AddPost1, name='U_Addpost1'),
        url('^CH/U/2$', views.CH_Up2, name='U_2'),
        url('^CH/U/add2$', views.U_AddTech2, name='U_Addtech2'),
        url('^CH/U/post2$', views.U_AddPost2, name='U_Addpost2'),
        url('^CH/U/3$', views.CH_Up3, name='U_3'),
        url('^CH/U/add3$', views.T_AddTech3, name='U_Addtech3'),
        url('^CH/U/post3$', views.AddPost3, name='Addpost3'),


        url('^CH/C/add1$', views.C_AddTech1, name='C_Addtech1'),
        url('^CH/C/post1$', views.C_AddPost1, name='C_Addpost1'),
        url('^CH/C/2$', views.CH_C2, name='C_2'),
        url('^CH/C/add2$', views.C_AddTech2, name='C_Addtech2'),
        url('^CH/C/post2$', views.C_AddPost2, name='C_Addpost2'),
        url('^CH/C/3$', views.CH_C3, name='C_3'),
        url('^CH/C/add3$', views.C_AddTech3, name='C_Addtech3'),
        url('^CH/C/post3$', views.AddPost3, name='Addpost3'),









        url('^EN$', views.Enlink,name='Enlink'),
        url('^DE$', views.Delink,name='Delink'),
        url('^EN/log$', views.LogEn, name='LogEn'),
        url('^DE/log$', views.LogDe, name='LogDe'),


        url('^EN/td$', views.TdEN),

        url('^EN/bp$', views.BpEN),

        url('^EN/cd$', views.CdEN),

        url('^EN/pre$', views.PreQEN),

        url('^3cp$', views.PostPlusCH),

        url('^EN/blank$', views.BlankEN,),



        ]