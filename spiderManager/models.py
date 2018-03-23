# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
maxCharLength = 200

class ZhysHomeInfo(models.Model):
    # question = models.ForeignKey(Question, on_delete=models.CASCADE)
    title = models.CharField(u'标题', max_length=200)
    url = models.CharField('URL', max_length=200)
    img = models.CharField('图片', max_length=200)
    create_time = models.DateTimeField('创建时间')

    def __str__(self):
        return self.title
