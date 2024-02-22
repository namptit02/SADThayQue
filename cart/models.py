from django.db import models
from product.models import Product
# Create your models here.

class CartItem(models.Model):
    book = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

class Order(models.Model):
    items = models.ManyToManyField(CartItem)
    total_price = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)

