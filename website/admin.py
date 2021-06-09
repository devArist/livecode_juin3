from django.contrib import admin
from . import models
from django.utils.safestring import mark_safe
# Register your models here.
@admin.register(models.Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ['email']


@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'message', 'date_add', 'date_update']


@admin.register(models.About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ['display_image', 'title', 'description', 'date_add', 'date_update']

    def display_image(self, obj):
        return mark_safe(
            f"<img src={obj.image.url} width=100px height=80px"
        )


@admin.register(models.Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ['display_image', 'title', 'description', 'date_add', 'date_update']

    def display_image(self, obj):
        return mark_safe(
            f"<img src={obj.image.url} width=100px height=80px"
        )


@admin.register(models.Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ['name', 'address']


@admin.register(models.HeaderTitle)
class HeaderTitleAdmin(admin.ModelAdmin):
    list_display = ['title']