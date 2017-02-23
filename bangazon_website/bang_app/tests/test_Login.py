from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User

from bang_app.views import login_view

import sys 
sys.path.append('../')  

from bang_app.models.customer import Customer


# class TestLogin(TestCase):

# 	def test_customer_can_login(self):
# 		"""
# 		Customer can login
# 		"""
# 		c = Client()
# 		user = dict({'username': 'abby', 'password': 'pass1234'})
# 		test_login = login_view.login_customer(c.request)
# 		print("TEST THE LOGIN **************", test_login)
# 		response = c.get(reverse('bang_app:customer_login'))
# 		print(response)
		
# 		self.assertEqual("", user)
# 		self.assertEqual("", response.status_code)
