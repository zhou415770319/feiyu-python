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
from django.conf.urls.static import static
from django.conf import settings

from django.contrib import admin
from blog import views as blog_views
from spiderManager import views as spider_views
from demo import views as demo_views
from polls import admin as polls_admin
from polls import views as polls_views
from login import views as login_views

urlpatterns = [

    #markdown编辑器

    url(r'mdeditor/', include('mdeditor.urls')),
    # markdown编辑器 上传图片

    url(r'api/upload/', login_views.upload, name='api-upload-url'),
    #例子
    url(r'^$', demo_views.index, name="home"),

    # url(r'^add/', demo_views.add, name= "add"),
    # url(r'^add2/(\d+)/(\d+)/', demo_views.add2, name= "add2"),

    # polls
    url(r'^polls/', include('polls.urls')),

    #博客
    url(r'^blog/getbloglist', blog_views.getbloglist),
    url(r'^blog/articleDetails/article_(?P<id>[\d]+)$', blog_views.article_details),

    url(r'^admin/', polls_admin.admin_site.urls),

    #爬虫
    url(r'^api/',include('spiderManager.urls')),

    # 登录注册
    url(r'^index/', login_views.index, name="index"),

    url(r'^login/', login_views.login, name="login"),

    url(r'^register/', login_views.register, name="register"),

    url(r'^logout/', login_views.logout, name="logout"),

    # url(r'^captcha', include('captcha.urls')),  # 增加这一行
    #
    # url(r'^api-auth/', include('rest_framework.urls'))

]
if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)