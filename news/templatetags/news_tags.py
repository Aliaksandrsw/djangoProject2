from django import template
from django.db.models import Count, F

from news.models import Category

register = template.Library()


@register.inclusion_tag('news/list_categories.html')
def show_categories(selected_category=0):
    categories = Category.objects.annotate(cnt=Count('news', filter=F('news__is_published'))).filter(cnt__gt=0)
    return {"categories": categories,'selected_category':selected_category }
