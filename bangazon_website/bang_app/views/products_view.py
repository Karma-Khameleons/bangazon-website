from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.contrib.auth import logout, login, authenticate
from django.http import HttpResponse, HttpResponseRedirect
from bang_app.models import Product, ProductType, Customer


class ProductsView(TemplateView):

	'''
		Purpose-
			This class provides the template to list all products

		Methods-
			get(self,request):
				gets all ProductType labels to display to customers

			def create_product(request):
				takes the request sent from form via the registered 
				customer and creates the product to sell based on
				whether the user created a category or used a predefined one

		Author:
			@rtwhitfield84
	'''

	template_name = 'products.html'

	def get(self, request):
		self.category_list = ProductType.objects.all()
		return render(request, self.template_name, {'category_list': self.category_list})

def create_product(request):

	data = request.POST

	if 'label' in data:

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

	else:

		
		Product.objects.create(
			name=data['product_name'],
			description=data['description'],
			price=data['price'],
			quantity=data['quantity'],
			product_type=ProductType.objects.get(pk=data['pk']),
			seller=Customer.objects.get(user=request.user)
		)

		return HttpResponseRedirect(redirect_to='/products')
