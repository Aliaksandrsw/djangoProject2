from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView

from .models import News


class NewsHome(ListView):
    template_name = 'news/index.html'
    context_object_name = 'news'

    def get_queryset(self):
        return News.objects.all()