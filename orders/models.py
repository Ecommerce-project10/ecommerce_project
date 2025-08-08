from decimal import Decimal
from django.db import models
from django.contrib.auth.models import User
from products.models import Product
from cart.context_processors import cart_item
import random

# Create your models here.
class Create_order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('shipped', 'Shipped'),
        ('delivered', 'Delivered'),
        ('cancelled', 'Cancelled'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    full_name = models.CharField(max_length=100)
    address = models.CharField(max_length=250)
    city = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    shipping_cost = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('15.00'))
    total = models.DecimalField(max_digits=10, decimal_places=2)
    
    payment_method = models.CharField(max_length=20)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Delivered')
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    order_number = models.CharField(max_length=100, unique=True, blank=True)
    
    def save(self, *args, **kwargs):
        if not self.order_number:
            self.order_number = str(random.randint(100000, 999999))
        super().save(*args, **kwargs)

    @property
    def status_color(self):
        if self.status == "Pending":
            return "warning"
        elif self.status == "Delivered":
            return "success"
        elif self.status == "Cancelled":
            return "danger"
        return "secondary"

class OrderItem(models.Model):
    order = models.ForeignKey(Create_order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)
    total = models.DecimalField(max_digits=10, decimal_places=2)

