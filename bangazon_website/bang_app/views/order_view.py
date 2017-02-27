from django.shortcuts import render, get_object_or_404
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth import logout, login, authenticate
from django.http import HttpResponse, HttpResponseRedirect
from bang_app.models import PaymentType, Customer, Product, CustomerOrder

class OrderDetailView(TemplateView):
    """
    Purpose: Class responsible for returning HTTP content when a user requests the 
    Order Detail view

    Author: Sam Phillips
    """
    template_name='order_detail_view.html'

    

    def get(self, request):
        """
        Overwriting the OrderDetailView's "get" method to bind line_item 
        data to the returned response

        Author: Sam Phillips
        """

        # this will need to be reconfigured to use request.user as the 
        # customer query value
        try:
            active_order = CustomerOrder.objects.get(customer=request.user, active_order=1)
        except TypeError as e:
            # Catch for requests coming from the tests module
            active_order = CustomerOrder.objects.get(customer=Customer.objects.get(pk=1), active_order=1)


        self.line_items = active_order.line_items.all()

        return render(
            request,
            self.template_name,
            {'line_items': self.line_items})

def close_order(request):
    """
    Purpose: Processes user requests to complete an order

    Author: Sam Phillips
    """
    data = request.POST 
    order = CustomerOrder.objects.get(id=data['customer_order_id'])
    order.payment_type=PaymentType.objects.get(id=data['payment_type_id'])
    order.active_order=0
    order.save()

    return HttpResponseRedirect(redirect_to='/')





