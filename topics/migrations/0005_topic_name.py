# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-03-27 12:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('topics', '0004_auto_20160327_1151'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='name',
            field=models.CharField(default=1, max_length=255, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0442\u043e\u043f\u0438\u043a\u0430'),
            preserve_default=False,
        ),
    ]