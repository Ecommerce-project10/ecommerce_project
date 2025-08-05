from time import sleep
from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from accounts.forms import UserRegistrationForm
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import ProductForm
from .models import Product
import cloudinary
import cloudinary.uploader
# import dotenv
# import os

# # Load environment variables from .env file
# dotenv.load_dotenv()
# # Configure Cloudinary with environment variables
# cloudinary.config( 
#     cloud_name = os.getenv("CLOUDINARY_CLOUD_NAME"), 
#     api_key = os.getenv("CLOUDINARY_API_KEY"), 
#     api_secret = os.getenv("CLOUDINARY_API_SECRET"),
#     secure=True
# )

cloudinary.config( 
    cloud_name = "dl0hsdl8i", 
    api_key = "686294187252397", 
    api_secret = "2PKhr8w1gvakug1_0xRLYSU0dWo",
    secure=True
)

# Create your views here.
def products(request):
    all_products =  list(Product.objects.all())
    # repeated_products = all_products * 50  
    return render(request, 'products.html', {'products': all_products})

def add_products(request):
    return render(request, 'add-product.html')
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