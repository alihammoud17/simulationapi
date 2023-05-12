from django.db import models
from django.utils.translation import gettext_lazy as _
import uuid
from django.utils.text import slugify
from datetime import datetime


def category_image_path(instance, filename):
    return f'product/category/icons/{instance.name}/{filename}'


def product_image_path(instance, filename):
    model = instance.album.model.__class__._meta
    name = model.verbose_name_plural.replace(' ', '_')
    return f'{name}/images/{filename}'


class ImageAlbum(models.Model):

    name = models.CharField(max_length=200, null=False,
                            default="Album 1", verbose_name="Album Name")
    created_at = models.DateTimeField(
        auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created_at', )

    def __str__(self) -> str:
        return self.name

    def default(self):
        return self.images.filter(default=True).first()

    def thumbnails(self):
        return self.images.filter(width__lt=100, length_lt=100)


class Image(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to=product_image_path)
    default = models.BooleanField(default=False)
    album = models.ForeignKey(
        ImageAlbum, related_name='images', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created_at', )

    def __str__(self) -> str:
        return self.name


class ProductCategory(models.Model):
    name = models.CharField(_('Category name'), max_length=100)
    icon = models.ImageField(upload_to=category_image_path, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _('Product Category')
        verbose_name_plural = _('Product Categories')
        ordering = ('-created_at', )

    def __str__(self):
        return self.name


def get_default_product_category():
    return ProductCategory.objects.get_or_create(name='Others')[0]


class Product(models.Model):

    id = models.UUIDField(default=uuid.uuid4,
                          unique=True,
                          primary_key=True,
                          editable=False)
    category = models.ForeignKey(
        ProductCategory, related_name="product_list", on_delete=models.SET(get_default_product_category))
    album = models.OneToOneField(
        ImageAlbum, related_name='model', on_delete=models.CASCADE, blank=True)
    slug = models.SlugField(unique=True, null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField(_('Description'), blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    quantity = models.IntegerField(default=1)
    new_arrivals = models.BooleanField(default=False)
    popular_items = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created_at', )

    def __str__(self):
        return f'{self.slug} | {self.id}'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Product, self).save(*args, **kwargs)
