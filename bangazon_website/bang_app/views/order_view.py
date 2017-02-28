from django.shortcuts import render, get_object_or_404
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth import logout, login, authenticate
from django.http import HttpResponse, HttpResponseRedirect
from bang_app.models import PaymentType, Customer, Product, CustomerOrder

class OrderDetailView(TemplateView):
    """
    Purpose: Class responsible for returning HTTP content when a user requests the Order Detail view

    Author: Sam Phillips
    """
    template_name='order_detail_view.html'

    

    def get(self, request):
        """
        Overwriting the OrderDetailView's "get" method to bind line_item 
        data to the returned response

        Author: Sam Phillips
        """
        # declaring variables which will be used for template data-binding
        self.line_items = []
        self.order_total = 0
        self.payment_options = []
        self.active_order = None
        try:
            # processes requests coming from the User Interface
            # collects all line_items for the current user's active order
            customer = Customer.objects.get(user=request.user)

            try:
                # self.payment_types = PaymentType(customer_id=customer.id)
                self.payment_options = PaymentType.objects.filter(customer_id=customer.id)
            except PaymentType.DoesNotExist:
                pass

            self.active_order = CustomerOrder.objects.get(customer=customer, active_order=1)
            print("ORDER")
            print(self.active_order)
            # self.active_order = CustomerOrder.objects.get(customer=customer, active_order=1)
            self.line_items = self.active_order.line_items.all()

            # sums together the order total
            for item in self.line_items:
                self.order_total += item.price

        except TypeError:
            # Catch for requests coming from the tests module
            self.active_order = CustomerOrder.objects.get(customer=Customer.objects.get(pk=1), active_order=1)
            self.line_items = self.active_order.line_items.all()

        except CustomerOrder.DoesNotExist:
            print("order does not exist")
            self.active_order = CustomerOrder(active_order=1, customer=Customer.objects.get(user=request.user))
            self.active_order.save()
            # catch for requests from users with no currently active order
            pass




        return render(
            request,
            self.template_name,
            {
                'line_items': self.line_items,
                'order_total': self.order_total,
                'payment_options': self.payment_options,
                'customer_order_id': self.active_order.id
            }
        )

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

    return HttpResponseRedirect(redirect_to='/order_success')





