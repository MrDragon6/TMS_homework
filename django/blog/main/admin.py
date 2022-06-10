from django.contrib import admin

from . import models

# Register your models here.


@admin.register(models.Reader)
class ReaderAdmin(admin.ModelAdmin):
    pass
