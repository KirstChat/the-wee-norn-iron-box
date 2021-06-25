from django.contrib import admin
from .models import Review

# Register your models here.


class ReviewsAdmin(admin.ModelAdmin):

    readonly_fields = ('posted_by', )

    list_display = (
        'review',
        'posted_by',
        'rating',
    )


admin.site.register(Review, ReviewsAdmin)
