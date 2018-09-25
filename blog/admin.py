from django.contrib import admin

# Register your models here.

from .models import BlogType, Blog


class BlogTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'type_name')


class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'get_read_num', 'blog_type', 'created_time', 'last_updated_time')
    search_fields = ('author', 'blog_type')
    list_per_page = 35
    list_display_links = ('id', 'title', 'author')
    list_filter = ('blog_type', 'last_updated_time')


admin.site.register(BlogType, BlogTypeAdmin)
admin.site.register(Blog, BlogAdmin)
