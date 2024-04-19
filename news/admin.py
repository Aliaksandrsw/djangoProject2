from django.contrib import admin
from django.utils.html import format_html
from django.utils.safestring import mark_safe

from news.models import News, Category


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'category', 'created_at', 'updated_at', 'is_published', 'photo_tag']
    list_display_links = ['title']
    search_fields = ['title', 'created_at']
    list_editable = ('is_published',)
    list_filter = ['is_published', 'category']
    fields = ['title', 'category', 'photo', 'content', 'photo_tag']
    readonly_fields = ['photo_tag', ]

    def photo_tag(self, obj):
        if obj.photo:
            return format_html('<img src="{}" width="75" />'.format(obj.photo.url))
        else:
            return 'фото отсутствует'

    photo_tag.short_description = 'Фото'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    list_display_links = ['title']
    search_fields = ['title']
