from pyexpat.errors import messages
from django.shortcuts import render 
from django.shortcuts import redirect
from django.http import HttpResponse
from .forms import UserRegistrationForm
from django.contrib.auth.models import User 
from django.contrib import messages
from accounts.models import Create_USER
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from products.views import products

# Create your views here.
def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration successful. You can now log in.')
            return redirect('login')
        else:
            # Useful to show form errors if any
            for field in form.errors:
                for error in form.errors[field]:
                    messages.error(request, f"{field}: {error}")
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = authenticate(request, username=username , password=password)
        except :
            user = authenticate(request, email=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('products')
        else:
            messages.error(request, 'Invalid username or password.')
    if request.user.is_authenticated:
        return redirect('products')
    return render(request, 'login.html')

def logout(request):
    auth_logout(request)
    messages.success(request, 'You have been logged out successfully.')
    return redirect('login')

def profile(request):
    if request.user.is_authenticated:
        user = request.user
        profile = Create_USER.objects.filter(user=user).first()
        return render(request, 'Profile.html', {'user': user, 'profile': profile})

    messages.error(request, 'You need to log in to view your profile.')
    return redirect('login')




from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404

from django.core.paginator import Paginator

def dashboard_view(request):
    context = {
        "seller": {
            "name": request.user.get_full_name() or request.user.username or "Ahmed",
            "total_products": 32,
            "orders_completed": 145,
            "current_orders": 12,
            "earnings": "$9,720",
            "monthly_sales": 87,
            "conversion_rate": "3.2%",
            "avg_order_value": "$67",
        },
        "recent_activity": [
            {"action": "New order received", "time": "2 minutes ago", "type": "order"},
            {"action": "Product updated", "time": "1 hour ago", "type": "product"},
            {"action": "Customer review", "time": "3 hours ago", "type": "review"},
        ],
        "top_products": [
            {"name": "Smartphone", "sales": 45, "revenue": "$22,455"},
            {"name": "Laptop", "sales": 23, "revenue": "$20,677"},
            {"name": "Headphones", "sales": 67, "revenue": "$6,633"},
        ]
    }
    return render(request, 'SellerDashboard.html', context)


def manage_products_view(request):
    all_products = [
        {
            "id": 1, 
            "name": "Smartphone", 
            "price": "$499", 
            "stock": 10,
            "category": "Electronics",
            "status": "active",
            "created_date": "2024-01-15",
            "sku": "SP001"
        },
        {
            "id": 2, 
            "name": "Laptop", 
            "price": "$899", 
            "stock": 5,
            "category": "Computers",
            "status": "active",
            "created_date": "2024-01-10",
            "sku": "LP001"
        },
        {
            "id": 3, 
            "name": "Wireless Headphones", 
            "price": "$99", 
            "stock": 20,
            "category": "Electronics",
            "status": "active",
            "created_date": "2024-01-08",
            "sku": "WH001"
        },
        {
            "id": 4, 
            "name": "Gaming Mouse", 
            "price": "$59", 
            "stock": 2,
            "category": "Accessories",
            "status": "active",
            "created_date": "2024-01-05",
            "sku": "GM001"
        },
        {
            "id": 5, 
            "name": "USB-C Cable", 
            "price": "$19", 
            "stock": 0,
            "category": "Accessories",
            "status": "inactive",
            "created_date": "2024-01-03",
            "sku": "UC001"
        },
        {
            "id": 6, 
            "name": "Smartwatch", 
            "price": "$299", 
            "stock": 8,
            "category": "Electronics",
            "status": "active",
            "created_date": "2024-01-12",
            "sku": "SW001"
        },
        {
            "id": 7, 
            "name": "Bluetooth Speaker", 
            "price": "$149", 
            "stock": 15,
            "category": "Electronics",
            "status": "active",
            "created_date": "2024-01-18",
            "sku": "BS001"
        },
        {
            "id": 8, 
            "name": "Mechanical Keyboard", 
            "price": "$129", 
            "stock": 4,
            "category": "Accessories",
            "status": "active",
            "created_date": "2024-01-20",
            "sku": "MK001"
        }
    ]

    search_query = request.GET.get('search', '').strip()
    category_filter = request.GET.get('category', '')
    status_filter = request.GET.get('status', '')
    
    filtered_products = all_products
    
    if search_query:
        filtered_products = [
            product for product in filtered_products 
            if search_query.lower() in product['name'].lower() or 
               search_query.lower() in product['sku'].lower()
        ]
    
    if category_filter and category_filter != 'all':
        filtered_products = [
            product for product in filtered_products 
            if product['category'].lower() == category_filter.lower()
        ]
    
    if status_filter and status_filter != 'all':
        filtered_products = [
            product for product in filtered_products 
            if product['status'].lower() == status_filter.lower()
        ]

    # Pagination
    paginator = Paginator(filtered_products, 10)  # Show 10 products per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # Get unique categories for filter dropdown
    categories = list(set([product['category'] for product in all_products]))
    categories.sort()

    context = {
        "products": page_obj,
        "categories": categories,
        "search_query": search_query,
        "category_filter": category_filter,
        "status_filter": status_filter,
        "total_products": len(all_products),
        "filtered_count": len(filtered_products)
    }
    return render(request, 'manage_products.html', context)


def find_product(product_id):
    for product in product_data:
        if product["id"] == product_id:
            return product

def view_product_view(request, product_id):
    product = find_product(product_id)
    if not product:
        raise Http404("Product not found")
    return render(request, 'view_product.html', {'product': product})

def edit_product_view(request, product_id):
    product = find_product(product_id)
    if not product:
        raise Http404("Product not found")
    if request.method == 'POST':
        product['name'] = request.POST.get('name')
        product['price'] = request.POST.get('price')
        product['stock'] = int(request.POST.get('stock'))
        product['category'] = request.POST.get('category')
        return redirect('manage_products')
    return render(request, 'edit_product.html', {'product': product})

def delete_product_view(request, product_id):
    global product_data
    product = find_product(product_id)
    if not product:
        raise Http404("Product not found")
    product_data = [p for p in product_data if p['id'] != product_id]
    return redirect('manage_products')
