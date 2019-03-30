# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Article
from .models import Category
from .models import Tag
from .models import Comment

from feiyu.admin import admin_site

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','user', 'isPub','commentNum','readNum','update_time')
    fieldsets = [(u'标题', {'fields': ['title']}),(u'内容', {'fields': ['content']}),(u'作者', {'fields': ['user','category','tag']}), (u'创建时间', {'fields': ['isPub','commentNum','readNum','create_time']}), ]
    # list_filter = ['pub_date']

    search_fields = ['question_text']


admin_site.register(Article,ArticleAdmin)
admin_site.register(Category)
admin_site.register(Tag)
admin_site.register(Comment)
