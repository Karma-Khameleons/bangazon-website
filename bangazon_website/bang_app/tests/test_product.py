from django.test import TestCase
from bang_app.models import Product




class TestProduct(TestCase):

	'''
		Purpose:
			This class tests  matters related to Product

		Methods:
			def test_product_can_be_created(self):
			def test_product_fields_contain_correct_value:

		Author:
			@rtwhitfield84
	'''
	
	def test_product_can_be_created(self):

		self.ball = Product("ball", 1.99, "It's round", 3, 1, None)
		self.assertIsInstance(self.ball, Product)
	
	def test_product_fields_contain_correct_values(self):

		ball = Product(None,"ball", 1.99, "It's round", 3, 3, None)

		self.assertEqual(ball.name, "ball")
		self.assertEqual(ball.price, 1.99)
		self.assertEqual(ball.description, "It's round")
		self.assertEqual(ball.quantity, 3)
		self.assertEqual(ball.product_type, None)
		self.assertEqual(ball.seller, None)
