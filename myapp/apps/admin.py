from django import forms
from django.contrib import admin
from employee.models import Employee, Country, Season,\
		Team, Match, Player, Batting, Bowling, Fielding



@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
	pass

admin.site.register(Country)
admin.site.register(Season)
admin.site.register(Team)
admin.site.register(Match)
admin.site.register(Player)
admin.site.register(Batting)
admin.site.register(Bowling)
admin.site.register(Fielding)
