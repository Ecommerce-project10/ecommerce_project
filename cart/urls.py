from django.contrib import admin
from django.urls import path ,include
from . import views

urlpatterns = [
    path('cart_view/', views.cart_view, name='cart'),
    path('checkout_view/', views.checkout_view, name='checkout'),
]
