from django.conf.urls import url
from . import views

#url for each function which calls the view/function

app_name = 'bang_app'
urlpatterns = [
    url(r'^$', views.index_view.IndexView.as_view(), name='index'),
    url(r'^success/', views.Success.as_view(), name='success'),
    
    #URL for Login
    url(r'^login/', views.login_view.Login.as_view(), name='login'),
    url(r'^create_product/', views.products_view.create_product, name='create_product'),
    url(r'^products/', views.products_view.ProductsView.as_view(), name='products'),
    url(r'^payment_type/', views.create_payment_type_view.
        CreatePaymentTypeView.as_view(), name='create_payment_type_view'),
    url(r'^create_payment_type/', views.create_payment_type_view.
        create_payment_type, name='create_payment_type'),
]
