from django.test import TestCase, Client
from django.urls import reverse

from django.contrib.auth.models import User
from bang_app.views import login_view

from bang_app.models import Customer
from bang_app.models import ProductType
from bang_app.views import ProductListView
from bang_app.models import Product


import sys 
sys.path.append('../')  

class TestProductCategory(TestCase):

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

	def test_product_category_view_can_display(self):
	# """Testing that page will return a HTTP 200 (success) response. If so, navigation runs properly."""
		response = self.client.get(reverse('bang_app:categories'))
		self.assertTemplateUsed('products.html')
		self.assertEqual(response.status_code, 200)

	def test_product_categories(self):
		# Test to ensure that product categories return properly.
		self.assertIsInstance(self.school_supplies, ProductType)
		
		#Testing that the returned category list includes test instance. 
		response = self.client.get(reverse('bang_app:categories'))
		self.assertIn( "{'category_list': <QuerySet [<ProductType: School Supplies>]>}", str(response.context))
		




