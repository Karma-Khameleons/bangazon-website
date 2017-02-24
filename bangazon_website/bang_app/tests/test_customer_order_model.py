from django.test import TestCase 
from bang_app.models import CustomerOrder, Customer, PaymentType
from django.contrib.auth.models import User

class TestCustomerOrderCreation(TestCase):
    """
    Purpost: Tests the instantiation of a CustomerOrder instance to ensure
    all values are correctly assigned
    """

    @classmethod
    def setUpTestData(self):
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

        self.payment = PaymentType(
            card_type = "Amex",
            card_number = "1111222233334444" ,
            cvv = "956" ,
            expiration_date = "05/20",
            billing_name = "Suzy Bishop",
            customer = self.suzy
        )

        self.new_customer_order = CustomerOrder(
            active_order=1, 
            customer=self.suzy, 
            payment_type=self.payment
        )


    def test_new_order_is_of_class_CustomerOrder(self):
        self.assertIsInstance(self.new_customer_order, CustomerOrder)

    def test_new_order_values_are_assigned_correctly(self):
        self.assertEqual(self.new_customer_order.active_order, 1)
        self.assertEqual(self.new_customer_order.customer, self.suzy)
        self.assertEqual(self.new_customer_order.payment_type, self.payment)