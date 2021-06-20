from django.contrib import admin
from .models import Order, BoxItems

# Register your models here.


class BoxItemsAdminInline(admin.TabularInline):
    model = BoxItems
    readonly_fields = ('product', )
    list_display = ('product', )


class OrderAdmin(admin.ModelAdmin):
    inlines = (BoxItemsAdminInline,)
    readonly_fields = ('order_number', 'date', 'original_box', 'stripe_pid', )

    fields = ('order_number', 'user_profile', 'date', 'full_name', 'email',
              'contact_number', 'address_line_1', 'address_line_2',
              'town_or_city', 'county', 'postcode', 'country',
              'original_box', 'stripe_pid', )

    list_display = ('order_number', 'date', 'full_name', 'email',
                    'postcode', )

    ordering = ('-date', )


admin.site.register(Order, OrderAdmin)
