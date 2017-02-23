from django.shortcuts import render, get_object_or_404
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth import logout, login, authenticate
from django.http import HttpResponse, HttpResponseRedirect
from bang_app.models import PaymentType

class CreatePaymentTypeView(TemplateView):
    template_name = 'bang_app/create_payment_type.html'

def create_payment_type(request):
    new_payment_type = request.POST 
    PaymentType.objects.create(
        card_type=new_payment_type['card_type'],
        card_number=new_payment_type['card_number'],
        cvv=new_payment_type['cvv'],
        expiration_date=new_payment_type['expiration_date'],
        billing_name=new_payment_type['billing_name'],
        customer=1
        # customer=request.user
    )




    
# def create_payment_type(request):
#     new_payment_type = request.POST 
#     PaymentType.objects.create(
#         card_type=new_payment_type['card_type'],
#         card_number=new_payment_type['card_number'],
#         cvv=new_payment_type['cvv'],
#         expiration_date=new_payment_type['expiration_date'],
#         billing_name=new_payment_type['billing_name'],
#         customer=1
#         # customer=request.user
#     )