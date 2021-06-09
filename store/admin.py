from django.contrib import admin
from . import models
from django.utils.safestring import mark_safe

# Register your models here.
@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['display_image', 'name', 'price', 'number_in_stock', 'status', 'date_add', 'date_update']
    list_display_links = ['display_image', 'name', 'price', 'number_in_stock']
    filter_horizontal = ['categories', 'big_category']

    def display_image(self, obj):
        return mark_safe(
            f"<img src={obj.image.url} width=100px height=80px>"
        )


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(models.BigCategory)
class BigCategoryAdmin(admin.ModelAdmin):
    list_display = ['name']