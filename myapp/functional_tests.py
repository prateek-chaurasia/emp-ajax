from selenium import webdriver
import unittest

#browser = webdriver.Firefox()
#browser.get('http://localhost:8000')

#assert 'Django' in browser.title
#browser.quit()

class NewVisitorTest(unittest.TestCase):
	def setUp(self):
		"""This function runs before and after each test """
		self.browser = webdriver.Firefox()

	def tearDown(self):
		"""This function runs before and after each test """
		self.browser.quit()

	def test_can_start_a_list_and_retrieve_it_later(self):
		"""Function starts with name test_ is a test method.
		And will run by the test runner. """
		self.browser.get("http://localhost:8000/")
		
		self.assertIn('To-Do', self.browser.title)
		self.fail('Finish the test!')


if __name__ == '__main__':
	unittest.main()


