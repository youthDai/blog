# encoding: utf-8
from django.contrib import admin
from django.db import models

# Create your models here.
# 博客分类



class BlogPost(models.Model):
    title = models.CharField(u'博客标题', max_length=150)
    body = models.TextField(u'博客内容', max_length=2000)
    timestamp = models.DateTimeField(u'发表时间')


    def __uincode__ (self):
        return  '%s %s' % (self.title, self.body)


class BlogPostAdmin(admin.ModelAdmin):
    list_display = models.CharField('title', 'timestamp', max_length=200)


admin.site.register(BlogPost)