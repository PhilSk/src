# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-04-06 16:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0013_question_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='likes_count',
            field=models.IntegerField(default=0),
        ),
    ]
