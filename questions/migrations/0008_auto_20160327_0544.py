# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-03-27 05:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0007_question_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='text',
            field=models.TextField(verbose_name='\u0421\u043e\u0434\u0435\u0440\u0436\u0430\u043d\u0438\u0435 \u0432\u043e\u043f\u0440\u043e\u0441\u0430'),
        ),
        migrations.AlterField(
            model_name='question',
            name='title',
            field=models.CharField(max_length=255, verbose_name='\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a \u0432\u043e\u043f\u0440\u043e\u0441\u0430'),
        ),
    ]