from django.urls import path ,include
from . import views

urlpatterns = [
    path('my_order/',views.orders_item,name='history_order'),
    path('add_to_order/',views.add_to_order,name='my_order'),
    path('checkout_view/', views.checkout_view, name='checkout'),
]
