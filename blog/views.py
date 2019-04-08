# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.forms.models import model_to_dict
from django.http import JsonResponse
from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse
import json

import json
import datetime

from .models import Article
# Create your views here.

def getbloglist(request):
    # tem = [{"title":"zhoufei","des":"kkksknnxmmallld","img":"http://pic30.photophoto.cn/20140211/0008020212116323_b.jpg"}
    #     ,{"title":"sssdsfff","des":"jkklllsmx","img":"http://pic30.photophoto.cn/20140211/0008020212116323_b.jpg"}
    #     ,{"title": "sssdsfff", "des": "jkklllsmx",
    #         "img": "http://pic30.photophoto.cn/20140211/0008020212116323_b.jpg"}
    #     ,{"title": "sssdsfff", "des": "jkklllsmx",
    #         "img": "http://pic30.photophoto.cn/20140211/0008020212116323_b.jpg"}
    #
    #        ]

    blogList = Article.objects.all().first()
    # tem = serializers.serialize('json',blogList)
    tem = model_to_dict(blogList)

    result = {"data":tem}

    print(tem)

    result = addCode(result,True)

    response = HttpResponse(json.dumps(result))
    response['Access-Control-Allow-Origin'] = '*'  # 允许的跨域名
    response['Access-Control-Allow-Headers'] = 'h1'  # 允许的请求头
    # response['Access-Control-Allow-Methods'] = 'PUT'   #允许的请求方法
    return response


def article_details(request,id):
    article = Article.objects.get(id=id)
    print(id)

    return render(request,'login/articledetail.html',{'article':article})

def addCode(result,isSuccusess):
    if isSuccusess:
        result['code'] = 200
        result['codemsg'] = "请求成功！"
    else:
        result['code'] = 404
        result['codemsg'] = "请求失败！"
    return result


class DateEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, datetime.datetime):
            return obj.strftime("%Y-%m-%d")
        else:
            return json.JSONEncoder.default(self, obj)