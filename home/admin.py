from django.contrib import admin
from .models import Review

# Register your models here.


class ReviewsAdmin(admin.ModelAdmin):

    readonly_fields = ('added_by', )

    list_display = (
        'title',
        'review',
        'added_by',
        'rating',
    )


admin.site.register(Review)
