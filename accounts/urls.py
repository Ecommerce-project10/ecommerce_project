from django.contrib import admin
from django.urls import path ,include

from products.views import products , add_products
from products.views import new_product , product_detail
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('products/', products, name='products'),
    path('products/add_products/', add_products, name='add_products'),
    path('products/new_product/', new_product, name='new_product'),
    path('products/<int:product_id>/', product_detail, name='product_detail'),
    path('reset_password/', views.reset_password, name='reset_password'),
    path('reset_password/new_password/<int:user_id>/', views.new_password, name='new_password'),
]
