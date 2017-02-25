from django.test import TestCase
from django.urls import reverse
from bang_app.models import Product
from bang_app.views import create_product




class TestAddProduct(TestCase):

    '''
        Purpose:
            This class tests that a customer can add a product
            and that the view routes correctly

        Methods:
            def test_customer_product_creation_routes_to_products(self):
            def test_customer_can_create_product(self):

        Author:
            @rtwhitfield84
    '''

    def test_customer_product_creation_routes_to_products(self):
        
        response = self.client.get(reverse('bang_app:products'))
        self.assertContains(response, "Products")
        self.assertEqual(response.status_code, 200)

    def test_customer_can_create_product(self):

        response = self.client.get('bang_app:create_product')
        self.assertContains(response, "Products")
        self.assertTemplateUsed('products.html')
