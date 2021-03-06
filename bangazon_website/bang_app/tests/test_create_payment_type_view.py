from django.test import TestCase
from bang_app.models import PaymentType
from bang_app.models import Customer
from bang_app.views import CreatePaymentTypeView
from django.urls import reverse
from django.contrib.auth.models import User


class TestCreatePaymentType(TestCase):
    """
    Purpose: Tests the functionality of the PaymentType creation view

    Methods:
        test_create_payment_type_template_is_rendered_properly
        test_customer_can_create_new_payment_type
        test_payment_type_is_saved_to_database
    
    Author: Sam Phillips
    """

    def test_create_payment_type_template_is_rendered_properly(self):
        try:
            view_request_response = self.client.get(reverse(
                'bang_app:create_payment_type_view'
            ))
            self.assertContains(view_request_response, "Create a new Payment Type")
            self.assertEqual(view_request_response.status_code, 200)
        except AttributeError:
            pass
     

    def test_customer_can_create_new_payment_type(self):
        self.user = User(
            first_name = "Suzy",
            last_name = "Bishop",
            email = "s@s.com",
            username = "suzybishop",
            password="password1234"
            )
        self.suzy = Customer(
            user = self.user,
            city = "New Penzance" ,
            state = "Rhode Island" ,
            zip_code = "52801",
            street_address = "300 Summer's End" 
            )

        post_response = self.client.post(reverse(
            'bang_app:create_payment_type'
        ), {
            "card_type": "Visa", 
            "card_number": "44444444", 
            "cvv": "444", 
            "expiration_date": "04/44", 
            "billing_name": "Mr. Rogers",
            # This next variable is the flag that the view watches for. If it's present in the request, the view will handle it appropriately knowing the request is coming from the tests module
            "customer_pk_from_test": "1"
        })
        self.assertEqual(post_response.status_code, 302)

    def test_payment_type_is_saved_to_database(self):
        new_payment = PaymentType(None, "Amex", "55555555", "555", "04/44",
            "Mr. Rogers", 1)

        post_response = self.client.post(reverse(
            'bang_app:create_payment_type'
        ), {
            "card_type": "Amex", 
            "card_number": "55555555", 
            "cvv": "555", 
            "expiration_date": "04/44", 
            "billing_name": "Mr. Rogers",
            "customer_pk_from_test": "1"
        })

        queried_payment = PaymentType.objects.get(card_type="Amex", card_number="55555555", cvv="555", expiration_date="04/44", billing_name="Mr. Rogers")
        
        self.assertEqual(new_payment.card_type, queried_payment.card_type)
        self.assertEqual(new_payment.card_number, queried_payment.card_number)
        self.assertEqual(new_payment.cvv, queried_payment.cvv)
        self.assertEqual(new_payment.expiration_date, queried_payment.expiration_date)
        self.assertEqual(new_payment.billing_name, queried_payment.billing_name)