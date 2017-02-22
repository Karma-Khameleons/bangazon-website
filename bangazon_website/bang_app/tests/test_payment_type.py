from django.test import TestCase 
import sys
sys.path.append("../")
from models import PaymentType

class PaymentTypeCreationTests(TestCase):

    def test_new_payment_is_of_class_PaymentType:
        new_payment = PaymentType(relevant arguments)
        self.assertIsInstance(new_payment, PaymentType)

    def test_new_payment_can_be_saved:
        new_payment = PaymentType(relevant arguments)
        all_payments = PaymentType.objects.all()
        final_index = len(all_payments) - 1
        last_saved_payment = all_payments[final_index]
        self.assertEqual(new_payment, last_saved_payment)