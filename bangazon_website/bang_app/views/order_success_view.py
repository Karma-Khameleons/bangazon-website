from django.views.generic.base import TemplateView
from django.shortcuts import render
from bang_app.models import Product, ProductType, CustomerOrder




''' Provides the template for the url that will display once a customer completes their order.
	Author: L.Sales, Kharma Khameleons
'''
class OrderSuccess(TemplateView):
	template_name = "order_success.html"

	def get(self, request):
		try:
			self.cart = CustomerOrder.objects.get(customer=request.user.customer, active_order=1)
			self.line_items = self.cart.line_items.all()
			self.total = 0
			for i in self.line_items:
				self.total +=1

		except CustomerOrder.DoesNotExist:
			self.total = 0
		return render(request, self.template_name, {'total': self.total})