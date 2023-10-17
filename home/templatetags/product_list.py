from django import template
from product.models import Product, Category
from home.utils import product_filter

register = template.Library()


@register.filter(name='category_wise_product')
def category_wise_product(request, category):
    filters = product_filter(request)
    products = Product.objects.filter(category=category)

    if filters:
        products = products.filter(**filters)

    return products[:10] if filters else products[:3]

