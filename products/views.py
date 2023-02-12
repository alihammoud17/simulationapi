from django.shortcuts import render
from rest_framework.views import APIView
from .models import Product, Category, Size
from .serializers import SizeSerializer, ProductSerializer, CategorySerializer
from rest_framework.response import Response
from django.http import Http404

# Create your views here.
class ProductView(APIView):

    # Get All Products
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

class ProductDetailView(APIView):

    def get_object(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            raise Http404


    # Get a specific product
    def get(self, request, pk):
        product = self.get_object(pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

class CategoriesView(APIView):

    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

class SizesView(APIView):

    def get(self, request):
        sizes = Size.objects.all()
        serializer = SizeSerializer(sizes, many=True)
        return Response(serializer.data)