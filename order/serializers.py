from rest_framework import serializers
from .models import Order, OrderLine

class OrderLineSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderLine
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        pass
