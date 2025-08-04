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