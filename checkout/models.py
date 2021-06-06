import uuid

from django.db import models
from django_countries.fields import CountryField

# Create your models here.


class Order(models.Model):
    order_number = models.CharField(max_length=32, null=False, editable=False)
    first_name = models.CharField(max_length=25, null=False, blank=False)
    last_name = models.CharField(max_length=25, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    contact_number = models.CharField(max_length=20, null=True, blank=True)
    address_line_1 = models.CharField(max_length=80, null=False, blank=False)
    address_line_2 = models.CharField(max_length=80, null=False, blank=False)
    town_or_city = models.CharField(max_length=80, null=True, blank=True)
    county = models.CharField(max_length=80, null=True, blank=True)
    postcode = models.CharField(max_length=20, null=False, blank=False)
    country = CountryField(blank_label="Country *", null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True)

    def _generate_order_number(self):
        # Generate Order Number using UUID
        return uuid.uuid4().hex.upper()

    def save(self, *args, **kwargs):
        # Override original save method to set order number
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number
