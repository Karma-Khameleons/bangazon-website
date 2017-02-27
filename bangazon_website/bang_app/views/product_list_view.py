from django.shortcuts import render, get_object_or_404
from django.views.generic.base import TemplateView
from django.contrib.auth import logout, login, authenticate
from django.http import HttpResponse, HttpResponseRedirect
from bang_app.models import Product, ProductType, Customer


class ProductListView(TemplateView):
	template_name = "product_list.html"


def get_product_category_list(request, id):
  product_category_list = Product.objects.filter(product_type_id=id)
  print("product cat list", product_category_list)
  return render(request, 'product_list.html', {'product_category_list': product_category_list})

