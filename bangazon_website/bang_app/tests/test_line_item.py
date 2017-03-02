from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

from bang_app.views import login_view

import sys 
sys.path.append('../')  

from bang_app.models import Customer
from bang_app.models import PaymentType
from bang_app.models import ProductType
from bang_app.models import Product
from bang_app.models import CustomerOrder



class TestLineItem(TestCase):
	"""
	Purpose: This class tests matters related to adding a line item to an order

	Methods:
		test_line_item_should_redirect_to_success_view
		test_line_item_returns_correct_context

	Author: Abby
	"""

	def setUp(self):
		
		# The most direct way to create users is to use the included create_user() helper function
		self.user = User.objects.create_user(
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

		self.suzy.save()

		self.payment = PaymentType(
			card_type = "Visa",
			card_number = "12312341234",
			cvv = "101",
			expiration_date = "10/10/17",
			billing_name = "Suzy S. Bishop",
			customer = self.suzy
			)

		self.payment.save()

		self.school_supplies = ProductType(
			label = "School Supplies"
			)

		self.school_supplies.save()

		self.scissors = Product(
			name = "Lefty Scissors",
			price = 3.99,
			description = "For the lefties",
			quantity = 3,
			product_type = self.school_supplies,
			seller = self.suzy
			)
		self.scissors.save()

		self.order = CustomerOrder(
			active_order = 1,
			customer = self.suzy,
			payment_type = self.payment,
			)
	
		self.order.save()

		# Add a line item to the order
		self.order.line_items.add(self.scissors)

		# Log in the setup customer
		self.client.login(username="suzybishop", password="password1234")


	
	def test_line_item_should_redirect_to_success_view(self):
		response = self.client.get(reverse('bang_app:categories'))
		self.assertTemplateUsed('success.html')
		self.assertEqual(response.status_code, 200)


	def test_line_item_returns_correct_context(self):
		# In order to see what's being returned, print response.context
		response = self.client.get(reverse('bang_app:list_line_items'))

		self.assertIn("{'line_items': <QuerySet [<Product: Lefty Scissors 3.99 For the lefties 3 School Supplies>]>, 'current_order': <CustomerOrder: Order for customer Suzy>, 'total': 1}", str(response.context))

	

