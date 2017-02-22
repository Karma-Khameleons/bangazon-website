from django.test import TestCase
from bang_app.models import Product
import sys
sys.path.append('../')

class TestProductType(TestCase):

	def test_product_has_type(self):
		self.ball = Product.objects.create("ball", "1.99", "3", 1, 1)
		self.assertIsInstance(self.ball, Product)
		self.assertTrue(self.ball.ProductType, 1)
