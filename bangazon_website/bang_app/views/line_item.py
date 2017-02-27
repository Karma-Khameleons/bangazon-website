from django.contrib.auth.models import User
from django.shortcuts import render
from django.contrib.auth import logout, login, authenticate
from django.http import HttpResponseRedirect
from django.views.generic.base import TemplateView
from bang_app.models import Product, ProductType, Customer, CustomerOrder


class LineItemView(TemplateView):
	"""
	Purpose: Return the line item in the customer's order
	Methods: get - returns a dictionary containing lists
	Author: Abby
	"""

	template_name = 'success.html'


	def get(self, request):

		# Get the current customer determined by the logged in user (request.user)
		self.current_customer = Customer.objects.get(user=request.user.pk)
		
		# Get the current order based on the customer logged in
		self.current_order = CustomerOrder.objects.get(customer=self.current_customer.pk)

		# Get all of the line items for the current customer
		all_line_items = self.current_order.line_items.all()
			
		# Return a request, page, and a dictionary with line items and current order
		return render(request, 'success.html', {'line_items': all_line_items, 'current_order': self.current_order})
