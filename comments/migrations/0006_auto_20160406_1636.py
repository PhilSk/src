# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-04-06 16:36
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0005_comment_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 6, 16, 36, 15, 401567)),
        ),
    ]
