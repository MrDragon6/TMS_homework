from django.contrib.auth.models import User
from django.db import models
from datetime import datetime
from django.urls import reverse
from ckeditor.fields import RichTextField

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
    header_image = models.ImageField(null=True, blank=True, upload_to='images/')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = RichTextField(blank=True, null=True)
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    category = models.CharField(max_length=255, default='uncategorized')
    snippet = models.CharField(max_length=255)
    likes = models.ManyToManyField(User, related_name='blog_posts')

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return f'{self.title} | {self.author}'

    @staticmethod
    def get_absolute_url():
        return reverse('home')


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField()
    profile_picture = models.ImageField(null=True, blank=True, upload_to='images/profile/')
    website_url = models.CharField(null=True, blank=True, max_length=255)
    facebook_url = models.CharField(null=True, blank=True, max_length=255)
    vkontakte_url = models.CharField(null=True, blank=True, max_length=255)
    instagram_url = models.CharField(null=True, blank=True, max_length=255)

    def __str__(self):
        return str(self.user)
