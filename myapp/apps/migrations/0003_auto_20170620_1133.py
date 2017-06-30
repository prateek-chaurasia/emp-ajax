# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-06-20 11:33
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('apps', '0002_auto_20170620_1120'),
    ]

    operations = [
        migrations.CreateModel(
            name='Batting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('runs', models.IntegerField(default=0, verbose_name=b'Runs')),
                ('balls_played', models.IntegerField(default=0, verbose_name=b'Balls Played')),
                ('fours', models.IntegerField(default=0, verbose_name=b"Four's")),
                ('sixes', models.IntegerField(default=0, verbose_name=b"Six's")),
                ('duck', models.BooleanField(default=False, verbose_name=b'Duck')),
                ('not_out', models.BooleanField(default=False, verbose_name=b'Not Out')),
                ('strike_rate', models.DecimalField(decimal_places=2, default=0.0, max_digits=15, verbose_name=b'Strike Rate')),
            ],
        ),
        migrations.CreateModel(
            name='Bowling',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('overs_delivered', models.DecimalField(decimal_places=1, default=0.0, max_digits=15, verbose_name=b'Overs Delievered')),
                ('economy', models.DecimalField(decimal_places=2, default=0.0, max_digits=15, verbose_name=b'Economy Rate')),
                ('wickets', models.IntegerField(default=0, verbose_name=b'Wickets Taken')),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name=b'Name')),
                ('short_code', models.CharField(max_length=10, verbose_name=b'Code')),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name=b'Name')),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(default=b'', max_length=200, verbose_name=b'Phone Number')),
                ('designation', models.CharField(max_length=200, verbose_name=b'Designation')),
                ('dob', models.DateField()),
                ('is_active', models.BooleanField(default=1)),
                ('created_date', models.DateTimeField(auto_now=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Fielding',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caught', models.IntegerField(default=0, verbose_name=b'Catches Taken')),
                ('run_out', models.IntegerField(default=0, verbose_name=b'Run Out')),
                ('stumped', models.IntegerField(default=0, verbose_name=b'Stumped')),
            ],
        ),
        migrations.CreateModel(
            name='League',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('match_type', models.CharField(choices=[(b'LM', b'League Match'), (b'QF', b'Quarter Final'), (b'SF', b'Semi Final'), (b'FM', b'Final')], default=b'LM', max_length=2)),
                ('dom', models.DateTimeField(verbose_name=b'Match Date')),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name=b'Name')),
                ('age', models.CharField(max_length=20, verbose_name=b'Age')),
                ('innings', models.IntegerField(default=0, verbose_name=b'Innings')),
                ('debut', models.DateField(auto_now_add=True)),
                ('total_runs', models.IntegerField(default=0, verbose_name=b'Total Runs')),
                ('total_wickets', models.IntegerField(default=0, verbose_name=b'Total Wickets')),
                ('runs_best', models.CharField(max_length=200, verbose_name=b'Runs Best')),
                ('wickets_best', models.CharField(max_length=200, verbose_name=b'Wickets Best')),
            ],
        ),
        migrations.CreateModel(
            name='Point',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('points', models.DecimalField(decimal_places=2, default=0.0, max_digits=15, verbose_name=b'Points')),
                ('match', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apps.Match')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apps.Player')),
            ],
        ),
        migrations.CreateModel(
            name='Season',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name=b'Name')),
                ('key', models.CharField(max_length=200, verbose_name=b'Key')),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name=b'Name')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apps.Country')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=100, verbose_name=b'First Name')),
                ('last_name', models.CharField(blank=True, max_length=100, verbose_name=b'Last Name')),
                ('age', models.IntegerField(default=18, help_text=b'Age should be greater than 18 years', verbose_name=b'Age')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now_add=True)),
                ('country', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='apps.Country')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserTeam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('league', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apps.League')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apps.Player')),
            ],
        ),
        migrations.AddField(
            model_name='player',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apps.Team'),
        ),
        migrations.AddField(
            model_name='match',
            name='season',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apps.Season'),
        ),
        migrations.AddField(
            model_name='match',
            name='team1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Team1', to='apps.Team'),
        ),
        migrations.AddField(
            model_name='match',
            name='team2',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Team2', to='apps.Team'),
        ),
        migrations.AddField(
            model_name='league',
            name='match',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apps.Match'),
        ),
        migrations.AddField(
            model_name='league',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='fielding',
            name='match',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apps.Match'),
        ),
        migrations.AddField(
            model_name='fielding',
            name='player',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apps.Player'),
        ),
        migrations.AddField(
            model_name='bowling',
            name='match',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apps.Match'),
        ),
        migrations.AddField(
            model_name='bowling',
            name='player',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apps.Player'),
        ),
        migrations.AddField(
            model_name='batting',
            name='match',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apps.Match'),
        ),
        migrations.AddField(
            model_name='batting',
            name='player',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apps.Player'),
        ),
    ]