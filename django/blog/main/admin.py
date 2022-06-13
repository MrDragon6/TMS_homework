from django.contrib import admin
from .models import Post, Reader, Category

admin.site.register(Reader)
admin.site.register(Post)
admin.site.register(Category)
