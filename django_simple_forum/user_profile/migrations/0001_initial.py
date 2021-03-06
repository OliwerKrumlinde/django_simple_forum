# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-30 17:09
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(default=b'uploads/avatars/default.jpg', upload_to=b'uploads/avatars/', verbose_name=b'Avatar')),
                ('title', models.CharField(default=b'New user', max_length=32, verbose_name=b'Title')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
