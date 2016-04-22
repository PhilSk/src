# coding: utf-8
from __future__ import unicode_literals

from datetime import datetime
from time import timezone

from django.db import models

from django.conf import settings


class Comment(models.Model):

    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    text = models.TextField(verbose_name=u'Содержание комментария')
    question = models.ForeignKey('questions.Question', related_name= "comments")
    pub_date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
           verbose_name = u'Коммент'
           verbose_name_plural = u'Комменты'

    def __unicode__(self):
       return self.text