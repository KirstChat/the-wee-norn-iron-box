from django.contrib import admin
from .models import Order

# Register your models here.


class OrderAdmin(admin.ModelAdmin):
    # Prevent fields from being editable
    readonly_fields = ('order_number', 'date', )

    fields = ('order_number', 'date', 'first_name', 'last_name', 'email',
              'contact_number', 'address_line_1', 'address_line_2',
              'town_or_city', 'county', 'postcode', 'country', )

    list_display = ('order_number', 'date', 'first_name', 'last_name', 'email',
                    'postcode', )

    ordering = ('-date', )


admin.site.register(Order, OrderAdmin)
