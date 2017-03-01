from django import forms
from models import Employee
from myapp import settings
from django.utils.translation import ugettext_lazy as _

class EmployeeForm(forms.ModelForm):
	dob = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS)
	class Meta:
		model = Employee
		exclude = ['is_active','created_date','modified_date']
		help_texts = {
            'dob': _('Please enter date in dd-mm-yyyy or yyyy-mm-dd formats'),
        }


