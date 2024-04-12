from django.http import HttpResponse
from django.shortcuts import render
from django.views import View


class NewsHome(View):
    def get(self, request, **kwargs):
        return HttpResponse('Хай')