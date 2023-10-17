from django.urls import path
from product import views


urlpatterns = [
    path('product-details/<str:slug>/', views.ProductDetailView.as_view(), name="product_details"),
    # path('product/<str:slug>/', views.product_details, name="product_details"),
    path('add-to-cart/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.CartListView.as_view(), name='cart_list'),
    path('cart-quantity/<int:cart_id>/', views.modify_cart_quantity, name='cart_quantity'),
    path('delete-cart-item/<int:cart_id>/', views.delete_cart_item, name='delete_cart_item'),
]
