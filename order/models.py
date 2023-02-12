from django.db import models
from django.contrib.auth.models import User
from products.models import Product

# Create your models here.

class Status(models.Model):
    STATUS = [
        ("P", "PENDING"), 
        ("A", "APPROVED"), 
        ("D", "DELIVERED")
    ]

    status = models.CharField("Status", choices=STATUS, null=True, max_length=100)

class Order(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    orderDate = models.DateTimeField("Order Date", auto_now_add=True)
    shippingDate = models.DateField("Shipping Date")
    orderStatus = models.ForeignKey(Status, on_delete=models.SET_NULL, null=True)


class OrderLine(models.Model):
    productID = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        verbose_name="Product"
    )
    orderID = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField("Quantity")
    unitPrice = models.DecimalField("Unit Price", max_digits=5, decimal_places=2)