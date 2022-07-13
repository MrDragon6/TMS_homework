from rest_framework import serializers
from django.http import HttpResponse

from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name')
