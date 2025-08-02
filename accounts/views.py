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
from products.views import products

# Create your views here.
def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            account_type = form.cleaned_data['account_type']

            user = User.objects.create_user(
                username=username,
                password=password,
                email=email,
                first_name=first_name,
                last_name=last_name
            )
            Create_USER.objects.create(user=user, account_type=account_type)

            print(f"User {username} registered with account type {account_type}")
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
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('products')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'login.html')
