from django.db import models


class Category(models.Model):

    class Meta:
        verbose_name_plural = "Categories"

    name = models.CharField(max_length=254)

    def __str__(self):
        return self.name

    def get_name(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=254, null=True)
    description = models.TextField(null=True, blank=True)
    brand = models.CharField(max_length=254, null=True, blank=True)
    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)
    size = models.CharField(max_length=20, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
