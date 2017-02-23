from django.test import TestCase
from bang_app.models import PaymentType
from bang_app.views import CreatePaymentTypeView
from django.urls import reverse

class TestCreatePaymentType(TestCase):
    """
    Purpose: Tests the functionality of the PaymentType creation view
    
    Author: Sam Phillips
    """

    def test_create_payment_type_template_is_rendered_properly(self):
        view_request_response = self.client.get(reverse(
            'bang_app:create_payment_type_view'
        ))
        # view_request_response = self.client.get('/create_payment_type/')
        self.assertIn("Create new payment type", view_request_response)
        

    def test_customer_can_create_new_payment_type(self):
        new_payment = PaymentType("Visa Max", "44444444", "444", "04/44", 
            "Mr. Rogers", 1)
        # post_response = self.client.post('/create_payment_type/', 
        post_response = self.client.post(reverse(
            'bang_app:create_payment_type'
        ), 
        {'payment_type': new_payment})
        self.assertIn("Success!", post_response)

    def test_payment_type_is_saved_to_database(self):
        new_payment = PaymentType("Amex", "33333333", "333", "03/33", 
            "Robot Jones", 1)
        queried_payment = PaymentType.objects.get(card_type="Amex", card_number="33333333", cvv="333", expiration_date="03/33", billing_name="Robot Jones")
        self.assertEqual(new_payment, queried_payment)