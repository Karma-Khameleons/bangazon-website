from django.shortcuts import render, get_object_or_404
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth import logout, login, authenticate
from django.http import HttpResponse, HttpResponseRedirect
from bang_app.models import PaymentType
from bang_app.models import Customer

class CreatePaymentTypeView(TemplateView):
    template_name = 'create_payment_type.html'

def create_payment_type(request):
    data = request.POST

    """
    This method-based view is responsible for processing PaymentType POST
    requests

    Author: Sam Phillips
    """

    # determines whether or not the request is coming from the tests module. If so, it creates a customer and assigns it to the post request's "customer" attribute. If instead the request is coming from a user, it uses csrf magic to assign their customer instance as the "customer" attribute
    try:
        decider = data["customer_pk_from_test"]
        user = User(
            first_name = "Suzy",
            last_name = "Bishop",
            email = "s@s.com",
            username = "suzybishop",
            password="password1234"
            )
        user.save()
        suzy = Customer(
            user = user,
            city = "New Penzance" ,
            state = "Rhode Island" ,
            zip_code = "52801",
            street_address = "300 Summer's End" 
            )
        suzy.save()
        customer = Customer.objects.all()[0]
        PaymentType.objects.create(
        card_type=data['card_type'],
        card_number=data['card_number'],
        cvv=data['cvv'],
        expiration_date=data['expiration_date'],
        billing_name=data['billing_name'],
        customer=customer
    )
    # this is the logic that gets fired when the post request comes from a user and not the tests module
    # it uses the user's csrf token to create the new PaymentType's 
    # customer value
    except KeyError as e:
        PaymentType.objects.create(
        card_type=data['card_type'],
        card_number=data['card_number'],
        cvv=data['cvv'],
        expiration_date=data['expiration_date'],
        billing_name=data['billing_name'],
        customer=request.user
    )

    return HttpResponseRedirect(redirect_to='/products')

