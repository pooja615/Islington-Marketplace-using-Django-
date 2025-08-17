from django.contrib import admin
from . models import Category, Blog
from django.utils.html import format_html

#Register your models here

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'title', 'content', 'author', 'image_preview')
    search_fields = ("title", )
    list_filter = ("category", )
    readonly_fields = ("image_preview", )

    def image_preview(self, obj):
        if obj.blog_image:
            return format_html('<img src="{}" width="80" height="80" style="object-fit:cover;" />', obj.blog_image.url)
        return "No image"
    image_preview.short_description = 'Image'


admin.site.register(Category, CategoryAdmin)
admin.site.register(Blog, BlogAdmin)