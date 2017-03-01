from django import forms
from django.contrib import admin
from employee.models import Employee



@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
	pass
