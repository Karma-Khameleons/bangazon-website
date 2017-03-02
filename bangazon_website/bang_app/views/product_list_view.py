from django.shortcuts import render, get_object_or_404
from django.views.generic.base import TemplateView
from django.contrib.auth import logout, login, authenticate
from django.http import HttpResponse, HttpResponseRedirect
from bang_app.models import Product, ProductType, Customer, CustomerOrder


class ProductListView(TemplateView):

  '''
    Purpose-
      This class provides the template for a customer to
      select a category and view the list of products associated with that category

    Methods-
      get_product_category_list

    Author:
      @whitneycormack
  '''
  pass
  
template_name = "product_list.html"


def get_product_category_list(request, id):
  product_category_list = Product.objects.filter(product_type_id=id) 
  try:
    cart = CustomerOrder.objects.get(customer=request.user.customer, active_order=1)
    line_items = cart.line_items.all()
    print("@@@@@@@@@@@@@", line_items)
    total = 0
    for i in line_items:
      total += 1
    print("@@@@@@@@@@@@@@@@@@@@",cart)
  except CustomerOrder.DoesNotExist:
    print("adfsaddas")
    total = 0
  except AttributeError:        
    total = 0
  return render(request, 'product_list.html', {'product_category_list': product_category_list, 
                                                'total': total})

