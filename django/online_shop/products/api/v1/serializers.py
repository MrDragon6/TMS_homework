from rest_framework import serializers
from django.contrib.auth.models import User

from products.models import Product, Category, Brand


class CategorySerializer(serializers.Serializer):
    title = serializers.CharField(max_length=60)


class BrandSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=60)
    country = serializers.CharField(max_length=60)

    def create(self, validated_data):
        return Brand.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.country = validated_data.get('country', instance.country)
        instance.save()
        return instance


class ProductBaseSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(allow_blank=True, max_length=50)
    price = serializers.IntegerField()
    description = serializers.CharField()
    created_at = serializers.DateTimeField(required=False)
    updated_at = serializers.DateTimeField(required=False)
    available_inventory = serializers.IntegerField()


class ProductCreateSerializer(ProductBaseSerializer):
    title = serializers.CharField(max_length=60)
    description = serializers.CharField(max_length=500)
    price = serializers.IntegerField()

    def create(self, validated_data):
        return Product.objects.create(**validated_data)


class ProductUpdateSerializer(ProductBaseSerializer):
    title = serializers.CharField(max_length=60)
    description = serializers.CharField(max_length=500)
    price = serializers.IntegerField()

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.price = validated_data.get('price', instance.price)
        instance.save()
        return instance


class ProductReadSerializer(ProductBaseSerializer):
    pass
