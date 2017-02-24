from django.shortcuts import render, get_object_or_404
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth import logout, login, authenticate
from django.http import HttpResponse, HttpResponseRedirect
from bang_app.models import Product, ProductType

class ProductDetailView(TemplateView):
  template_name = 'product_detail.html'

def list_product_detail(request):
  return HttpResponse('product detail view')

