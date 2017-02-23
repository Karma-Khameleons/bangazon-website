from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
# import view

import sys 
sys.path.append('../')  

from bang_app.models.customer import Customer


class TestRegister(TestCase):

	# @classmethod
	# def setUpClass(self):
		
	# 	self.user = User(
	# 		first_name = "Suzy",
	# 		last_name = "Bishop",
	# 		email = "s@s.com",
	# 		username = "suzybishop",
	# 		password="password1234"
	# 		)


	# 	self.suzy = Customer(
	# 		user = self.user,
	# 		city = "New Penzance" ,
	# 		state = "Rhode Island" ,
	# 		zip_code = "52801",
	# 		street_address = "300 Summer's End" 
	# 		)


	def test_page_has_customer_name(self):
		"""
		Page should display the customer's name
		"""
		response = self.client.get(reverse('bang_app:create_product'))
		# response: <HttpResponse status_code=200, "text/html; charset=utf-8">
		self.assertContains(response, "Suzy")
		self.assertEqual(response.status_code, 200)




