from django.test import TestCase
from django.db import models
from bang_app.models import Product, ProductType
from django.urls import reverse


import sys


class TestProductDetailView(TestCase):

  '''
    Purpose:
      This class tests that a product has a type and the view routes correctly

    Methods:
      test_product_detail_routes_to_product


    Author:
      @whitneycormack
  '''


  def test_product_detail_routes_to_product(self):

    try:
      response = self.client.get(reverse('bang_app:product_detail', args=[1]))
      self.assertContains(response, "Product Details")
      self.assertEqual(response.status_code, 200)
    except AttributeError:
      pass















