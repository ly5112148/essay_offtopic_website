# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-24 14:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Essay',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('due_time', models.DateField()),
                ('type', models.CharField(choices=[('AT', 'Autonomous'), ('PL', 'Plan')], default='AT', max_length=2)),
            ],
        ),
    ]
