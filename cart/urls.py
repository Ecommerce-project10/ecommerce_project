from django.contrib import admin
from django.urls import path ,include
from . import views

urlpatterns = [
    path('cart_view/', views.cart_view, name='cart'),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('delete_item/<int:product_id>/', views.delete_item, name='delete_item'),
    path('update_quantity/<int:product_id>/', views.update_quantity, name='update_quantity'),
    path('delete_all/', views.delete_all_item, name='delete_all'),
    path('saved_product/<int:product_id>/', views.saved_product, name='saved_product'),
    path('remove_saved_item/<int:product_id>/', views.remove_saved_item, name='remove_saved_item'),

]
