# coding: utf-8
from __future__ import unicode_literals
from django.db import models


class Topic(models.Model):

    name = models.CharField(max_length=255, verbose_name=u'Название топика')
    description = models.TextField(verbose_name=u'Описание топика')

    class Meta:
        verbose_name = u'Топик'
        verbose_name_plural = u'Топики'

    def __unicode__(self):
       return self.name
