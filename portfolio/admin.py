from django.contrib import admin

from .models import Post, Education, Experience, Certificates, Skills, Photo


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'body', 'publish']
    list_filter = ['publish', ]
    prepopulated_fields = {'slug': ['title', ]}


admin.site.register(Education)
admin.site.register(Experience)
admin.site.register(Certificates)
admin.site.register(Skills)
admin.site.register(Photo)
