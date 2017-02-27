from django.test import TestCase, Client
from django.urls import reverse
import sys 
sys.path.append('../')  



class TestOrderSuccessPage(TestCase):
	''' This will test whether the 200 Status response is returned from the expected page, which indicates that
		the proper page is being rendered. 
		Author: L.Sales, Karma Khameleons
	'''
	def test_display_success_page_after_order_complete(self):
		response = self.client.get(reverse('bang_app:order_success'))
		self.assertTemplateUsed('order_success.html')
		self.assertEqual(response.status_code, 200)




