from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

NULLABLE = {"blank": True, "null": True}


class User(AbstractUser):
    username = None
    email = models.EmailField(verbose_name="почта", unique=True)
    phone = models.CharField(max_length=35, verbose_name="телефон")
    avatar = models.ImageField(verbose_name="Аватар", **NULLABLE)
    country = models.CharField(max_length=100, verbose_name="страна", **NULLABLE)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
