# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-03-27 11:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('topics', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='title',
            field=models.CharField(default=1, max_length=255, verbose_name='\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a \u0442\u043e\u043f\u0438\u043a\u0430'),
            preserve_default=False,
        ),
    ]