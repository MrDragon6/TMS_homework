from django.contrib import admin
from .models import Post, Reader, Author, Category, Profile, Comment, Subscription


admin.site.register(Reader)
admin.site.register(Author)
admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Profile)
admin.site.register(Comment)
admin.site.register(Subscription)
