# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.
from spiderManager import manager


def index(request):
    return HttpResponse(u"欢迎访问spiderManager")


def spiderNavi(request):
    navis = manager.spiderZHYSNavis()

    return HttpResponse(navis)

    # return open(r'../files/zhysNavis.json').read()

def spiderCocochinaHome(request):
    homeD = manager.spiderCocoaChinaHomeData()

    return HttpResponse(homeD)