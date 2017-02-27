from django.views.generic.base import TemplateView


''' Provides the template for the url that will display once a customer adds a product to their order.
	Author: L.Sales, Kharma Khameleons
'''
class Success(TemplateView):
	template_name = "success.html"