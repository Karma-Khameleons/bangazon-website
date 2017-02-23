from django.db import models 
from .customer import Customer
class PaymentType(models.Model):
    """
    Purpose: maintain information relevant to a customer's payment type

    Properties: 
        card_type: the credit card name (i.e. "Visa")
        card_number: the account number associated with the card
        cvv: the 3 digit security code on the back of the card
        expiration_date: when the card expires
        billing_name: the name on the front of the card
        customer: a foreign key to the Customer the card belongs to

    Author: Sam Phillips
    """

    card_type = models.CharField(max_length=50)
    card_number = models.CharField(max_length=16)
    cvv = models.CharField(max_length=3)
    expiration_date = models.CharField(max_length=10)
    billing_name = models.CharField(max_length=100)
    customer = models.ForeignKey(Customer, related_name='payment_types', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'PaymentTypes'
    def __str__(self):
        return "{}'s {} card".format(self.billing_name, self.card_type)