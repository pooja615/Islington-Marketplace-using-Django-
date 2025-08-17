from django.contrib import admin

# Register your models here.
from .models import Page

# class PageAdmin(admin.ModelAdmin):
#     list_display = ('id', 'title', 'slug', 'content', 'created_at')

admin.site.register(Page)