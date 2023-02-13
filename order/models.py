from django.db import models
from django.contrib.auth.models import User
from products.models import Product, Size, ProductSize

# Create your models here.

class Status(models.Model):
    label = models.CharField("Status Label", null=True, max_length=2, blank=True)
    status = models.CharField("Status", null=True, max_length=100, blank=True)

    def __str__(self):
        return self.status

class Order(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    orderDate = models.DateTimeField("Order Date", auto_now_add=True)
    shippingDate = models.DateField("Shipping Date", blank=True, null=True)
    orderStatus = models.ForeignKey(Status, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self) -> str:
        return str(self.id)

class OrderLine(models.Model):
    productID = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        verbose_name="Product",
        default=0
    )
    orderID = models.ForeignKey(Order, on_delete=models.CASCADE)
    sizeID = models.ForeignKey(Size, on_delete=models.CASCADE, default=1)
    quantity = models.PositiveIntegerField("Quantity")
    unitPrice = models.DecimalField("Unit Price", max_digits=5, decimal_places=2)

    
    def __str__(self) -> str:
        return str(self.id)