from django.test import TestCase 
import sys
sys.path.append("../")
from models import PaymentType

class TestPaymentTypeCreation(TestCase):

    def test_new_payment_is_of_class_PaymentType(self):
        new_payment = PaymentType(card_type="Visa", card_number="11111111", cvv="111", expiration_date="01/11", billing_name="Happy Gilmore", customer=1)
        self.assertIsInstance(new_payment, PaymentType)

    