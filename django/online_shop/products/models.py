from django.db import models


class Brand(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Brand'
        verbose_name_plural = 'Brands'

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(null=False, blank=False, max_length=100)
    description = models.TextField()
    price = models.PositiveIntegerField(null=False, blank=False)
    stock = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    image = models.ImageField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='products')

    class Meta:
        ordering = ('name',)
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.name
