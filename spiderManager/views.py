# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.
from spiderManager import manager
from . import tool


def index(request):
    # 爬取cocoachina iOS最新文章
    res = [{'type':'find','result':'list',
            're':{'name':'div','class':'leftSide'}},
           {'type':'findall','result':'li',
            're':{'name':'li','attrs':[{'type':'result','content':'title','nametypes':['a'],'attr':'string'},
                                       {'type':'result','content':'url','nametypes':['a'],'attr':'href'},
                                       {'type':'result','content':'imgurl','nametypes':['img'],'attr':'src'},
                                       # {'type':'findall','result':'span',
                                       #  're':{'name':'span','attrs':[{'content':'time','nametypes':['span'],'attr':'string'}]}}

                                       ]}}]
    manager.spiderWithUrl('http://www.cocoachina.com/ios/list_69_1.html',res)

#爬取cocoachina navi
    # res = [{'type': 'find', 'result': 'nav-list', 're': {'name': 'div', 'class': 'nav-list'}},
    #        {'type': 'findall', 'result': 'li', 're': {'name': 'li', 'attrs': [
    #            {'content': 'title', 'nametypes': ['a'], 'attr': 'string'},
    #            {'content': 'url', 'nametypes': ['a'], 'attr': 'href'}]}}]
    # manager.spiderWithUrl('http://www.cocoachina.com/news/index.php', res)

    return HttpResponse(u"欢迎访问spiderManager")


def spiderNavi(request):
    navis = manager.spiderZHYSNavis()
    print(navis)
    return HttpResponse(navis)

    # return open(r'../files/zhysNavis.json').read()

def spiderCocochinaHome(request):
    homeD = manager.spiderCocoaChinaHomeData()

    response = HttpResponse(homeD)
    response['Access-Control-Allow-Origin'] = '*'  # 允许的跨域名
    response['Access-Control-Allow-Headers'] = 'h1'  # 允许的请求头
    # response['Access-Control-Allow-Methods'] = 'PUT'   #允许的请求方法
    print(response)
    return response

def spiderCocochinaIosList(request):
    homeD = manager.spiderCocoaChinaIosListData()

    response = HttpResponse(homeD)
    response['Access-Control-Allow-Origin'] = '*'  # 允许的跨域名
    response['Access-Control-Allow-Headers'] = 'h1'  # 允许的请求头
    # response['Access-Control-Allow-Methods'] = 'PUT'   #允许的请求方法
    print(response)
    return response

def spiderZhysItems(request):

    navis = manager.spiderZHYSContentItem('http://www.cnys.com/ertong/77714.html')

    return HttpResponse(navis)


def spiderZhysHome(request):

    return HttpResponse(manager.spiderZHYSHomeInfo('http://www.zhys.com/'))