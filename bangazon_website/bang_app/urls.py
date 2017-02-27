from django.conf.urls import url
from . import views

#url for each function which calls the view/function

app_name = 'bang_app'
urlpatterns = [
    url(r'^$', views.index_view.IndexView.as_view(), name='index'),
    url(r'^success/', views.Success.as_view(), name='success'),
    url(r'^order_success/', views.order_success_view.OrderSuccess.as_view(), name='order_success'),


    # Login
    url(r'^customer_login/', views.login_view.login_customer, name='customer_login'),
    url(r'^login/', views.login_view.Login.as_view(), name='login'),

    #Logout
    url(r'^logout/',  views.login_view.logout_view, name='customer_logout'),

    # Register
    url(r'^customer_register/', views.register_view.register_customer, name='customer_register'),
    url(r'^register/', views.register_view.Register.as_view(), name='register'),

    # Products
    url(r'^create_product/', views.products_view.create_product, name='create_product'),
    url(r'^new_product/', views.new_product_view.NewProductView.as_view(), name='new_product'),
    url(r'^product_list/(?P<id>\d+)/$', views.product_list_view.get_product_category_list, name='product_list'),

    url(r'^categories/$', views.products_view.ProductsView.as_view(), name="categories"),

    #Product Categories
    url(r'product_detail/(?P<id>\d+)/$', views.product_detail_view.get_product_detail, name="product_detail"),


    # Payment Types

    url(r'^payment_type/', views.create_payment_type_view.CreatePaymentTypeView.as_view(), name='create_payment_type_view'),
    url(r'^create_payment_type/', views.create_payment_type_view.create_payment_type, name='create_payment_type'),

]
