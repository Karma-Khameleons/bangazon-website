# from django.test import TestCase
# from bang_app.models import Product




# class TestAddProduct(TestCase):

# 	'''
# 		Purpose:
# 			This class tests that a customer can add a product

# 		Methods:
# 			def test_customer_can_create_product(self):

# 		Author:
# 			@rtwhitfield84
# 	'''

# 	def test_customer_can_create_product(self):

# 		ball = Product("ball", "1.99", "It's round", 3, 1, 1)
# 		response = self.client.post('/create_product/', {'product': ball})
# 		self.assertRedirects(response, '/products/')
# 		self.assertTemplateUsed(response, 'products.html')
# 	