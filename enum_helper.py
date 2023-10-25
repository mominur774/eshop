from django.db import models
from django.utils.translation import gettext_lazy as _



class StatusChoices(models.TextChoices):
    CANCELLED = 'CANCELLED', _('Cancelled')
    COMPLETED = 'COMPLETED', _('Completed')
    FAILED = 'FAILED', _('Failed')
    ONHOLD = 'ONHOLD', _('On Hold')
    PENDING = 'PENDING', _('Pending')
    PROCESSING = 'PROCESSING', _('Processing')
    REFUNDED = 'REFUNDED', _('Refunded')


class PaymentMethodChoices(models.TextChoices):
    CASH = 'CASH', _('Cash on Delivery')
    STRIPE = 'STRIPE', _('Stripe')