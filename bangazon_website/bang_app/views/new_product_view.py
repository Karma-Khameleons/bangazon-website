from django.shortcuts import render, get_object_or_404
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth import logout, login, authenticate
from django.http import HttpResponse, HttpResponseRedirect
from bang_app.models import Product, ProductType

class NewProductView(TemplateView):
	template_name = 'new_product.html'

	# def get(self, request):
	# 	self.categories = ProductType.objects.all()
	# 	print("@@@@@@@@@@@@@", self.categories)
	# 	return render(request, self.template_name, {'categories': self.categories})
