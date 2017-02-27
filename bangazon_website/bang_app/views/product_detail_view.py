from django.shortcuts import render, get_object_or_404
from django.views.generic.base import TemplateView
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth import logout, login, authenticate
from django.http import HttpResponse, HttpResponseRedirect
from bang_app.models import Customer, Product, ProductType
from bang_app import models

class ProductDetailView(TemplateView):
  template_name = 'product_detail.html'
  model = models.Product

def get_product_detail(request, id):
  print(request)
  product_detail = Product.objects.filter(id=id)
  return render(request, 'product_detail.html', {'product_detail': product_detail})




