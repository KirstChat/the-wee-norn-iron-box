from django.contrib import admin
from .models import Category, Product

# Register your models here.
admin.site.register(Category)


@admin.register(Product)
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
