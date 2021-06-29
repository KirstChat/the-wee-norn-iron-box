from django.contrib import admin
from .models import Category, Product


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'brand',
        'category',
        'size')

    list_filter = (
        'category',
        'size')

    search_fields = (
        'name',
        'brand',
        'category__name',
        'size')


admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
