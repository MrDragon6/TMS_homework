from django.contrib import admin
from .models import Post, Reader, Category, Profile, Comment

admin.site.register(Reader)
admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Profile)
admin.site.register(Comment)
