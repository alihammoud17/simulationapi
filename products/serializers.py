from rest_framework import serializers
from .models import Product, ProductImage, ProductSize, Size, Category

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['id', 'imageURL', 'altText']

class ProductSizeSerializer(serializers.ModelSerializer):
        class Meta:
            model = ProductSize
            fields = '__all__'

class SizeSerializer(serializers.ModelSerializer):
        class Meta:
            model = Size
            fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = "__all__"
        
class ProductSerializer(serializers.ModelSerializer):
    # productImages = serializers.StringRelatedField(many=True)
    
    images = ImageSerializer(many=True, read_only=True)
    sizes = ProductSizeSerializer(many=True, read_only=True)
    productCategory = CategorySerializer(many=False, read_only=True)

    # def getCategory(self):
    #     return self.productCategory.categoryName
    class Meta:
        model = Product
        fields = [
            'id',
            'name',
            'description',
            'isFeatured',
            'price',
            'images',
            'sizes',
            'productCategory'
        ]

