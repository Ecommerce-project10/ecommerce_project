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
    
    path('SellerDashbaord/', views.dashboard_view, name='dashboard'),
    path('ManageProducts/', views.manage_products_view, name='manage_products'),
    path('products/<int:product_id>/', views.view_product_view, name='view_product'),
    path('products/<int:product_id>/edit/', views.edit_product_view, name='edit_product'),
    path('products/<int:product_id>/delete/', views.delete_product_view, name='delete_product'),
]
