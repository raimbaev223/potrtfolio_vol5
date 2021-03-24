from django.contrib import admin

from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'image', 'body', 'publish']
    list_filter = ['publish',]
    prepopulated_fields = {'slug': ['title',]}
