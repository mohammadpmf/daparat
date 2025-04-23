from django.contrib import admin

from .models import BlogPost


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "datetime_created",
        "datetime_modified",
        "likes",
        "author",
    ]
    list_display_links = [
        "title",
        "datetime_created",
        "datetime_modified",
        "likes",
        "author",
    ]
