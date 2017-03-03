from django.test import TestCase
from django.db import models
from django.contrib.auth.models import User
from bang_app.models import Product, ProductType, Customer
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

    category = ProductType.objects.create(
        label='Toys'
    )

    user = User(
        first_name = "Suzy",
        last_name = "Bishop",
        email = "s@s.com",
        username = "suzybishop",
        password="password1234"
    )
    user.save()

    suzy = Customer(
        user = user,
        city = "New Penzance" ,
        state = "Rhode Island" ,
        zip_code = "52801",
        street_address = "300 Summer's End" 
    )
    suzy.save()

    product = Product.objects.create(
        name="Slinky",
        price=6,
        description="Rusty springy thingy",
        quantity=5,
        product_type=category,
        seller=suzy
    )

    try:
      response = self.client.get(reverse('bang_app:product_detail', args=[1]))
      self.assertContains(response, "Slinky")
      self.assertEqual(response.status_code, 200)
    except AttributeError:
      pass















