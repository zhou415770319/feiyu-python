# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from login.models import User
import datetime
# Create your models here.
# class BlogPost(models.Model):
#     title = models.CharField(max_length=150)
#     body = models.TextField()
#     timestamp = models.DateTimeField()

class Category(models.Model):
    categoryName = models.CharField('分类',max_length=128)
    categoryImg = models.ImageField(upload_to='categoryImg')
    categoryImg.verbose_name = "图片"

    # categoryImg = models.CharField('图片地址',max_length=100 ,null=True,blank=True)
    categoryId = models.IntegerField('分类ID',primary_key=True,db_column='分类ID',default=1)

    def __str__(self):
        return self.categoryName
    class Meta:
        verbose_name = "分类"
        verbose_name_plural = "分类"

class Tag(models.Model):
    tagName = models.CharField('标签',max_length=128)
    tagId = models.IntegerField(primary_key=True,db_column='标签ID',default=1)

    def __str__(self):
        return self.tagName
    class Meta:
        verbose_name = "标签"
        verbose_name_plural = "标签"



class Article(models.Model):
    title = models.CharField(u'标题', max_length=256)
    content = models.TextField(u'内容',default="")
    des = models.TextField(u'描述',default="")

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    user.verbose_name = u'作者'
    # img = models.CharField(u'图片地址', max_length=100,null=True,blank=True)
    # img = models.ImageField(upload_to='img')
    # img.verbose_name = "图片"
    # contentdes = models.TextField(u'内容',default="")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    category.verbose_name = "分类"
    tag = models.ManyToManyField(Tag)
    tag.verbose_name = "标签"
    isPub = models.BooleanField('发布状态',default=False)
    commentNum = models.IntegerField('评论数',default=0)
    readNum = models.IntegerField('阅读数',default=0)

    create_time = models.DateTimeField(u'发表时间',default=datetime.datetime.now)
    update_time = models.DateTimeField(u'更新时间',default=datetime.datetime.now)
    readonly_fields = ('create_time','update_time')

    # 获取后台文本编辑器图文内容中图片url地址
    # 需要引入PyQuery
    # def get_contentimg_url(self):
    #     temp = Article.objects.filter(pk=str(self.id)).values('content')  # values获取Article数据表中的content字段内容
    #     html = pq(temp[0]['content'])  # pq方法获取编辑器html内容
    #     img_path = pq(html)('img').attr('src')  # 截取html内容中的路径
    #     return img_path  # 返回图片路径
    def __str__(self):
        # if len(self.content) > 40:
        #     self.contentdes = '{0}...'.format(self.content[0:39])
        return self.title
    class Meta:
        # db_table = 'Article'
        ordering = ["create_time"]
        verbose_name = "文章"
        verbose_name_plural = "文章"

class Comment(models.Model):
    title = models.CharField(u'评论标题', max_length=256)
    content = models.TextField(u'评论内容', default="")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    user.verbose_name = u'评论者'
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    article.verbose_name = u'评论的博客'
    create_time = models.DateTimeField(u'评论时间', default=datetime.datetime.now)
    update_time = models.DateTimeField(u'评论时间', default=datetime.datetime.now)
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = "评论"
        verbose_name_plural = "评论"

# class ImageStore(models.Model):
#     img = models.ImageField(upload_to='img')
#




class Meta:
    db_table = 'Category,Article'

    verbose_name = "博客"
    verbose_name_plural = "博客"