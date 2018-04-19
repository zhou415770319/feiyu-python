# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
# class BlogPost(models.Model):
#     title = models.CharField(max_length=150)
#     body = models.TextField()
#     timestamp = models.DateTimeField()


class Article(models.Model):
    title = models.CharField(u'标题', max_length=256)
    content = models.TextField(u'内容')
    # create_time = models.DateTimeField(u'发表时间', auto_now_add=True, editable=True)
    # update_time = models.DateTimeField(u'更新时间', auto_now=True, null=True)
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = "文章"
        verbose_name_plural = "文章"

class Category(models.Model):
    categoryName = models.CharField('类别',max_length=128)
    categoryId = models.IntegerField('类别ID',primary_key=True,db_column='类别ID',default=1)

    def __str__(self):
        return self.categoryName
    class Meta:
        verbose_name = "分类"
        verbose_name_plural = "分类"

class Tag(models.Model):
    tagName = models.CharField('类别',max_length=128)
    tagId = models.IntegerField(primary_key=True,db_column='类别ID',default=1)

    def __str__(self):
        return self.tagName
    class Meta:
        verbose_name = "标签"
        verbose_name_plural = "标签"


class Meta:
    verbose_name = "博客"
    verbose_name_plural = "博客"