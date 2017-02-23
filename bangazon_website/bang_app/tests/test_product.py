from django.test import TestCase
# from django.test.utils import setup_test_environment
# from django.contrib.auth.models import User
from bang_app.models import Product, ProductType


# set_up_test_environment():

class TestProduct(TestCase):

	'''
		Purpose:
			This class tests that matters realted to Product

		Methods:
			def test_product_can_be_created(self):
			def test_product_fields_contain_correct_value:

		Author:
			@rtwhitfield84
	'''
	
	def test_product_can_be_created(self):

		self.ball = Product("ball", "1.99","It's round", 3, 1, 1)
		self.assertIsInstance(self.ball, Product)
	
	def test_product_fields_contain_correct_values(self):

		self.ball = Product("ball", "1.99","It's round", "3", 1, 1)

		self.assertTrue(self.ball.name, "ball")
		self.assertTrue(self.ball.price, "1.99")
		self.assertTrue(self.ball.description, "It's round")
		self.assertTrue(self.ball.quantity, 3)
