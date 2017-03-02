from django.contrib.auth.models import User
from django.shortcuts import render
from django.contrib.auth import logout, login, authenticate
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic.base import TemplateView
from bang_app.models import Product, ProductType, Customer, CustomerOrder, PaymentType, LineItem


class LineItemView(TemplateView):
    """
    Purpose: Return the line item in the customer's order, Post a line item
    Methods: get - returns a dictionary containing lists
             post -  creates a new line order, if the order does not exsist, create the order first.
    Authors: Abby, Sam
    """

    def get(self, request):

        # Get the current customer determined by the logged in user (request.user)
        self.current_customer = Customer.objects.get(user=request.user.pk)
        
        # Get the current order based on the customer logged in
        self.current_order = CustomerOrder.objects.get(customer=self.current_customer.pk)

        # Get all of the line items for the current customer
        all_line_items = self.current_order.line_items.all()

        self.category_list = ProductType.objects.all()

        try:
            self.cart = CustomerOrder.objects.get(customer=request.user.customer, active_order=1)
            self.line_items = self.cart.line_items.all()
            self.total = 0
            for i in self.line_items:
                self.total +=1
            print("@@@@@@@@@@@@@@@@@@@@",self.cart)
        except CustomerOrder.DoesNotExist:
                self.total = 0
            
        # Return a request, page, and a dictionary with line items and current order
        return render(request, 'success.html', {'line_items': all_line_items, 
                                                'current_order': self.current_order,
                                                'total': self.total})



    def post(self, request):
        data = request.POST

        # Get the current customer
        current_customer = Customer.objects.get(user=request.user.pk)

        # Get the current products
        product = Product.objects.get(pk=data['product_pk'])


        # Check to see if there is an order created, if not create an order.
        try:
            current_order = CustomerOrder.objects.get(customer=current_customer, active_order=1)

        except CustomerOrder.DoesNotExist:
            current_order = CustomerOrder.objects.create(customer=current_customer, active_order=1)

        # Add the product
        # processes quantity via the custom 'through' table
        # checks to see if the product already exists as a line item
        # on the user's current order. 
        # If it does, the already existing LineItem's quantity value 
        # is increased by the POST quantity.
        try:
            old_line_item = LineItem.objects.get(
                order=current_order, 
                product=product
            )
            old_line_item.quantity += int(data['product_quantity'])
            old_line_item.save()

        # If it doesn't exist, a new LineItem is created
        except LineItem.DoesNotExist:
            new_line_item = LineItem(
                order=current_order, 
                product=product, 
                quantity=data['product_quantity']
            )
            new_line_item.save()
        

        return HttpResponseRedirect("/success")



