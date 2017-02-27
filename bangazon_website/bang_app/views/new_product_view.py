from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.contrib.auth import logout, login, authenticate
from django.http import HttpResponse, HttpResponseRedirect
from bang_app.models import Product, ProductType

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
		print("hiiiiiiii", self.category_list)
		return render(request, 'new_product.html', {'category_list': self.category_list})
