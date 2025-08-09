from pyexpat.errors import messages
from django.shortcuts import render 
from django.shortcuts import redirect
from django.http import HttpResponse
from .forms import UserRegistrationForm
from django.contrib.auth.models import User 
from django.contrib import messages
from accounts.models import Create_USER
from products.models import Product
from orders.models import Create_order
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.db.models import Sum
from decimal import Decimal

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
            for field in form.errors:
                for error in form.errors[field]:
                    messages.error(request, f"{field}: {error}")
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})

def login(request):
    if request.method == 'POST':
        login_input = request.POST.get('username').strip()
        password = request.POST.get('password')


        user_obj = User.objects.filter(Q(username__iexact=login_input) | Q(email__iexact=login_input)).first()

        if user_obj:
            user = authenticate(request, username=user_obj.username, password=password)
            if user:
                auth_login(request, user)
                return redirect('products')

        messages.error(request, 'Invalid username or password.')

    if request.user.is_authenticated:
        return redirect('products')

    return render(request, 'login.html')



def logout(request):
    auth_logout(request)
    messages.success(request, 'You have been logged out successfully.')
    return redirect('login')

def new_password(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        print(user)
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')
        if new_password == confirm_password:
            user.set_password(new_password)
            user.save()
            messages.success(request, 'Your password has been updated successfully.')
            return redirect('login')
        else:
            messages.error(request, 'Passwords do not match.')
    messages.success(request, 'A password reset link has been sent to your email.')
    return render(request, 'new_password.html',{'user': user})

def reset_password(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        user_obj = User.objects.filter(Q(email__iexact=email)).first()

        try:
            if not user_obj:
                raise User.DoesNotExist
            if not user_obj.is_active:
                messages.error(request, 'This account is inactive.')
                return redirect('login')
            return redirect('new_password', user_id=user_obj.id)
        except User.DoesNotExist:
            messages.error(request, 'No user found with that email address.')
    return render(request, 'reset_password.html')

def profile(request):
    if request.user.is_authenticated:
        user = request.user
        profile = Create_USER.objects.filter(user=user).first()
        return render(request, 'Profile.html', {'user': user, 'profile': profile})

    messages.error(request, 'You need to log in to view your profile.')
    return redirect('login')

def admin_dash(request):
    user = request.user
    total_users = User.objects.count()
    total_products = Product.objects.count()
    total_orders = Create_order.objects.count()
    all_users = User.objects.filter()
    total_items = Product.objects.filter().aggregate(
        total  = Sum('quantity')
    )['total'] or Decimal(0)
    context = {
        'user':user,
        'total_products':total_products,
        'total_users':total_users,
        'total_orders':total_orders,
        'all_users':all_users,
        'total_items':total_items,
    }
    return render(request,'admin_dashboard.html',context)

def delete_user(request, user_id):
    if request.method == "POST":
        user = get_object_or_404(User, id=user_id)
        username = user.get_username()
        user.delete()
        messages.success(request, f'User "{username}" has been deleted successfully.')
        return redirect(request.META.get('HTTP_REFERER', 'home'))
    return redirect(request.META.get('HTTP_REFERER', 'home'))

def block_user(request, user_id):
    if request.method == "POST":
        user = get_object_or_404(User, id=user_id)
        username = user.get_username()
        user.is_active = False 
        user.save()
        messages.success(request, f'User "{username}" has been blocked successfully.')
    return redirect(request.META.get('HTTP_REFERER', 'home'))

def Add_superuser(request, user_id):
    if request.method == "POST":
        user = get_object_or_404(User, id=user_id)
        username = user.get_username()
        user.is_superuser = True 
        user.is_staff = True 
        user.save()
        messages.success(request, f'User "{username}" has been Superuser and added to stuff successfully.')
    return redirect(request.META.get('HTTP_REFERER', 'home'))
