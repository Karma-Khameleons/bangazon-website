from django.test import TestCase
from django.urls import reverse
from bang_app.models import Product




class TestAddProduct(TestCase):

    '''
        Purpose:
            This class tests that a customer can add a product

        Methods:
            def test_customer_can_create_product(self):

        Author:
            @rtwhitfield84
    '''

    def test_customer_product_creation_routes_to_products(self):
        
        response = self.client.get(reverse('bang_app:products'))
        self.assertContains(response, "Placeholder")
        self.assertEqual(response.status_code, 200)

    # def test_customer_can_create_product(self):
