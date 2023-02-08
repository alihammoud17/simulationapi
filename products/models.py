from django.db import models
import uuid

# Create your models here.

def product_image_path(instance, filename):
    return "product/images/{}/{}".format(instance.title, filename)


class Size(models.Model):
    label = models.CharField(max_length=1)
    sizeName = models.CharField(max_length=100, default="small")

    def __str__(self) -> str:
        return self.sizeName

class Product(models.Model):
    productID = models.UUIDField(
        primary_key=True,
        null=False,
        editable=False,
        default=uuid.uuid5
    )
    name = models.CharField(
        max_length=200
    )
    description = models.TextField()
    isFeatured = models.BooleanField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    dateCreated = models.DateTimeField(auto_now_add=True)
    dateModified = models.DateTimeField(auto_now=True)
    productSizes = models.ManyToManyField(Size, related_name='size', through='ProductSize')

    def __str__(self) -> str:
        return self.name




class ProductImage(models.Model):
    productID = models.ForeignKey(
        Product, 
        on_delete=models.CASCADE,   
    )
    imageURL = models.ImageField(upload_to=product_image_path, blank=True)


class ProductSize(models.Model):
    product = models.ForeignKey(
        Product, 
        on_delete=models.CASCADE,   
    )
    size = models.ForeignKey(
        Size,
        on_delete=models.CASCADE
    )
    quantityInStock = models.IntegerField()
