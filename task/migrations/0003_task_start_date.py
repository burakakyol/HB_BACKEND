# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-12-20 11:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0002_auto_20171217_2230'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='start_date',
            field=models.DateField(auto_now=True),
        ),
    ]