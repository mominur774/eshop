from django.contrib import admin
from product.models import Product, Category, Cart

# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'display_name', 'slug', )


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'slug', )


class CartAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'product', 'quantity', )

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Cart, CartAdmin)