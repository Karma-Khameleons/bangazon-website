from django.test import TestCase, Client
from django.urls import reverse
import sys 
sys.path.append('../')  



class TestSuccessPage(TestCase):
	''' This will test whether the 200 Status response is returned from the expected page, which indicates that
		the proper page is being rendered. 
		Author: L.Sales, Karma Khameleons
	'''
	def test_display_success_page_after_product_add(self):
		try:
			response = self.client.get(reverse('bang_app:success'))
			self.assertTemplateUsed('success.html')
			self.assertEqual(response.status_code, 200)
		except AttributeError:
			pass




