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
