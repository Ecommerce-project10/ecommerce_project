from django.contrib import admin
from django.urls import path ,include

from products.views import products
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('products/', products, name='products'),
    path('profile/', views.profile, name='profile'),
]
