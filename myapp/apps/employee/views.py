import mimetypes
import os
import urllib2, urllib
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from models import Employee
from rest_data import retail_data
from forms import EmployeeForm
from django.views import generic
from django.shortcuts import get_object_or_404
from django.utils.encoding import smart_str

PROJECT_PATH = os.path.realpath(os.path.dirname(__file__))
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))



def ajax_test(request):
#	import ipdb;ipdb.set_trace()
	if request.method == 'GET':
		retail_list = retail_data
		print request.session.get('match_one', "Not Exists")
		print request.session.get('match_all', "Not Exists")
		return JsonResponse(retail_data)

def detail(request, employee_id):
	movie = get_object_or_404(Employee, pk=employee_id)
	return render(request, 'detail.html', {'movie': movie})


def filter_records(request):
	context = {}
	if request.method == 'POST':
		match_query = request.POST.get('match_query')
		context['match_query'] = match_query
	return render(request, 'filter_form.html',context)
		

def search_records(request):
	context = {}
	if request.method == 'POST':
		match_query_one = request.POST.get('check_one', "")
		match_query_all = request.POST.get('check_all', "")
		if match_query_one:
			val1 = request.POST.get('test1', "")
			val2 = request.POST.get('test2', "")
			val3 = request.POST.get('test3', "")
			val4 = request.POST.get('test4', "")
			request.session['match_one'] = {"values": [
				val1, val2, val3, val4
			]}
			return redirect('employee:ajax_test')
		else:
			val1 = request.POST.get('check1', "")
			val2 = request.POST.get('check2', "")
			val3 = request.POST.get('check3', "")
			val4 = request.POST.get('check4', "")
			request.session['match_all'] = {"values": [
				val1, val2, val3, val4
			]}
			return redirect('employee:ajax_test')
		

class IndexView(generic.ListView):
	template_name = 'user_list.html'
	context_object_name = 'employee_list'
	
	def get_queryset(self):
		"""Returns the list of employee filtered by recently created profile"""
		return Employee.objects.all().order_by('-created_date')


def create_employee(request):
	context = {}
	if request.method == 'POST':
		data = request.POST.get('form_data').split('&')
		data_dict = {}
		for d in data:
			data_dict[d.split("=")[0]] = urllib.unquote_plus(d.split("=")[1])
		form = EmployeeForm(data=data_dict)
		if form.is_valid():
			print "Data being sucessfully saved"
			form.save()
			return JsonResponse({'status': 'success'})
		else:
			error_dict = form.errors
			message = "Entered data is incorrect"
			return JsonResponse({'status': 'fail',
							'err_dict': error_dict, 
							'err_message': message})
	else:
		form = EmployeeForm()
		context['form'] = form
		context['err_dict'] = {}
	return render(request, 'employee_form.html',context)


def edit_employee(request, id):
	emp_id = id
	data = Employee.objects.get(id=emp_id)
	context = {}
	if request.method == 'POST':
		updated_data = request.POST.get('form_data').split('&')
		data_dict = {}
		for d in updated_data:
			data_dict[d.split("=")[0]] = urllib.unquote_plus(d.split("=")[1])
		print "Data coming in from form: ",data_dict
		form = EmployeeForm(data_dict, instance=data)
		if form.is_valid():
			print "Data being sucessfully updated"
			form.save()
			return JsonResponse({'status': 'success'})
		else:
			error_dict = form.errors
			message = "Entered data is incorrect"
			return JsonResponse({'status': 'fail',
							'err_dict': error_dict, 
							'err_message': message})
	else:
		form = EmployeeForm(instance=data)
		context['form'] = form
		context['id'] = emp_id
	return render(request, 'update_employee.html', context)

def profile(request):
	return render(request, 'portfolio.html', {})

def download_cv(request):
	file_path = os.path.join(BASE_DIR, 'static/docs/Prateek_Resume-8.doc')
	download_name = "Resume.doc"
	response = HttpResponse(content_type='application/force-download')
	response['Content-Length'] = os.path.getsize(file_path)
	response['Content-Disposition'] = "attachment; filename=%s"%smart_str(download_name)
	response['X-Sendfile'] = smart_str(file_path)
	return response

#def create_update_user(request, id=None):
#    '''This function will render a form to add a new user,
#    as well as to edit an existing user details.
#    '''
##     import ipdb;ipdb.set_trace()
#    context = RequestContext(request)
#    form_header = ''
#    if id and request.method == 'POST':
#        # This gets executed for a edit request.
#        instance = User.objects.get(id=id)
#        form = UserForm(request.POST, instance=instance)
#        if form.is_valid():
#            form.save()
#        else:
#            return render_to_response('user_form.html',
#                              {'form': form,
#                               'form_header': form_header,},
#                              context)
#        return HttpResponseRedirect(reverse("user_list"))
#    elif id:
#        user_id = id
#        user_obj = User.objects.get(id=user_id)
#        form = UserForm(instance=user_obj)
#        form_header = 'Edit User Details'
#    elif request.method == 'POST':
#        # This gets executed for a new user request.
#
#        form = UserForm(request.POST)
#        if form.is_valid():
#            form.save()
#        else:
#            return render_to_response('user_form.html',
#                              {'form': form,
#                               'form_header': form_header,},
#                              context)
#		return HttpResponseRedirect(reverse("user_list"))
#    else:
#        form = UserForm()
#        form_header = 'Add New User Details'
#    return render_to_response('user_form.html',
#                              {'form': form,
#                               'form_header': form_header},
#                              context)
