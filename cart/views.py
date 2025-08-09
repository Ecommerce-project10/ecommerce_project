import os
from django.shortcuts import render
from .models import Cart , Saved
from products.models import Product
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from decimal import Decimal
import cloudinary
import cloudinary.uploader
import dotenv
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .context_processors import cart_item

dotenv.load_dotenv()

cloudinary.config( 
    cloud_name = os.getenv("CLOUDINARY_CLOUD_NAME"), 
    api_key = os.getenv("CLOUDINARY_API_KEY"), 
    api_secret = os.getenv("CLOUDINARY_API_SECRET"),
    secure=True
)

# Create your views here.

@login_required
def get_product_by_id(request, product_id):
    return get_object_or_404(Product, id=product_id)


@login_required
def add_to_cart(request, product_id):   
    product = get_product_by_id(request, product_id)
    if product.quantity == 0:
        messages.error(request, 'This item is Out of Stock')
        return render(request, 'detail.html', {'product': product})
    cart, created = Cart.objects.get_or_create(
        user=request.user, 
        product=product,
    )

    if not created:
        cart.quantity += 1
    else:
        cart.name = product.name
        cart.category = product.category
        cart.price = product.price
        cart.image = product.image
        cart.quantity = 1  
    cart.save()
    
    messages.success(request, 'Your item was added to the cart successfully!')

    return redirect(request.META.get('HTTP_REFERER', 'home'))

@login_required
def saved_product(request, product_id):
    product = get_product_by_id(request, product_id)

    saved_item, created = Saved.objects.get_or_create(
        user=request.user, 
        product=product,
    )

    saved_item.image = product.image
    saved_item.name = product.name
    saved_item.price = product.price
    saved_item.save()

    if created:
        messages.success(request, f'"{product.name}" has been added to your saved products.')
    else:
        messages.info(request, f'"{product.name}" is already in your saved products.')

    return redirect(request.META.get('HTTP_REFERER', 'home'))

@login_required
def remove_saved_item(request , product_id):
    Saved_itm = Saved.objects.filter(user=request.user,product_id=product_id).first()
    if Saved_itm:
        Saved_itm.delete()
        messages.success(request,'Items removed from saved')
    else:
        messages.error(request,'try again later')
    return redirect(request.META.get('HTTP_REFERER', 'home'))

@login_required
def cart_view(request):
    context = cart_item(request)
    return render(request, 'cart.html', {'cart': context['cart_items'], 'subtotal': context['subtotal'], 'total_price':context['total_price'] ,'saved_item': context['saved_item']})

@login_required
def delete_item(request, product_id):
    cart_item = Cart.objects.filter(user=request.user, product_id=product_id).first()
    if cart_item:
        cart_item.delete()
        messages.success(request, "Item removed from cart.")
    else:
        messages.error(request, "Item not found in your cart.")
    return redirect(request.META.get('HTTP_REFERER', 'home'))

@login_required
def delete_all_item(request):
    cart_items = Cart.objects.filter(user=request.user)
    if cart_items.exists():
        cart_items.delete()
        messages.success(request, "All items removed from cart.")
    else:
        messages.error(request, "No items found in your cart.")
    return redirect(request.META.get('HTTP_REFERER', 'home'))


@login_required
def update_quantity(request, product_id):
    cart_item = get_object_or_404(Cart, user=request.user, product_id=product_id)

    if request.method == "POST":
        action = request.POST.get("action")
        if action == "increase":
            cart_item.quantity += 1
            messages.success(request, "Quantity increased successfully.")
        elif action == "decrease" and cart_item.quantity > 1:
            cart_item.quantity -= 1
            messages.success(request, "Quantity decreased successfully.")
        else:
            messages.warning(request, "Quantity can't be less than 1.")
        cart_item.save()

    return redirect(request.META.get('HTTP_REFERER', 'home'))

