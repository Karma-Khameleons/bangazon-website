from django.test import TestCase
from bang_app.models import Customer, Product
import sys
sys.path.append('../')

class TestProduct(TestCase):

	
	def test_product_can_be_created(self):
		self.ball = Product.objects.create("ball", "1.99", "3", "sporting goods", 1)
		self.assertIsInstance(self.ball, Product)
