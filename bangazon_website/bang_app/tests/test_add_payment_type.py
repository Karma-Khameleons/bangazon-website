from django.test import TestCase 
import sys
sys.path.append("../")
from bang_app.models.payment_type import PaymentType


# reconfigure for http requests instead of direct interaction
class TestAddPaymentType(TestCase):

    def test_new_payment_can_be_saved(self):
        new_payment = PaymentType(card_type="MasterCard", card_number="22222222", cvv="222", expiration_date="02/22", billing_name="Carl Sagan", customer=2)
        all_payments = PaymentType.objects.all()
        final_index = len(all_payments) - 1
        last_saved_payment = all_payments[final_index]
        self.assertEqual(new_payment, last_saved_payment)
    
    def test_payment_can_be_retrieved_by_id(self):
        new_payment = PaymentType(card_type="Visa", card_number="11111111", cvv="111", expiration_date="01/11", billing_name="Happy Gilmore", customer=1)
        queried_payment = PaymentType.objects.get(pk=new_payment['pk'])
        self.assertEqual(new_payment, queried_payment)