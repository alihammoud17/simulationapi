from django.db import models

# Create your models here.

def product_image_path(instance, filename):
    return "product/images/{}/{}".format(instance.altText, filename)


class Category(models.Model):
    categoryName = models.CharField("Product Category", max_length=200, default="hoodie", unique=True)

    def __str__(self) -> str:
        return self.categoryName

class Size(models.Model):
    label = models.CharField("Size Label", max_length=5, default="S", unique=True,  blank=True, null=True)
    sizeName = models.CharField("Size Title", max_length=100, default="small", unique=True,  blank=True, null=True)

    def __str__(self) -> str:
        return self.sizeName

class Product(models.Model):
    # productID = models.UUIDField(
    #     primary_key=True,
    #     null=False,
    #     editable=False,
    #     default=uuid.uuid4()
    # )
    name = models.CharField(
        "Product Title",
        max_length=200,
        default="Hoodie 1",
        blank=True,
        null=True
    )
    description = models.TextField("Product Description", null=True, blank=True)
    isFeatured = models.BooleanField("Show on home page", default=False)
    price = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    dateCreated = models.DateTimeField(auto_now_add=True)
    dateModified = models.DateTimeField(auto_now=True)
    # productSizes = models.ManyToManyField(Size, related_name='size', through='ProductSize')
    productCategory = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, verbose_name="Product Category", blank=True)

    # def get_parents(self):
    #     return ",".join([str(p) for p in self.productSizes.all()])

    def __str__(self) -> str:
        return self.name

class ProductImage(models.Model):
    productID = models.ForeignKey(
        Product, 
        on_delete=models.CASCADE,   
        related_name="images"
    )
    imageURL = models.ImageField("Image File", upload_to=product_image_path, blank=True, null=True)
    altText = models.CharField("Image Name", max_length=200, null=True, default="image alternative", blank=True)

    def __str__(self) -> str:
        return f"{self.altText}: {self.imageURL}"

class ProductSize(models.Model):
    product = models.ForeignKey(
        Product, 
        on_delete=models.CASCADE,  
        related_name="productsizes" ,
        null=True,
        default=0
    )
    size = models.ForeignKey(
        Size,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        default=0
    )
    quantityInStock = models.PositiveBigIntegerField("Quantity", default=1)
    quantitySold = models.PositiveBigIntegerField("Quantity Sold", default=0)
