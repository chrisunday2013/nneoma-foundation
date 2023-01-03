
from django.urls import path 
from . import views



urlpatterns = [
    path('', views.index, name='index'),
    path('home', views.home, name='home'),
    path('paypal-return', views.paypal_return, name='paypal-return'),
    path('paypal-cancel', views.paypal_cancel, name='paypal-cancel'),
    path("confirm_payment/<str:pk>", views.confirm_payment, name="add"),
    path("payment/", views.initiate_payment, name="initiate-payment"),
    path("<str:ref>/", views.verify_payment, name="verify-payment"),
]
