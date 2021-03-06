# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-06-22 08:52
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('apps', '0004_auto_20170622_0608'),
    ]

    operations = [
        migrations.CreateModel(
            name='SelectedTeam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, verbose_name=b'Team Name')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='league',
            name='match',
        ),
        migrations.RemoveField(
            model_name='league',
            name='user',
        ),
        migrations.RemoveField(
            model_name='player',
            name='team',
        ),
        migrations.RemoveField(
            model_name='team',
            name='country',
        ),
        migrations.RemoveField(
            model_name='userteam',
            name='league',
        ),
        migrations.AddField(
            model_name='player',
            name='country',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='apps.Country'),
        ),
        migrations.AddField(
            model_name='team',
            name='player',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='apps.Player'),
        ),
        migrations.AddField(
            model_name='userteam',
            name='match',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='apps.Match'),
        ),
        migrations.AlterField(
            model_name='batting',
            name='match',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='apps.Match'),
        ),
        migrations.AlterField(
            model_name='batting',
            name='player',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='apps.Player'),
        ),
        migrations.AlterField(
            model_name='bowling',
            name='match',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='apps.Match'),
        ),
        migrations.AlterField(
            model_name='bowling',
            name='player',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='apps.Player'),
        ),
        migrations.AlterField(
            model_name='fielding',
            name='match',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='apps.Match'),
        ),
        migrations.AlterField(
            model_name='fielding',
            name='player',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='apps.Player'),
        ),
        migrations.AlterField(
            model_name='point',
            name='match',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='apps.Match'),
        ),
        migrations.AlterField(
            model_name='point',
            name='player',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='apps.Player'),
        ),
        migrations.RemoveField(
            model_name='userteam',
            name='player',
        ),
        migrations.AddField(
            model_name='userteam',
            name='player',
            field=models.ManyToManyField(default=1, to='apps.Player'),
        ),
        migrations.DeleteModel(
            name='League',
        ),
        migrations.AddField(
            model_name='userteam',
            name='selected_team',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='apps.SelectedTeam'),
        ),
    ]
