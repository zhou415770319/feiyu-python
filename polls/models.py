# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import datetime
from django.utils import timezone

# Create your models here.

class Question(models.Model):
    question_text = models.CharField('问题',max_length=200)
    pub_date = models.DateTimeField('创建时间')
    # update_time = models.DateTimeField('更新时间')

    def was_published_recently(self):
        return self.pub_date <= timezone.now()
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = '是否发布'


    # def question_text(self):
    #     return models.CharField(max_length=200)
    # question_text.short_description = '问题'
    def __str__(self):

        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField('选项',max_length=200)
    votes = models.IntegerField('投票数',default=0)

    def __str__(self):
        return self.choice_text