from django.views.generic.base import TemplateView



''' Provides the template for the url that will display once a customer completes their order.
	Author: L.Sales, Kharma Khameleons
'''
class OrderSuccess(TemplateView):
	template_name = "order_success.html"