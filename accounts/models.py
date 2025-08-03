from django.contrib.auth.models import User
from django.db import models

class Create_USER(models.Model):
    ACCOUNT_TYPES = [
        ('customer', 'Customer'),
        ('seller', 'Seller'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE ,related_name='profile')
    account_type = models.CharField(max_length=10, choices=ACCOUNT_TYPES , default='customer') 
