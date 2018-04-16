# -*- coding: utf-8 -*-

from django.contrib import admin


# Register your models here.
from feiyu.admin import admin_site
from spiderManager.models import ZhysHomeInfo, ZhysArticleInfo

class ScrollImagesInline(admin.TabularInline):
    model = ZhysArticleInfo
    extra = 3

class ZhysHomeInfoAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'img', 'create_time')
    fieldsets = [(u'问题', {'fields': ['title']}),
                 ('', {'fields': ['url']}),
                 ('', {'fields': ['img']}),
                 (u'时间信息', {'fields': ['create_time'], 'classes': ['collapse']}), ]
    inlines = [ScrollImagesInline]
    list_filter = ['create_time']
    #
    # search_fields = ['title']

    # fields = ['title','title']

class ZhysArticleInfoAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'img', 'create_time')
    fieldsets = [(u'问题', {'fields': ['title']}),
                 ('', {'fields': ['url']}),
                 ('', {'fields': ['img']}),
                 (u'时间信息', {'fields': ['create_time'], 'classes': ['collapse']}), ]
    # inlines = [ChoiceInline]
    list_filter = ['create_time']

admin_site.register(ZhysHomeInfo, ZhysHomeInfoAdmin)
admin_site.register(ZhysArticleInfo, ZhysArticleInfoAdmin)

