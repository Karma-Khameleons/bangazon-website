from django.db import models
from .customer import Customer
from .payment_type import PaymentType
from .product import Product

class CustomerOrder(models.Model):
    """
    Purpose: Maintain information relevant to a Customer's order

    Author: Sam Phillips
    """
    
    active_order = models.IntegerField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    payment_type = models.ForeignKey(PaymentType, null=True, on_delete=models.CASCADE)
    line_items = models.ManyToManyField(Product)

    def __str__(self):
        return "Order for customer {}".format(self.customer)