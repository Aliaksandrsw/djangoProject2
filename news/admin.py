from django.contrib import admin

from news.models import News, Category


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'category', 'created_at', 'updated_at', 'is_published']
    list_display_links = ['title']
    search_fields = ['title', 'created_at']
    list_editable = ('is_published',)
    list_filter = ['is_published', 'category']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    list_display_links = ['title']
    search_fields = ['title']
