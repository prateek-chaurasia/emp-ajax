# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-08-16 06:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name=b'Name')),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(default=b'', max_length=11, verbose_name=b'Phone Number')),
                ('designation', models.CharField(max_length=200, verbose_name=b'Designation')),
                ('dob', models.DateField()),
                ('is_active', models.BooleanField(default=1)),
                ('created_date', models.DateTimeField(auto_now=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
