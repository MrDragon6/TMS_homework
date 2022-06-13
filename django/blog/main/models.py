from django.contrib.auth.models import User
from django.db import models
from datetime import datetime
from django.urls import reverse

# Create your models here.


class Reader(models.Model):
    class Meta:
        verbose_name = 'Reader'
        verbose_name_plural = 'Readers'

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
        related_name='reader',
    )

    registration_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.user.username


class Category(models.Model):
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    @staticmethod
    def get_absolute_url():
        return reverse('home')


class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    creation_date = models.DateTimeField(default=datetime.now, blank=True)
    category = models.CharField(max_length=255, default='uncategorized')

    def __str__(self):
        return f'{self.title} | {self.author}'

    @staticmethod
    def get_absolute_url():
        return reverse('home')
