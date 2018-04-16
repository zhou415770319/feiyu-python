# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from . import models
from . import forms
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
@csrf_exempt
def login(request):
    if request.method == "POST":
        login_form = forms.UserForm(request.POST)

        # print(username,password)
        message = "请检查填写的内容！"

        if login_form.is_valid():
            username = request.POST.get('username', None)
            password = request.POST.get('password', None)
            try:
                user = models.User.objects.get(name=username)
                if user.password == password:
                    return redirect('/index/')
                else:
                    message = "密码不正确！"
            except:
                message = "用户名不存在"

        return render(request, 'login/login.html',locals())
    login_form = forms.UserForm()

    return render(request,'login/login.html',locals())


def register(request):
    return render(request,'login/register.html')


def logout(request):
    return render(request,'base.html')


def index(request):
    return render(request,'login/index.html')
