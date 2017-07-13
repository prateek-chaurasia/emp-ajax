from django.conf.urls import url

from . import views
from models import Employee

app_name = 'employee'
urlpatterns = [
    url(r'employee_list/$', views.IndexView.as_view(paginate_by=10), name="employee_list"),
    url(r'create_employee/$', views.create_employee, name="create_employee"),
    url(r'filter_records/$', views.filter_records, name="filter_records"),
    url(r'search_records/$', views.search_records, name="search_records"),
    url(r'ajax-test/$', views.ajax_test, name="ajax_test"),
	url(r'edit/(?P<id>\w+)/$', views.edit_employee, name="edit_employee_details"),
#	url(r'employee/(?P<employee_id>\w+)/$', views.detail, name="detail"),
    url(r'profile/$', views.profile, name="my_portfolio"),
    url(r'my/cv/$', views.download_cv, name="my_cv"),
]
