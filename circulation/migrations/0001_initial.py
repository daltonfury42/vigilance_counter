# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-12-20 10:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CheckOut',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roll', models.CharField(max_length=20)),
                ('accn_no', models.CharField(max_length=20)),
                ('time_stamp', models.DateTimeField()),
            ],
        ),
    ]
