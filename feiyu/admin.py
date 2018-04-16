# -*- coding: utf-8 -*-

from django.contrib import admin
# from users import users

class AdminSite(admin.AdminSite):
    # site_header = u'飞羽的管理后台'
    index_title = ''


admin_site = AdminSite()
# admin_site.register(users,user)
