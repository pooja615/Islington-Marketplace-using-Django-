from django.contrib import admin

# Register your models here.
from . models import SiteSetting

# class SiteSettingAdmin(admin.ModelAdmin):
#     list_display = ('site_title', 'meta_description', 'meta_keywords', 'logo', 'favicon')

admin.site.register(SiteSetting)