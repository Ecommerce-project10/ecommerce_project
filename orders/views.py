from django.shortcuts import render ,get_object_or_404 ,redirect
from django.contrib.auth.decorators import login_required
from products.models import Product
from .models import Create_order , OrderItem
from cart.views import cart_view
from cart.context_processors import cart_item
from decimal import Decimal
from cart.models import Cart 


# Create your views here.
@login_required
def get_product_by_id(request, product_id):
    return get_object_or_404(Product, id=product_id)

def checkout_view(request):
    context = cart_item(request)
    return render(request, 'checkout.html',{'cart': context['cart_items'], 'Tax':context['Tax'],'subtotal': context['subtotal'],'total_price':context['total_price'],'Shipping_fee':context['Shipping_fee']},)


from django.views.decorators.csrf import csrf_exempt

@login_required
def add_to_order(request):
    if request.method == "POST":
        item_data = cart_item(request)
        cart_items = Cart.objects.filter(user=request.user)

        order = Create_order.objects.create(
            user=request.user,
            full_name=request.POST.get("name"),
            address=request.POST.get("address"),
            city=request.POST.get("city"),
            phone=request.POST.get("phone"),
            payment_method=request.POST.get("payment_method"),
            subtotal=item_data['subtotal'],
            shipping_cost=item_data['Shipping_fee'],
            total=item_data['total_price'],
        )

        for item in cart_items:
            OrderItem.objects.create(
                order=order,
                product=item.product,
                price=item.price,
                quantity=item.quantity,
                total=(item.price * item.quantity)+item_data['Shipping_fee']+item_data['Tax']
            )
        
        cart_items.delete()

        return redirect('history_order')  
    return redirect('cart')


@login_required
def orders_item(request):
    user_orders = Create_order.objects.filter(user=request.user)
    context = cart_item(request)
    return render(request, 'order.html', {
        'orderitem': user_orders,
        'Tax':context['Tax'],
    })