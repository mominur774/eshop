from django.db import models
from django.contrib.auth.models import AbstractUser
from accounts.managers import UserManager

# Create your models here.


class User(AbstractUser):
    email = models.EmailField(unique=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('username', )

    def __str__(self):
        return self.username