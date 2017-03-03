from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.views.generic.base import TemplateView
from django.contrib.auth import logout, login, authenticate
from django.http import HttpResponse, HttpResponseRedirect
from bang_app.models import Product, ProductType, Customer, CustomerOrder


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

	template_name = 'categories.html'

	def get(self, request):
		self.category_list = ProductType.objects.order_by('id')
		for c in self.category_list:
			c.products = Product.objects.filter(product_type_id=c.id)[:10]
			c.quantity = c.products.count()
			print(c.quantity)
		try:
			self.cart = CustomerOrder.objects.get(customer=request.user.customer, active_order=1)
			self.line_items = self.cart.line_items.all()
			self.total = 0
			for i in self.line_items:
				self.total +=1
			# self.total = Product.objects.filter()
		except CustomerOrder.DoesNotExist:
				self.total = 0
		except AttributeError:		
			self.total = 0
		return render(request, self.template_name, {'category_list': self.category_list,
													'total': self.total})

def create_product(request):

	data = request.POST
	cat_list = data['category_list']

	if cat_list == 'Select Category':

		product_category = ProductType.objects.create(label=data['label'])

		Product.objects.create(
			name=data['product_name'],
			description=data['description'],
			price=data['price'],
			quantity=data['quantity'],
			product_type=ProductType.objects.get(pk=product_category.pk),
			seller=Customer.objects.get(user=request.user)
		)

		return HttpResponseRedirect(redirect_to='/categories')

	else:


		Product.objects.create(
			name=data['product_name'],
			description=data['description'],
			price=data['price'],
			quantity=data['quantity'],
			product_type=ProductType.objects.get(pk=data['category_list']),
			seller=Customer.objects.get(user=request.user)
		)

		return HttpResponseRedirect(redirect_to='/categories')




