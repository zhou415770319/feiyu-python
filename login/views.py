# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import hashlib

from django.shortcuts import render, redirect
from . import models
from . import forms
from blog import models as blogmodles
from django.views.decorators.csrf import csrf_exempt
import time
import os
from django.conf import settings
from django.http import JsonResponse

# Create your views here.
# @csrf_exempt
def login(request):
    if request.session.get('is_login',None):
        return redirect("/index/")
    if request.method == "POST":
        login_form = forms.UserForm(request.POST)

        # print(username,password)
        message = "请检查填写的内容！"

        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            # username = request.POST.get('username', None)
            # password = request.POST.get('password', None)
            try:
                user = models.User.objects.get(name=username)
                if user.password == hash_code(password):
                    request.session['is_login'] = True
                    request.session['user_id'] = user.id
                    request.session['user_name'] = user.name
                    return redirect('/index/')
                else:
                    message = "密码不正确！"
            except:
                message = "用户名不存在"

        return render(request, 'login/login.html',locals())
    login_form = forms.UserForm()

    return render(request,'login/login.html',locals())


def register(request):
    if request.session.get('is_login', None):
        # 登录状态不允许注册。你可以修改这条原则！
        return redirect("/index/")
    print(request.method)
    if request.method == "POST":
        register_form = forms.RegisterForm(request.POST)
        message = "请检查填写的内容！"
        if register_form.is_valid():  # 获取数据
            print('获取数据')

            username = request.POST.get('username', None)
            password1 = request.POST.get('password1', None)
            password2 = request.POST.get('password2', None)
            email = request.POST.get('email', None)
            sex = request.POST.get('sex', None)

            print(username,password1)
            # username = register_form.cleaned_data['username']
            # password1 = register_form.cleaned_data['password1']
            # password2 = register_form.cleaned_data['password2']
            # email = register_form.cleaned_data['email']
            # sex = register_form.cleaned_data['sex']
            if password1 != password2:  # 判断两次密码是否相同
                message = "两次输入的密码不同！"
                return render(request, 'login/register.html', locals())
            else:
                same_name_user = models.User.objects.filter(name=username)
                if same_name_user:  # 用户名唯一
                    message = '用户已经存在，请重新选择用户名！'
                    return render(request, 'login/register.html', locals())
                same_email_user = models.User.objects.filter(email=email)
                if same_email_user:  # 邮箱地址唯一
                    message = '该邮箱地址已被注册，请使用别的邮箱！'
                    return render(request, 'login/register.html', locals())

                # 当一切都OK的情况下，创建新用户

                new_user = models.User.objects.create()
                new_user.name = username
                new_user.password = hash_code(password1)
                new_user.email = email
                new_user.sex = sex
                new_user.save()
                return redirect('/login/')  # 自动跳转到登录页面
    register_form = forms.RegisterForm()
    return render(request, 'login/register.html', locals())


def logout(request):
    if not request.session.get('is_login',None):
        redirect("/index/")
    request.session.flush()

    return redirect("/index/")


def index(request):
    articles = blogmodles.Article.objects.order_by("-create_time")
    print('articles+++++'+str(articles))
    return render(request,'login/index.html',{'articles':articles})


def hash_code(s,salt='mysite'):
    h = hashlib.sha256()
    s += salt
    h.update(s.encode())
    return h.hexdigest()


@csrf_exempt
def upload(request):
    upload_file = request.FILES['imagefile']
    if request.method == 'POST' and upload_file:
        success, message = 0, '上传失败'

        # 本地创建保存图片的文件夹
        path = settings.STATIC_URL + 'uploads/' + time.strftime('%Y%m%d') + '/'
        if not os.path.exists(settings.BASE_DIR + path):
            os.makedirs(settings.BASE_DIR + path)

        # 拼装本地保存图片的完整文件名
        filename = time.strftime('%H%M%S') + '_' + upload_file.name
        local_file = settings.BASE_DIR + path + filename

        # 写入文件
        with open(local_file, 'wb+') as f:
            for chunk in upload_file.chunks():
                f.write(chunk)

            success, message = 1, '上传成功'

        # 返回格式
        data = {
            'success': success,
            'message': message,
            'url': path + filename
        }

        return JsonResponse(data)
    else:
        return JsonResponse({'state': 0, 'message': 'Not support method or Can not get file'})

