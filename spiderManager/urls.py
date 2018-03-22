# -*- coding: utf-8 -*-
from django.conf.urls import url

from spiderManager import views

urlpatterns = [
    url(r'^$',views.index,name="spider_home"),

    url(r'^zhys/navi/',views.spiderNavi,name="spider_navi"),

    url(r'^cocoachina/home', views.spiderCocochinaHome, name="spider_cocoachina_home"),

]
