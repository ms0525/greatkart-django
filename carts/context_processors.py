from .models import Cart, CartItem
from django.core.exceptions import ObjectDoesNotExist
from .views import _cart_id


def cart_item_count(request):
    total = 0
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
        cart_items = CartItem.objects.all().filter(cart=cart)
        for cart_item in cart_items:
            total += cart_item.quantity
    except ObjectDoesNotExist:
        pass
    
    return dict(cart_item_count=total)
    