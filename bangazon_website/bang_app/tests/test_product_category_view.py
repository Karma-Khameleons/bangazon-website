from django.test import TestCase, Client
from django.urls import reverse
from bang_app.models import ProductType
# from django.contrib.auth.models import User

import sys 
sys.path.append('../')  

class TestProductCategory(TestCase):

	def test_product_category_view_can_display(self):
	# """Testing that page will return a HTTP 200 (success) response. If so, navigation runs properly."""
		response = self.client.get(reverse('bang_app:products'))
		self.assertTemplateUsed('products.html')
		self.assertEqual(response.status_code, 200)

	# def test_product_categories(self):
	# 	# Test to ensure that product categories return properly.
	# 	self.food = ProductType("groceries")
	# 	self.assertIsInstance(self.food, ProductType)
	# 	#Testing that the returned category list includes test instance. 
	# 	category_list = ProductType.get_product_categories()
	# 	self.assertIn(self.food, category_list)