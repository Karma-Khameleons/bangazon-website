from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.contrib.auth import logout, login, authenticate
from django.http import HttpResponse, HttpResponseRedirect
from bang_app.models import Product, ProductType, CustomerOrder

class NewProductView(TemplateView):

	'''
		Purpose-
			This class provides the template for a customer to
			select a category and create a product or create
			a category and product

		Methods-
			get(self,request):
				gets all ProductType labels to populate the select menu
		Author:
			@rtwhitfield84
	'''

	template_name = 'new_product.html'

	def get(self, request):
		self.category_list = ProductType.objects.all()
		try:
			self.cart = CustomerOrder.objects.get(customer=request.user.customer, active_order=1)
			self.line_items = self.cart.line_items.all()
			self.total = 0
			for i in self.line_items:
				self.total +=1
			
			
		except CustomerOrder.DoesNotExist:
			self.total = 0
		return render(request, 'new_product.html', {'category_list': self.category_list,
													'total': self.total})
