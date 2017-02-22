from django.test import TestCase
from bang_app.models import Customer, Product
import sys
sys.path.append('../')

class TestProduct(TestCase):

	'''
		Purpose:
			This class tests that matters realted to Product

		Methods:
			def test_product_can_be_created(self):
			def test_customer_can_create_product(self):
			def test_product_has_type(self):

		Author:
			@rtwhitfield84
	'''

	
	def test_product_can_be_created(self):
		self.ball = Product.objects.create("ball", "1.99", "3", 1, 1)
		self.assertIsInstance(self.ball, Product)

	def test_customer_can_create_product(self):
		self.customer = Customer()
		self.ball = Product.objects.create("ball", "1.99", "3", 1, 1)
		self.customer.create_product(self.ball)
		self.assertIsInstance(self.ball)

	def test_product_has_type(self):
		self.ball = Product.objects.create("ball", "1.99", "3", 1, 1)
		self.customer.create_product(self.ball)
