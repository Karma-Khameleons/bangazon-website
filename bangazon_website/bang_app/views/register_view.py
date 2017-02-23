from django.shortcuts import render, get_object_or_404
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth import logout, login, authenticate
from django.http import HttpResponse, HttpResponseRedirect

from bang_app.models import Product, ProductType, Customer
from bang_app.views import login_view



class Register(TemplateView):
    template_name = 'bang_app/register.html'

def register_customer(request):
    """
    Resources: https://docs.djangoproject.com/en/1.10/ref/contrib/auth/#django.contrib.auth.models.UserManager
    """
    data = request.POST

    User.objects.create_user(
        username = data['username'], 
        email = data['email'],
        password = data['password'],
        first_name = data['first_name'],
        last_name = data['last_name'],
        street_address = data['street_address'],
        city = data['city'],
        state = data['state'],
        zip = data['zip']
        )
    return login_customer(request)
