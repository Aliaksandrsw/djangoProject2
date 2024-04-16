from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import ListView

from .models import News, Category


class NewsHome(ListView):
    template_name = 'news/index.html'
    context_object_name = 'news'
    extra_context = {
        'title': 'Список новостей',
        'categories': Category.objects.all(),
    }

    def get_queryset(self):
        return News.objects.all()


class NewsCategories(ListView):
    template_name = 'news/index.html'
    context_object_name = 'news'

    def get_queryset(self):
        return News.objects.filter(category_id=self.kwargs['cat_id'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['selected_category'] = Category.objects.get(pk=self.kwargs['cat_id'])
        return context
