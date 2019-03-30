# -*- coding: utf-8 -*-
from django.conf.urls import url

from spiderManager import views

urlpatterns = [
    url(r'^$',views.index,name="spider_home"),
#中华养生网  获取导航信息
    url(r'^zhys/navi/',views.spiderNavi,name="spider_navi"),
#中华养生网  首页信息

    url(r'^zhys/home/', views.spiderZhysHome, name="spider_zhys_item"),

#中华养生网  分类列表
    url(r'^zhys/items/', views.spiderZhysItems, name="spider_zhys_item"),

    url(r'^cocoachina/home', views.spiderCocochinaHome, name="spider_cocoachina_home"),
    url(r'^cocoachina/ioslist', views.spiderCocochinaIosList, name="spider_cocoachina_ioslist"),

]
