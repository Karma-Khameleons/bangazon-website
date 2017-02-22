from django.conf.urls import url
from . import views

#url for each function which calls the view/function

app_name = 'bang_app'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^success/', views.Success.as_view(), name='success'),
    
    #URL for Login
    url(r'^login/', views.Login.as_view(), name='login'),
]

