from django.test import TestCase
from django.contrib.auth.models import User

import sys 
sys.path.append('../') 

from bang_app.models.customer import Customer
import datetime


# python manage.py test bang_app

class TestCustomer(TestCase):
	"""
	Purpose: Test Customer
	Author: Abby
	Tests: 
		test_customer_has_properties
		test_customer_is_instance
		test_customer_has_account_creation_date
		test_customer_has_id
		test_customer_has_full_name
		test_customer_has_street_address
		test_customer_has_zip_code
		test_customer_has_state
		test_customer_has_email
	"""


	@classmethod
	def setUpClass(self):
		
		self.user = User(
			first_name = "Suzy",
			last_name = "Bishop",
			email = "s@s.com",
			username = "suzybishop",
			password="password1234"
			)


		self.suzy = Customer(
			user = self.user,
			city = "New Penzance" ,
			state = "Rhode Island" ,
			zip_code = "52801",
			street_address = "300 Summer's End" 
			)

	

	def test_customer_has_account_creation_date(self):
		self.assertTrue("", self.suzy.get_creation_date())

	def test_customer_has_id(self):
		self.assertTrue("", self.suzy.get_customer_id())

	def test_customer_has_full_name(self):
		self.assertTrue("", self.suzy.User.get_full_name())

	def test_customer_has_street_address(self):
		self.assertTrue("", self.suzy.get_address())

	def test_customer_has_zip_code(self):
		self.assertTrue("", self.suzy.get_postal_zip())

	def test_customer_has_state(self):
		self.assertTrue("", self.suzy.get_state())

	def test_customer_has_email(self):
		self.assertTrue("", self.suzy)
	

	