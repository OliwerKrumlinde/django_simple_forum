# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-06 16:41
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('django_simple_forum', '0003_auto_20170830_1901'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='comment',
            field=ckeditor.fields.RichTextField(verbose_name=b'Comment'),
        ),
    ]
