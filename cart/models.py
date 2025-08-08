from django.db import models
from django.contrib.auth.models import User
from products.models import Product

# Create your models here.
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=100,null=True,blank=True)
    category = models.CharField(max_length=100,null=True,blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2,null=True,blank=True)
    image = models.URLField(blank=True, null=True)


class Saved(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    name = models.CharField(max_length=100,null=True,blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2,null=True,blank=True)
    image = models.URLField(blank=True, null=True)
    