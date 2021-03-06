# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from feiyu.admin import admin_site
# Register your models here.
from .models import Question,Choice


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):

    list_display = ('question_text', 'pub_date', 'was_published_recently')
    fieldsets = [
        (u'问题',      {'fields':['question_text']}),
        (u'时间信息',{'fields':['pub_date'],'classes':['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_filter = ['pub_date']

    search_fields = ['question_text']

    # fields = ['pub_date','question_text']

admin_site.register(Question,QuestionAdmin)
# admin.site.register(Choice)
