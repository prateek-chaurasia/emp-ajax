from django.db import models
from django import forms
from datetime import datetime
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings


class Country(models.Model):
	name = models.CharField(verbose_name="Name", max_length=100)
	short_code = models.CharField(verbose_name="Code", max_length=10)
	
	def __unicode__(self):
		return u'%s -- %s'%(self.short_code, self.name)

class Season(models.Model):
	name = models.CharField(verbose_name="Name", max_length=250)
	key = models.CharField(verbose_name="Key", max_length=200)
	
	def __unicode__(self):
		return u'%s -- %s'%(self.name, self.key)

class Team(models.Model):
	name = models.CharField(verbose_name="Name", max_length=100)
	player = models.ForeignKey('Player', default=1)

	def __unicode__(self):
		return u'%s'%self.name

class Match(models.Model):
	TYPE_CHOICES = (
		('LM', 'League Match'),
		('QF', 'Quarter Final'),
		('SF', 'Semi Final'),
		('FM', 'Final'),
	)
	team1 = models.ForeignKey('Team', related_name='Team1')
	team2 = models.ForeignKey('Team', related_name='Team2')
	match_type = models.CharField(choices=TYPE_CHOICES, 
					max_length=2, default='LM')
	season = models.ForeignKey('Season')
	dom = models.DateTimeField(verbose_name="Match Date")

	def __unicode__(self):
		return u'%s -- %s | %s VS %s'%(self.season.name, 
				self.match_type, self.team1.name, self.team2.name)


class Player(models.Model):
	name = models.CharField(verbose_name="Name", max_length=100)
	age = models.CharField(verbose_name="Age", max_length=20)
	country = models.OneToOneField('Country', default=1)
	innings = models.IntegerField(verbose_name="Innings", default=0)
	debut = models.DateField(auto_now_add=True)
	total_runs = models.IntegerField(verbose_name="Total Runs", default=0)
	total_wickets = models.IntegerField(verbose_name="Total Wickets", default=0)
	runs_best = models.CharField(verbose_name="Runs Best", max_length=200)
	wickets_best = models.CharField(verbose_name="Wickets Best", max_length=200)
	
	def __unicode__(self):
		return u'%s -- %s'%(self.name, self.team.name)

class Batting(models.Model):
	player = models.OneToOneField('Player', default=1)
	match = models.OneToOneField('Match', default=1)
	runs = models.IntegerField(verbose_name="Runs", default=0)
	balls_played = models.IntegerField(verbose_name="Balls Played", default=0)
	fours = models.IntegerField(verbose_name="Four's", default=0)
	sixes = models.IntegerField(verbose_name="Six's", default=0)
	duck = models.BooleanField(verbose_name="Duck", default=False)
	not_out = models.BooleanField(verbose_name="Not Out", default=False)
	strike_rate = models.DecimalField(verbose_name="Strike Rate", 
					decimal_places=2, default=00.00, max_digits=15)

	def __unicode__(self):
		return u'%s -- %s'%(self.player.name, self.runs)

class Bowling(models.Model):
	player = models.OneToOneField('Player', default=1)
	match = models.OneToOneField('Match', default=1)
	overs_delivered = models.DecimalField(verbose_name="Overs Delievered", 
				decimal_places=1, default=00.0, max_digits=15)
	economy = models.DecimalField(verbose_name="Economy Rate", 
				decimal_places=2, default=00.00, max_digits=15)
	wickets = models.IntegerField(verbose_name="Wickets Taken", default=0)

	def __unicode__(self):
		return u'%s -- %s'%(self.player.name, self.wickets)

class Fielding(models.Model):
	player = models.OneToOneField('Player', default=1)
	match = models.OneToOneField('Match', default=1)
	caught = models.IntegerField(verbose_name="Catches Taken", default=0)
	run_out = models.IntegerField(verbose_name="Run Out", default=0)
	stumped = models.IntegerField(verbose_name="Stumped", default=0)
	
	def __unicode__(self):
		return u'%s -- %s'%(self.player.name, self.run_out)

class UserProfile(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL, 
			on_delete=models.CASCADE,
			related_name='profile')
	first_name = models.CharField(verbose_name="First Name", 
					max_length=100, blank = True)
	last_name = models.CharField(verbose_name="Last Name", 
					max_length=100, blank = True)
	age = models.IntegerField(verbose_name="Age",
			help_text="Age should be greater than 18 years", 
			default=18)
	country = models.ForeignKey('Country', blank = True)
	created_date = models.DateTimeField(auto_now_add=True, editable = False)
	modified_date = models.DateTimeField(auto_now_add=True, editable = False)


	def __unicode__(self):
		return u'%s'%self.first_name

	def get_fullName(self):
		return u'%s %s'%(self.first_name, self.last_name)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
	if created:
		UserProfile.objects.create(user=instance)

class SelectedTeam(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL)
	name = models.CharField(verbose_name="Team Name", 
					max_length=100, blank = True)

	def __unicode__(self):
		return u'%s -- %s'%(self.match, self.user.username)


class UserTeam(models.Model):
	selected_team = models.ForeignKey('SelectedTeam', default=1)
	match = models.ForeignKey('Match', default=1)
	player = models.ManyToManyField('Player', default=1)

	def __unicode__(self):
		return u'%s'%self.league


class Point(models.Model):
	player = models.OneToOneField('Player', default=1)
	match = models.OneToOneField('Match', default=1)
	points = models.DecimalField(verbose_name="Points", 
				decimal_places=2, default=00.00, max_digits=15)

	def __unicode__(self):
		return u'%s | %s -- %s'%(self.match, self.player, self.points)
	
