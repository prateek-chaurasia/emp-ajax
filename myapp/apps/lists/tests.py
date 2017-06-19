from django.core.urlresolvers import resolve
from django.test import TestCase
from views import home_page
from django.http import HttpRequest
# Create your tests here.

#class SmokeTest(TestCase):
#	def test_bad_maths(self):
#		self.assertEqual(1+1,3)


class HomePageTest(TestCase):
	
	def test_root_url_resolve_to_home_page_view(self):
		found = resolve('/lists/')
		self.assertEqual(found.func, home_page)

	def test_home_page_return_correct_html(self):
		request = HttpRequest()
		response = home_page(request)
		self.assertTrue(response.content.strip().startswith(b'<html>'))
		self.assertIn(b'<title>To-Do lists</title>', response.content)
		self.assertTrue(response.content.strip().endswith(b'</html>'))
		

