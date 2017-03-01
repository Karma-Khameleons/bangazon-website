from django.shortcuts import render, get_object_or_404
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth import logout, login, authenticate
from django.http import HttpResponse, HttpResponseRedirect

from bang_app.models import Product, ProductType, Customer,CustomerOrder
from bang_app.views import login_view



class Register(TemplateView):
    template_name = 'register.html'

    def get(self, request):
        try:
            self.cart = CustomerOrder.objects.get(customer=request.user.customer)
            self.line_items = self.cart.line_items.all()
            self.total = 0
            for i in self.line_items:
                self.total +=1
            print("@@@@@@@@@@@@@@@@@@@@",self.cart)
        except CustomerOrder.DoesNotExist:
            self.total = 0
        return render(request, self.template_name, {'total': self.total})


def register_customer(request):
    """
    Purpose: Register a customer and immediently login
    Author: Abby

    """
    # create_user is what holds the username/password. (Django magic)
    # then, we pass that into the 1:1 field on our model, Customer
    # send all of the information to login_customer on login_view.py

    data = request.POST

    new_user = User.objects.create_user(
        username = data['username'], 
        email = data['email'],
        password = data['password'],
        first_name = data['first_name'],
        last_name = data['last_name'],
        )

    Customer.objects.create(
        user = new_user,
        street_address = data['street_address'],
        city = data['city'],
        state = data['state'],
        zip_code = data['zip_code']
        )

    return login_view.login_customer(request)
