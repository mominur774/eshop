from django.db import models
from common.models import BaseModel
from autoslug import AutoSlugField
from accounts.models import User
from enum_helper import StatusChoices, PaymentMethodChoices

# Create your models here.


class Category(BaseModel):
    name = models.CharField(max_length=255)
    display_name = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='name')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'


class Product(BaseModel):
    name = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='name')
    image = models.ImageField(upload_to='product')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')


    def __str__(self):
        return self.name



class Cart(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    purchased = models.BooleanField(default=False)

    @property
    def total_price(self):
        return self.quantity * self.product.price
    

    def __str__(self):
        return f"{self.user.username}'s cart"


class BillingDetails(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.user}'s billing"

class Order(BaseModel):
    carts = models.ManyToManyField(Cart)
    billing = models.ForeignKey(BillingDetails, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=50, 
        choices=StatusChoices.choices, 
        default=StatusChoices.PENDING
    )
    payment_method = models.CharField(
        max_length=100,
        choices=PaymentMethodChoices.choices,
        default=PaymentMethodChoices.CASH
    )


