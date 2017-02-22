from django.test import TestCase
# from django.test.utils import setup_test_environment
from django.contrib.auth.models import User
from bang_app.models import Customer, Product
import sys
sys.path.append('../')

# set_up_test_environment():

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
	@classmethod
	def setUpClass(self):
		
		self.user = User(
			first_name="phil",
			last_name="product",
			email="p@p.com"
			)

		self.phil = Customer(
			user=self.user,
			city="New Pinanche",
			state="Confusion",
			zip_code="12343",
			street_address="300 Winter's End"
			)

		self.ball = Product("ball", "1.99","It's round", "3", 1, 1)
	
	def test_product_can_be_created(self):
		self.assertIsInstance(self.ball, Product)

	# def test_customer_can_create_product(self):
	# 	self.customer = Customer()
	# 	self.ball = Product.objects.create("ball", "1.99", "3", 1, 1)
	# 	self.customer.create_product(self.ball)
	# 	self.assertIsInstance(self.ball)

	# def test_product_has_type(self):
	# 	self.ball = Product.objects.create("ball", "1.99", "3", 1, 1)
	# 	self.customer.create_product(self.ball)
