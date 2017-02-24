from django.shortcuts import render, get_object_or_404
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth import logout, login, authenticate
from django.http import HttpResponse, HttpResponseRedirect
from bang_app.models import Product, ProductType, Customer

class ProductsView(TemplateView):
	template_name = 'products.html'


def create_product(request):

	data = request.POST

	product_category = ProductType.objects.create(label=data['label'])
	
	Product.objects.create(
		name=data['product_name'],
		description=data['description'],
		price=data['price'],
		quantity=data['quantity'],
		product_type=ProductType.objects.get(pk=product_category.pk),
		seller=Customer.objects.get(user=request.user)
	)

	return HttpResponseRedirect(redirect_to='/products')