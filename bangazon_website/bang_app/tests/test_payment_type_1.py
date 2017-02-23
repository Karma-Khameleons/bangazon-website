from django.test import TestCase 
import sys
# sys.path.append("../")
# from bang_app.models.payment_type import PaymentType
from bang_app.models import PaymentType

class TestPaymentTypeCreation(TestCase):

    def test_new_payment_is_of_class_PaymentType(self):
        new_payment = PaymentType("Visa", "11111111", "111", "01/11", "Happy Gilmore", 1)
        self.assertIsInstance(new_payment, PaymentType)


    