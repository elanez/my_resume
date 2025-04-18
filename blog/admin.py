from django.contrib import admin

from .models import Author, Post, Tag

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_filter = ("author", "tags", "date")
    list_display = ("title", "date", "author", "slug")
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Author)
admin.site.register(Post, PostAdmin)
admin.site.register(Tag)
