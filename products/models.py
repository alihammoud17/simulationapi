from django.db import models
import uuid

# Create your models here.

def product_image_path(instance, filename):
    return "product/images/{}/{}".format(instance.title, filename)


class Size(models.Model):
    label = models.CharField("Size Label", max_length=1)
    sizeName = models.CharField("Size Title", max_length=100, default="small")

    def __str__(self) -> str:
        return self.sizeName

class Product(models.Model):
    productID = models.UUIDField(
        primary_key=True,
        null=False,
        editable=False,
        default=uuid.uuid4()
    )
    name = models.CharField(
        "Product Title",
        max_length=200
    )
    description = models.TextField("Product Description", null=True)
    isFeatured = models.BooleanField("Show on home page")
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
    imageURL = models.ImageField("Image File", upload_to=product_image_path, blank=True)
    altText = models.CharField("Image Name", max_length=200, null=True)

class ProductSize(models.Model):
    product = models.ForeignKey(
        Product, 
        on_delete=models.CASCADE,   
    )
    size = models.ForeignKey(
        Size,
        on_delete=models.CASCADE
    )
    quantityInStock = models.IntegerField("Quantity", default=1)
