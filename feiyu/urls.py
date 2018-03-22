# -*- coding: utf-8 -*-

"""feiyu URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include,url
from django.contrib import admin
from blog import views as blog_views
from spiderManager import views as spider_views
from demo import views as demo_views
from polls import admin as polls_admin
from polls import views as polls_views
urlpatterns = [
    #例子

    url(r'^$', demo_views.index, name="home"),

    url(r'^add/', demo_views.add, name= "add"),
    url(r'^add2/(\d+)/(\d+)/', demo_views.add2, name= "add2"),

    # polls
    url(r'^polls/', include('polls.urls')),

    #博客
    url(r'^blog/', blog_views.index),

    url(r'^admin/', polls_admin.admin_site.urls),

    #爬虫
    url(r'^api/',include('spiderManager.urls')),
]
