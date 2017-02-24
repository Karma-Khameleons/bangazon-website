from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth import logout, login, authenticate
from django.http import HttpResponse, HttpResponseRedirect
from bang_app.models import Product, ProductType, Customer

class SelectCategoryView(TemplateView):
	template_name = 'select_category.html'

	def get(self, request):
		self.category_list = ProductType.objects.all()
		print("hiiiiiiii", self.category_list)
		return render(request, 'select_category.html', {'category_list': self.category_list})