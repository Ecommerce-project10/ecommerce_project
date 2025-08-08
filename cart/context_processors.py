from .models import Cart
from .models import Saved
from decimal import Decimal

def cart_item(request):
    if request.user.is_authenticated:
        cart_items = Cart.objects.filter(user=request.user)
        saved_item = Saved.objects.filter(user=request.user)
        subtotal = sum(item.price * item.quantity for item in cart_items)
        Shipping_fee = Decimal(15.00)
        Tax = Decimal(56.80)
        total_price = subtotal + Shipping_fee + Tax

        return {
            'cart_items': cart_items,
            'saved_item': saved_item,
            'subtotal': subtotal,
            'Shipping_fee': Shipping_fee,
            'Tax': Tax,
            'total_price': total_price,
        }
    return {}

def cart_item_count(request):
    if request.user.is_authenticated:
        cart_count = Cart.objects.filter(user=request.user).count()
    else:
        cart_count = 0
    return {'cart_count': cart_count}

def saved_products(request):
    if request.user.is_authenticated:
        saved_ids = Saved.objects.filter(user=request.user).values_list('product_id',flat=True)
    else:
        saved_ids = []
    return {'saved_ids':saved_ids}

def order_count(request):
    from orders.models import Create_order
    if request.user.is_authenticated:
        n_order = Create_order.objects.filter(user=request.user).count()
    else:
        n_order = []
    return {'n_order':n_order}
