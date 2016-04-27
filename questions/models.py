# coding: utf-8
from __future__ import unicode_literals
from django.db import models
from django.conf import settings
from django.dispatch import receiver

from comments.models import Comment
from topics.models import Topic
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey


class Like(models.Model):

    name = models.CharField(max_length=100)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    item_type = models.ForeignKey(ContentType)
    item_id = models.PositiveIntegerField()
    item = GenericForeignKey('item_type', 'item_id')


class Question(models.Model):

    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    title = models.CharField(max_length=255, verbose_name=u'Заголовок вопроса')
    text = models.TextField(verbose_name=u'Содержание вопроса')
    pub_date = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=False)
    topics = models.ManyToManyField(Topic, related_name='questions')
    image = models.ImageField(blank=True, null=True)
    likes_count = models.IntegerField(default=0)

    class Meta:
        verbose_name = u'Вопрос'
        verbose_name_plural = u'Вопросы'
        ordering = ('-pub_date', )

    def __unicode__(self):
       return self.title


@receiver(models.signals.post_save, sender=Comment)
def on_answer_creation(sender, instance, *args, **kwargs):
    if kwargs.get('created'):
        answer = instance
        from .tasks import send_email_notification
        send_email_notification.delay(
            'd.isaev@corp.mail.ru',
            'New answer to question "{}"'.format(answer.question.title),
            'You got answer with the text: "{}"'.format(answer.text)
        )




