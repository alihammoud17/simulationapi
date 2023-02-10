from django.contrib import admin
from .models import Category, Product, ProductImage, Size, ProductSize

# Register your models here.

class ImageAdminInline(admin.StackedInline):
    model = ProductImage
    extra = 1

class ProductSizeInline(admin.TabularInline):
    model = ProductSize
    extra = 1

class ProductAdmin(admin.ModelAdmin):
    inlines = (ImageAdminInline, ProductSizeInline)

# class SizeAdmin(admin.ModelAdmin):
#     inlines = (ProductSizeInline, )

admin.site.register(Product, ProductAdmin)
admin.site.register(Size)
admin.site.register(Category)
# admin.register(ProductSize)