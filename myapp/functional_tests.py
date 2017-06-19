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
		self.browser.implicitly_wait(3)

	def tearDown(self):
		"""This function runs before and after each test """
		self.browser.quit()

	def test_can_start_a_list_and_retrieve_it_later(self):
		"""Function starts with name test_ is a test method.
		And will run by the test runner. """
		self.browser.get("http://localhost:8000/lists/")
		
		self.assertIn('To-Do', self.browser.title)
		header_text = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('To-Do', header_text)

		inputbox = self.browser.find_element_by_id('id_new_item')
		self.assertEqual(
				inputbox.get_attribute('placeholder'),
				'Enter a to-do item'
		)

		inputbox.send_keys('Buy peacock feathers')

		inputbox.send_keys(Keys.ENTER)
		
		table = self.browser.get_element_by_id('id_list_table')
		rows = table.find_element_by_tag_name('tr')
		self.assertTrue(
			any(row.text == '1: Buy peacock feathers' for row in rows)
		)
		
		self.fail('Finish the test!')


if __name__ == '__main__':
	unittest.main()


