from django.views.generic.base import TemplateView
from django.shortcuts import render
from bang_app.models import CustomerOrder



''' Provides the template for the url that will display once a customer adds a product to their order.
	Author: L.Sales, Kharma Khameleons
'''
class Success(TemplateView):
	template_name = "success.html"

	def get(self, request):
		try:
			self.cart = CustomerOrder.objects.get(customer=request.user.customer, active=1)
			self.line_items = self.cart.line_items.all()
			self.total = 0
			for i in self.line_items:
				self.total +=1
			print("@@@@@@@@@@@@@@@@@@@@",self.cart)
		except CustomerOrder.DoesNotExist:
			self.total = 0
		return render(request, self.template_name, {'total': self.total})