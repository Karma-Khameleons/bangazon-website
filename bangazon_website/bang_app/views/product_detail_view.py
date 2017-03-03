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


def get_product_detail(request, id):
    product_detail = Product.objects.filter(id=id)
    try:
        cart = CustomerOrder.objects.get(customer=request.user.customer, active_order=1)
        line_items = cart.line_items.all()
        total = 0
        
        for i in line_items:
          total += 1
    
   
    except CustomerOrder.DoesNotExist:
        total = 0
    except AttributeError:        
        total = 0

    # create a list that can be looped over in the template to create the
    # appropriate quantity options when buying a product
    product_quantity = range(product_detail[0].quantity)
    product_quantity = [x+1 for x in product_quantity]

    return render(
        request, 
        'product_detail.html', 
        {
            'product_detail': product_detail,
            'total': total,
            'product_quantity': product_quantity
        }
    )




