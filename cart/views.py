from django.shortcuts import redirect, get_object_or_404
from django.views.decorators.http import require_POST
from .cart import Cart
from core.models import Product

@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.add(product=product, quantity=1)
    return redirect(f"{request.META.get('HTTP_REFERER', '/')}?cart_open=1")

@require_POST
def cart_decrement(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.decrement(product=product)
    return redirect(f"{request.META.get('HTTP_REFERER', '/')}?cart_open=1")

@require_POST
def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product=product)
    return redirect(f"{request.META.get('HTTP_REFERER', '/')}?cart_open=1")

