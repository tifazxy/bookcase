# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-22 04:02
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('fishing_books', '0002_auto_20180414_0741'),
    ]

    operations = [
        migrations.AddField(
            model_name='storage',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
