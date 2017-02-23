from django.test import TestCase 
import sys
from bang_app.models import PaymentType

class TestPaymentTypeCreation(TestCase):
    """
    Purpose: Tests the core functionality of the PaymentType model to ensure 
    new instances are created correctly with all relevant properties

    Author: Sam Phillips
    """

    def test_new_payment_is_of_class_PaymentType(self):
        new_payment = PaymentType("Visa", "11111111", "111", "01/11", 
            "Happy Gilmore", 1)
        self.assertIsInstance(new_payment, PaymentType)


    def test_payment_fields_contain_correct_values(self):
        new_payment = PaymentType(None, "Visa", "11111111", "111", "01/11", 
            "Happy Gilmore", 1)
        self.assertEqual(new_payment.card_type, "Visa")
        self.assertEqual(new_payment.card_number, "11111111")
        self.assertEqual(new_payment.cvv, "111")
        self.assertEqual(new_payment.expiration_date, "01/11")
        self.assertEqual(new_payment.billing_name, "Happy Gilmore")