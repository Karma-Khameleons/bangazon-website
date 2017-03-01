from django.db import models
from .product import Product
from .customer_order import CustomerOrder 

class LineItem(models.Model):
    """
    Purpose: 
        Act as the intermediary between a customer's order and the 
        products on that order

    Fields:
        order (the instance of CustomerOrder)
        product (the Product being ordered)
        quantity (the number of "product" being ordered)

    Author: Sam Phillips
    """

    order = models.ForeignKey(CustomerOrder, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return "line item on {}".format(self.order)
