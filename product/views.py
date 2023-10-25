from django.shortcuts import render, redirect
from django.urls import reverse
from product.models import Product, Category, Cart, BillingDetails, Order
from django.views.generic import ListView, DetailView
from django.db.models import F, ExpressionWrapper, fields, Sum
from product.forms import BillingForm
from enum_helper import StatusChoices
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
            user=self.request.user,
            purchased=False
        )


def modify_cart_quantity(request, cart_id):
    cart = Cart.objects.get(id=cart_id)
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 1))
        cart.quantity = quantity
        cart.save()
    return redirect(request.META.get('HTTP_REFERER'))


def increment_cart(request, cart_id):
    cart = Cart.objects.get(id=cart_id)
    cart.quantity += 1
    cart.save()
    return redirect(request.META.get('HTTP_REFERER'))

def decrement_cart(request, cart_id):
    cart = Cart.objects.get(id=cart_id)
    if cart.quantity > 1:
        cart.quantity -= 1
        cart.save()
    return redirect(request.META.get('HTTP_REFERER'))


def delete_cart_item(request, cart_id):
    cart = Cart.objects.get(id=cart_id)
    cart.delete()
    return redirect(request.META.get('HTTP_REFERER'))



def checkout_view(request):
    if request.method == 'POST':
        request.session['checkout_cart'] = request.POST.getlist('cart_item')
    return redirect(reverse('place_order'))


def create_billing(request):
    form = BillingForm()
    if request.method == 'POST':
        form = BillingForm(request.POST)
        if form.is_valid():
            billing = form.save(commit=False)
            billing.user = request.user
            billing.save()
            return redirect(reverse('place_order'))
    
    context = {
        'form': form
    }
    return render(request, 'pages/billing.html', context)

def place_order(request):
    carts = Cart.objects.filter(pk__in=request.session.get('checkout_cart'))
    billing_details = BillingDetails.objects.filter(user=request.user)

    if request.method == 'POST':
        billing = BillingDetails.objects.get(pk=request.POST.get('billing'))
        order = Order.objects.create(
            billing=billing,
            payment_method=request.POST.get('payment_method'),
            status=StatusChoices.PROCESSING
        )
        order.carts.set(request.session.get('checkout_cart'))
        if order:
            carts.update(purchased=True)
        
        return redirect('/')

    context = {
        'carts': carts,
        'billing_details': billing_details
    }
    return render(request, 'pages/checkout.html', context)
 