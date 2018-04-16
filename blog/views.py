# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse
import json
# Create your views here.

def getbloglist(request):
    tem = [{"title":"sjjjjx","img":"https://"},{"title":"sssdsfff","img":"https://"}]
    json.dumps(tem)
    return HttpResponse(tem)