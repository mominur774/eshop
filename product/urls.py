from django.urls import path
from product import views


urlpatterns = [
    path('product-details/<str:slug>/', views.ProductDetailView.as_view(), name="product_details"),
    # path('product/<str:slug>/', views.product_details, name="product_details"),
    path('add-to-cart/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.CartListView.as_view(), name='cart_list'),
    path('increment-cart/<int:cart_id>/', views.increment_cart, name='increment_cart'),
    path('decrement-cart/<int:cart_id>/', views.decrement_cart, name='decrement_cart'),
    path('delete-cart-item/<int:cart_id>/', views.delete_cart_item, name='delete_cart_item'),
    path('checkout/', views.checkout_view, name='checkout'),

    path('create-billing/', views.create_billing, name='create_billing'),
    path('place-order/', views.place_order, name='place_order'),
]
