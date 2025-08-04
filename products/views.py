from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from accounts.forms import UserRegistrationForm
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import ProductForm
from .models import Product

# Create your views here.
def products(request):
    all_products = Product.objects.all()
    return render(request, 'products.html', {'products': all_products})

def add_products(request):
    return render(request, 'add-product.html')
def new_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, user=request.user)
        if form.is_valid():
            form.save() 
            messages.success(request, 'Product added successfully.')
            return redirect('products')
    else:
        form = ProductForm(user=request.user)
    return render(request, 'add-product.html', {'form': form})
