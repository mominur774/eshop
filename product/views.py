from django.shortcuts import render, redirect
from product.models import Product, Category, Cart
from django.views.generic import ListView, DetailView
from django.db.models import F, ExpressionWrapper, fields, Sum

# Create your views here.


class ProductDetailView(DetailView):
    template_name = 'pages/product-details.html'
    model = Product
    slug_field = "slug"
    

def add_to_cart(request):
    if request.method == 'POST':
        product = Product.objects.get(pk=request.POST.get('product'))
        quantity = int(request.POST.get('quantity', 1))
        cart, created = Cart.objects.get_or_create(
            user=request.user, product=product,
            defaults={'quantity': quantity}
        )
        if not created:
            cart.quantity += quantity
            cart.save()
    return redirect(request.META.get('HTTP_REFERER'))


class CartListView(ListView):
    template_name = "pages/cart-list.html"
    model = Cart
    context_object_name = 'carts'

    def get_queryset(self):
        return Cart.objects.filter(
            user=self.request.user
        )
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        carts = Cart.objects.filter(
            user=self.request.user
        )
        cart_total_price = 0
        for cart in carts:
            cart_total_price += cart.total_price

        context['cart_total_price'] = cart_total_price

        return context


def modify_cart_quantity(request, cart_id):
    cart = Cart.objects.get(id=cart_id)
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 1))
        cart.quantity = quantity
        cart.save()
    return redirect(request.META.get('HTTP_REFERER'))

def delete_cart_item(request, cart_id):
    cart = Cart.objects.get(id=cart_id)
    if request.method == 'POST':
        cart.delete()
    return redirect(request.META.get('HTTP_REFERER'))