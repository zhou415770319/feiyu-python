# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

class AdminSite(admin.AdminSite):
    site_header = u'飞羽的管理后台'
    index_title = ''

admin_site = AdminSite()

