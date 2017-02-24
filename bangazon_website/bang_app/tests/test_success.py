from django.test import TestCase, Client
from django.urls import reverse
import sys 
sys.path.append('../')  



class TestSuccessPage(TestCase):
	

	def test_display_success_page_after_product_add(self):
		response = self.client.get(reverse('bang_app:success'))
		self.assertTemplateUsed('success.html')
		self.assertEqual(response.status_code, 200)




