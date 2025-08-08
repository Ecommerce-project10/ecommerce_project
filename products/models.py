from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.URLField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    rate = models.PositiveIntegerField(default=5, help_text="Rate from 1 to 5")
    category = models.CharField(max_length=50, choices=[
        ('electronics', 'Electronics'),
        ('clothing', 'Clothing'),
        ('books', 'Books'),
        ('toys', 'Toys'),
        ('home', 'Home'),
        ('sports', 'Sports'),
        ('health', 'Health'),
        ('beauty', 'Beauty'),
        ('other', 'Other'),
    ])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name