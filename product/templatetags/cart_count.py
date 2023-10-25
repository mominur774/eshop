from django import template
from product.models import Cart

register = template.Library()


@register.filter(name='cart_count')
def cart_count(user):
    return len(Cart.objects.filter(user=user, purchased=False))


@register.filter(name='total_cart_price')
def total_cart_price(carts):
    cart_total_price = 0
    for cart in carts:
        cart_total_price += cart.total_price

    return cart_total_price