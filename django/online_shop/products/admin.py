from django.contrib import admin
from .models import Product, Category, Brand


@admin.register(Product)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'brand', 'price', 'stock', 'available', 'created_at']
    list_filter = ['available', 'created_at', 'name']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Brand)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'country']
