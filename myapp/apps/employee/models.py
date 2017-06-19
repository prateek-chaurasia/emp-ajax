from django.db import models
from datetime import datetime

class Employee(models.Model):
	name = models.CharField(verbose_name='Name', max_length=50)
	email = models.EmailField()
	phone = models.CharField(verbose_name='Phone Number', default='', max_length=200)
	designation = models.CharField(max_length=200, verbose_name='Designation')
	dob = models.DateField()
	is_active = models.BooleanField(default=1)
	created_date = models.DateTimeField(auto_now=True, editable=False)
	modified_date = models.DateTimeField(auto_now=True, editable=False)

	def __unicode__(self):
		return u'%s -- %s'%(self.name, self.email)

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
	country = models.ForeignKey('Country')

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
	team = models.ForeignKey('Team')
	name = models.CharField(verbose_name="Name", max_length=100)
	age = models.CharField(verbose_name="Age", max_length=20)
	innings = models.IntegerField(verbose_name="Innings", default=0)
	debut = models.DateField(auto_now_add=True)
	total_runs = models.IntegerField(verbose_name="Total Runs", default=0)
	total_wickets = models.IntegerField(verbose_name="Total Wickets", default=0)
	runs_best = models.CharField(verbose_name="Runs Best", max_length=200)
	wickets_best = models.CharField(verbose_name="Wickets Best", max_length=200)
	
	def __unicode__(self):
		return u'%s -- %s'%(self.name, self.team.name)

class Batting(models.Model):
	player = models.ForeignKey('Player')
	match = models.ForeignKey('Match', on_delete=models.CASCADE)
	runs = models.IntegerField(verbose_name="Runs", default=0)
	fours = models.IntegerField(verbose_name="Four's", default=0)
	sixes = models.IntegerField(verbose_name="Six's", default=0)
	duck = models.BooleanField(verbose_name="Duck", default=False)
	not_out = models.BooleanField(verbose_name="Not Out", default=False)
	strike_rate = models.DecimalField(verbose_name="Strike Rate", 
					decimal_places=2, default=00.00, max_digits=15)

	def __unicode__(self):
		return u'%s -- %s'%(self.player.name, self.runs)

class Bowling(models.Model):
	player = models.ForeignKey('Player')
	match = models.ForeignKey('Match', on_delete=models.CASCADE)
	economy = models.DecimalField(verbose_name="Economy Rate", 
				decimal_places=2, default=00.00, max_digits=15)
	wickets = models.IntegerField(verbose_name="Wickets Taken", default=0)

	def __unicode__(self):
		return u'%s -- %s'%(self.player.name, self.wickets)

class Fielding(models.Model):
	player = models.ForeignKey('Player')
	match = models.ForeignKey('Match', on_delete=models.CASCADE)
	caught = models.IntegerField(verbose_name="Catches Taken", default=0)
	run_out = models.IntegerField(verbose_name="Run Out", default=0)
	stumped = models.IntegerField(verbose_name="Stumped", default=0)
	
	def __unicode__(self):
		return u'%s -- %s'%(self.player.name, self.run_out)
