from django.test import TestCase
from bang_app.models import Customer, Product

class ProductTestCase(TestCase):

	# def setUp(self):
	# 	Product.objects.create()
	
	def test_user_can_create_product():

