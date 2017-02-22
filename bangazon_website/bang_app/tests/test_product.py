from django.test import TestCase
from bang_app.models import Customer, Product

class ProductTestCase(TestCase):

	
	def test_product_has_name(self):
		self.ball = Product.objects.create("ball", "1.99", "3", "sporting goods", 1)
		self.assertIsInstance(self.ball, Product)
