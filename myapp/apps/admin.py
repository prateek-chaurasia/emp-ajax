from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group 
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from employee.models import Employee
from cricket.models import Country, Season,\
		Team, Match, Player, Batting, Bowling, Fielding,\
		UserProfile, SelectedTeam, Point, UserTeam



@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
	pass

#class UserCreationForm(forms.ModelForm):
#	"""A form for creating new users. Includes
#	all required fields, plus a repeated password.
#	"""
#	password1 = forms.CharField(label='Password', 
#					widget = forms.PasswordInput)
#	password2 = forms.CharField(label='Confirm password', 
#					widget = forms.PasswordInput)
#	
#	class Meta:
#		model = UserProfile
#		fields = ('first_name','last_name', 'email',
#				'age','country')
#
#	def clean_password(self):
#		# Check for two password entries match
#		password1 = self.cleaned_data.get('password1')
#		password2 = self.cleaned_data.get('password2')
#		if password1 and password2 and password1 != password2:
#			raise forms.ValidationError("Passwords don't match.")
#		return password2
#
#	def save(self, commit=True):
#		# Save the provided password in hashed format
#		user = super.save(commit=False)
#		user.set_password(self.cleaned_data['password1'])
#		if commit:
#			user.save()
#		return user
#
#class UserChangeForm(forms.ModelForm):
#	"""A form for updating users. Includes all the fields on
#    the user, but replaces the password field with admin's
#    password hash display field.
#    """
#	password = ReadOnlyPasswordHashField()
#	
#	class Meta:
#		model = UserProfile
#		fields = ('first_name', 'last_name',
#				'email', 'age', 'country',)
#	
#	def clean_password(self):
#		# Regardless of what the user provides, return the initial value.
#		# This is done here, rather than on the field, because the
#		# field does not have access to the initial value
#		return self.initial["password"]
#
#
#class UserAdmin(BaseUserAdmin):
#    # The forms to add and change user instances
#    form = UserChangeForm
#    add_form = UserCreationForm
#
#    # The fields to be used in displaying the User model.
#    # These override the definitions on the base UserAdmin
#    # that reference specific fields on auth.User.
#    list_display = ('first_name', 'last_name',
#				'email', 'age', 'country','created_date')
#    list_filter = ('created_date',)
#    fieldsets = (
#        (None, {'fields': ('email', 'password')}),
#        ('Personal info', {'fields': ('first_name','last_name',
#							'age', 'country',)}),
##        ('Permissions', {'fields': ('is_admin',)}),
#    )
#    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
#    # overrides get_fieldsets to use this attribute when creating a user.
#    add_fieldsets = (
#        (None, {
#            'classes': ('wide',),
#            'fields': ('first_name','last_name','email',
#						'age', 'country', 'password1', 'password2')}
#        ),
#    )
#    search_fields = ('email',)
#    ordering = ('email',)
#    filter_horizontal = ()
#
## Now register the new UserAdmin...
#admin.site.register(UserProfile, UserAdmin)
## ... and, since we're not using Django's built-in permissions,
## unregister the Group model from admin.
#admin.site.unregister(Group)

admin.site.register(UserProfile)
admin.site.register(SelectedTeam)
admin.site.register(Country)
admin.site.register(Season)
admin.site.register(Team)
admin.site.register(Match)
admin.site.register(Player)
admin.site.register(Batting)
admin.site.register(Bowling)
admin.site.register(Fielding)
