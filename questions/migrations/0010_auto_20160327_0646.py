# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-03-27 06:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0009_question_published'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
