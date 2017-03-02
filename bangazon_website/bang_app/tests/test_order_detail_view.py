from django.test import TestCase
from bang_app.models import PaymentType, Customer, CustomerOrder, Product
from bang_app.views import OrderDetailView
from django.urls import reverse
from django.contrib.auth.models import User

class TestOrderDetailView(TestCase):
    """
    Purpose: tests the functionality of the OrderDetail view

    Author: Sam Phillips
    """

    @classmethod
    def setUpTestData(self):
        """
        Provides data for test database
        """
        self.user = User(
            first_name = "Suzy",
            last_name = "Bishop",
            email = "s@s.com",
            username = "suzybishop",
            password="password1234"
        )
        self.user.save()

        self.suzy = Customer(
            user = self.user,
            city = "New Penzance" ,
            state = "Rhode Island" ,
            zip_code = "52801",
            street_address = "300 Summer's End" 
        )
        self.suzy.save()

        self.payment = PaymentType(
            card_type = "Amex",
            card_number = "1111222233334444" ,
            cvv = "956" ,
            expiration_date = "05/20",
            billing_name = "Suzy Bishop",
            customer = self.suzy
        )
        self.payment.save()

        self.new_customer_order = CustomerOrder(
            active_order=1, 
            customer=self.suzy, 
            payment_type=self.payment
        )
        self.new_customer_order.save()
        self.ball = Product(None, "ball", 1.99, "It's round", 3, 1, 1)
        self.ball.save()
        self.testing_product = Product.objects.get(pk=1)
        self.new_customer_order.line_items.add(self.testing_product)

    def test_order_detail_template_is_rendered_properly(self):
        try:
            view_request_response = self.client.get(reverse('bang_app:order_detail_view'))
            self.assertContains(view_request_response, "Your Current Order:")
            self.assertEqual(view_request_response.status_code, 200)
        except AttributeError:
            pass

    def test_closing_an_order_adds_payment_and_updates_order_to_inactive(self):
        order_pre_closing = CustomerOrder.objects.get(pk=1)

        close_order_request_response = self.client.post(
            reverse('bang_app:close_order'), 
            {"customer_order_id": order_pre_closing.id, "payment_type_id": self.payment.id}
        )
        order_post_closing = CustomerOrder.objects.get(id=order_pre_closing.id)


        self.assertEqual(order_pre_closing.id, order_post_closing.id)
        self.assertEqual(order_post_closing.active_order, 0)
        self.assertEqual(order_post_closing.payment_type, self.payment)

    def test_closing_an_order_redirects_the_user(self):
        order = CustomerOrder.objects.get(pk=1)

        close_order_request_response = self.client.post(
            reverse('bang_app:close_order'), 
           {"customer_order_id": order.id, "payment_type_id": self.payment.id}
        )
        self.assertEqual(close_order_request_response.status_code, 302)

