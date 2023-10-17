from django import template
from product.models import Cart

register = template.Library()


@register.filter(name='cart_count')
def cart_count(user):
    return len(Cart.objects.filter(user=user))