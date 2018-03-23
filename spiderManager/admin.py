# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin


# Register your models here.
from feiyu.admin import admin_site
from spiderManager.models import ZhysHomeInfo


class ZhysHomeInfoAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'img', 'create_time')
    fieldsets = [(u'问题', {'fields': ['title']}),
                 ('', {'fields': ['url']}),
                 ('', {'fields': ['img']}),
                 (u'时间信息', {'fields': ['create_time'], 'classes': ['collapse']}), ]
    # inlines = [ChoiceInline]
    list_filter = ['create_time']
    #
    # search_fields = ['title']

    # fields = ['title','title']

admin_site.index_title = ''
admin_site.register(ZhysHomeInfo, ZhysHomeInfoAdmin)