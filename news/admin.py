from django.contrib import admin

from news.models import News


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['id','title', 'created_at', 'updated_at', 'is_published']
    list_display_links = ['title']
    search_fields = ['title', 'created_at']