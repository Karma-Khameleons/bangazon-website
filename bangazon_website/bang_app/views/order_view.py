from django.shortcuts import render, get_object_or_404
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth import logout, login, authenticate
from django.http import HttpResponse, HttpResponseRedirect
from bang_app.models import PaymentType, Customer, Product, CustomerOrder, LineItem

class OrderDetailView(TemplateView):
    """
    Purpose: Class responsible for returning HTTP content when a user requests the Order Detail view

    Author: Sam Phillips
    """
    template_name='order_detail_view.html'

    def get(self, request):
        print("*******HELLO? ORDER VIEW*********")

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
            self.cart = CustomerOrder.objects.get(customer=request.user.customer, active_order=1)
            self.line_items = self.cart.line_items.all()
            # self.line_items = list(self.cart.line_items)
            self.total = 0
            for i in self.line_items:
                self.total +=1
            # self.total = Product.objects.filter()

        except CustomerOrder.DoesNotExist:
                self.total = 0

        # collects all line_items and payment type options for the current user's active order
        try:
            # processes requests coming from the User Interface
            customer = Customer.objects.get(user=request.user)
            try:
                self.payment_options = PaymentType.objects.filter(customer_id=customer.id)
            except PaymentType.DoesNotExist:
                pass
            self.payment_options = list(self.payment_options)
            self.active_order = CustomerOrder.objects.get(customer=customer, active_order=1)
            
            self.line_items = LineItem.objects.filter(order=self.active_order)


            # sums together the order total
            for item in self.line_items:
                print("***** LINE ITEM BY ACTIVE ORDER*****", item)
                self.order_total += item.product.price


        except TypeError:
            # Catch for requests coming from the tests module
            self.active_order = CustomerOrder.objects.get(customer=Customer.objects.get(pk=1), active_order=1)
            self.line_items = self.active_order.line_items.all()

        except CustomerOrder.DoesNotExist:
            # catch for requests from users with no currently active order
            # creates a new order for the user
            self.active_order = CustomerOrder(active_order=1, customer=Customer.objects.get(user=request.user))
            self.active_order.save()
            pass



        return render(
            request,
            self.template_name,
            {
                'line_items': self.line_items,
                'order_total': self.order_total,
                'payment_options': self.payment_options,
                'customer_order_id': self.active_order.id,
                'total': self.total,
            }
        )

def close_order(request):
    """
    Purpose: Processes user requests to complete an order

    Author: Sam Phillips
    """
    data = request.POST 
    order = CustomerOrder.objects.get(id=data['customer_order_id'])

    # checks to see if the user is trying to create a new payment type for this order. If so, it creates that payment type and assigns it to the order. 
    # Otherwise it assigns the pk of the selected payment type.
    if data['payment_type_id'] == 'new':
        new_payment_type = PaymentType.objects.create(
        card_type=data['card_type'],
        card_number=data['card_number'],
        cvv=data['cvv'],
        expiration_date=data['expiration_date'],
        billing_name=data['billing_name'],
        customer=Customer.objects.get(user=request.user)
        )
        new_payment_type.save()
        order.payment_type = new_payment_type
    else:
        order.payment_type=PaymentType.objects.get(id=data['payment_type_id'])
    # closes the order and updates it in the database
    order.active_order=0
    order.save()

    return HttpResponseRedirect(redirect_to='/order_success')


