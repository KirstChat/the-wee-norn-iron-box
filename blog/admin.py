from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):

    readonly_fields = ('posted_by', )

    list_display = (
        'title',
        'post',
        'posted_by',
        'date_posted',
        'status',
    )


admin.site.register(Post, PostAdmin)
