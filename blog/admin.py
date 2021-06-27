from django.contrib import admin
from .models import Post, Comment


class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('posted_by', )

    list_display = (
        'title',
        'post',
        'posted_by',
        'date_posted',
        'status',
    )

    list_filter = (
        'status',
    )


class CommentAdmin(admin.ModelAdmin):
    readonly_fields = ('posted_by', 'post', )

    list_display = (
        'comment',
        'posted_by',
        'date_commented',
        'post',
    )


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
