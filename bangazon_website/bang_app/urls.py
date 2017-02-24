from django.conf.urls import url
from . import views

#url for each function which calls the view/function

app_name = 'bang_app'
urlpatterns = [
    url(r'^$', views.index_view.IndexView.as_view(), name='index'),
    url(r'^success/', views.Success.as_view(), name='success'),
    
    # Login
    url(r'^customer_login/', views.login_view.login_customer, name='customer_login'),
    url(r'^login/', views.login_view.Login.as_view(), name='login'),

    # Register
    url(r'^customer_register/', views.register_view.register_customer, name='customer_register'),
    url(r'^register/', views.register_view.Register.as_view(), name='register'),

    # Products
    url(r'^create_product/', views.products_view.create_product, name='create_product'),
    url(r'^new_product/', views.new_product_view.NewProductView.as_view(), name='new_product'),
    url(r'^products/', views.products_view.ProductsView.as_view(), name='products'),
]
