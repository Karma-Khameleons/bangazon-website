from django.shortcuts import render, get_object_or_404
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth import logout, login, authenticate
from django.http import HttpResponse, HttpResponseRedirect

from bang_app.models import Product, ProductType, Customer


class LoginSuccess(LoginRequiredMixin, TemplateView):
    template_name = 'create_product.html'

class Login(TemplateView):
    template_name = 'login.html'

	
def login_customer(request):
    print(request)

    data = request.POST.get
    print("REQUEST POST***********", data)

    username = data['username']
    password = data['password']

    user = authenticate(username=username, password=password) #Line 5

    if user is not None:
    	login(request=request, user=user) 
    else:
    	return HttpResponseRedirect(redirect_to='/')
    return HttpResponseRedirect(redirect_to='/success')
