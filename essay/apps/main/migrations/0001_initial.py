# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-24 13:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User_Essay',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='\u4fdd\u5b58\u65e5\u671f')),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='\u6700\u540e\u4fee\u6539\u65e5\u671f')),
                ('content', models.CharField(max_length=350)),
                ('isSubmit', models.BooleanField()),
            ],
        ),
    ]
