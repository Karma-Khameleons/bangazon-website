from django.shortcuts import render, get_object_or_404
from django.views.generic.base import TemplateView
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth import logout, login, authenticate
from django.http import HttpResponse, HttpResponseRedirect
from bang_app.models import Customer, Product, ProductType, CustomerOrder
from bang_app import models

class ProductDetailView(TemplateView):

  '''
    Purpose-
      This class provides the template for a customer to
      select a product and view it's details: name, price, description, quantity

    Methods-
      get_product_detail

    Author:
      @whitneycormack
  '''

  template_name = 'product_detail.html'
  model = models.Product

  def get(self, request):
    self.category_list = ProductType.objects.all()
    try:
      self.cart = CustomerOrder.objects.get(customer=request.user.customer)
      self.line_items = self.cart.line_items.all()
      self.total = 0
      for i in self.line_items:
        self.total +=1
      print("@@@@@@@@@@@@@@@@@@@@",self.cart)
    except CustomerOrder.DoesNotExist:
      self.total = 0
    return render(request, 'new_product.html', {'total': self.total})

def get_product_detail(request, id):
  product_detail = Product.objects.filter(id=id)
  return render(request, 'product_detail.html', {'product_detail': product_detail})




