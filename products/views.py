from time import sleep
from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from accounts.forms import UserRegistrationForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import ProductForm
from .models import Product
from orders.models import Create_order , OrderItem
from decimal import Decimal
from django.db.models import Sum
import cloudinary
import cloudinary.uploader
import dotenv
import os

dotenv.load_dotenv()

cloudinary.config( 
    cloud_name = os.getenv("CLOUDINARY_CLOUD_NAME"), 
    api_key = os.getenv("CLOUDINARY_API_KEY"), 
    api_secret = os.getenv("CLOUDINARY_API_SECRET"),
    secure=True
)


def products(request):
    all_products =  list(Product.objects.all())
    categories = Product.objects.values_list('category', flat=True).distinct()
    # repeated_products = all_products * 50  
    return render(request, 'products.html', {'products': all_products,'categories':categories})

@login_required
def add_products(request):
    return render(request, 'add-product.html')

@login_required
def new_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, user=request.user)
        if form.is_valid():
            product = form.save(commit=False)

            image_file = form.cleaned_data.get('image')
            print(f"request.FILES.keys(): {request.FILES.keys()}")
            print(f"Image file: {image_file}")

            if image_file:
                try:
                    upload_result = cloudinary.uploader.upload(image_file)
                    product.image = upload_result['secure_url']
                except Exception as e:
                    messages.error(request, f"Image upload failed: {e}")
                    return render(request, 'add-product.html', {'form': form})

            product.user = request.user
            product.save()
            messages.success(request, 'Product added successfully.')
            return redirect('products')
    else:
        form = ProductForm(user=request.user)
    return render(request, 'add-product.html', {'form': form})

def product_detail(request, product_id):
    product = Product.objects.get(id=product_id)
    return render(request, 'detail.html', {'product': product})


@login_required
def seller_dashboard(request,user):
    seller_user = request.user

    total_products = Product.objects.filter(user=seller_user).count()
    seller_items = OrderItem.objects.filter(product__user=seller_user)
    total_item_ordered = seller_items.count()
    orders_completed = seller_items.filter(order__status="Delivered").count()
    current_orders = seller_items.filter(order__status="pending").count()
    seller_order_ids = seller_items.values_list('order_id', flat=True).distinct()
    
    earnings = Create_order.objects.filter(
        id__in=seller_order_ids,
        status="Delivered"
    ).aggregate(
        total=Sum('subtotal')
    )['total'] or Decimal(0)
    
    context = {
        "seller": {
            "name": seller_user.username,
            "total_products": total_products,
            "total_item_orderd": total_item_ordered,
            "orders_completed": orders_completed,
            "current_orders": current_orders,
            "earnings": earnings,
        }
    }
    return render(request, "SellerDashboard.html", context)

def seller_manage(request,user):
    seller_user = request.user
    seller_items = Product.objects.filter(user=seller_user)
    in_stock = Product.objects.filter(
        user=seller_user
    ).aggregate(
        total=Sum('quantity')
    )['total'] or Decimal(0)

    out_stock = Product.objects.filter(
        user=seller_user,
        quantity=0
    ).count()

    low_stock = Product.objects.filter(
        user=seller_user,
        quantity__lte=10,
        quantity__gt=0,
    ).count()

    context = {
        "seller": seller_user.username,
        "products": seller_items,
        "in_stock":in_stock,
        "out_stock":out_stock,
        "low_stock":low_stock,
    }
    return render(request, 'manage_products.html', context)

def del_product(request,product_id):
    seller_user = request.user
    seller_item = Product.objects.filter(user=seller_user,id=product_id)
    if seller_item:
        seller_item.delete()
        messages.success(request,'product remove successfully')
    else:
        messages.success(request,'Try again later')
    return redirect(request.META.get('HTTP_REFERER', 'home'))