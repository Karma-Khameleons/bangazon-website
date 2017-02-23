from django.shortcuts import render, get_object_or_404
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth import logout, login, authenticate
from django.http import HttpResponse, HttpResponseRedirect
from bang_app.models import Product, ProductType

class ProductsView(TemplateView):
	template_name = 'bang_app/products.html'

def create_product(request):
	new_product = request.POST
	Product.objects.create(
		name=new_product['product_name'],
		description=new_product['description'],
		price=new_product['price'],
		quantity=new_product['quantity']
		seller=request.user
	)

	return HttpResponseRedirect(redirect_to='/products')