from django.contrib import admin

# Register your models here.
from products.models import Product, ProductCategory, ImageAlbum, Image


admin.site.register(ProductCategory)
admin.site.register(Product)
admin.site.register(ImageAlbum)
admin.site.register(Image)
